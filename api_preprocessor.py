import re
from pymystem3 import Mystem
from string import punctuation

class Preprocessor(object):
    
    def clean_text(self, text):
        '''
        Split text to list of sentance.
        Remove spasers.
        '''
        sentences = text.replace('.', '. ')
        sentences = sentences.split()
        sentences = ' '.join(sentences)
        sentences = sentences.split('. ')
        if sentences[-1][-1] == '.':
            sentences[-1] = sentences[-1][:-1]
        return sentences
    
    def normalize(self, texts, path):
        '''Normalize texts in DataFrame object'''        
        
        rus_dict_file = path + 'rus_stop_dict.txt'
        eng_dict_file = path + 'eng_stop_dict.txt'
        
        try:
            with open(rus_dict_file) as f:
                russian_stopwords = [line.rstrip('\n') for line in f]
        except Exception as err:
            print(err)

        try:
            with open(eng_dict_file) as f:
                english_stopwords = [line.rstrip('\n') for line in f]
        except Exception as err:
            print(err)

        text_list = []
        mystem = Mystem()
        for text in texts:
            text=text.lower()
            text=re.sub("<!--?.*?-->","",text)
            text=re.sub("(\\d|\\W)+"," ",text)

            tokens = mystem.lemmatize(text)

            rus_r = re.compile("[а-я]+")
            eng_r = re.compile("[a-z]+")

            rus_tokens = [w for w in filter(rus_r.match, tokens)]
            eng_tokens = [w for w in filter(eng_r.match, tokens)]

            rus_tokens = [token for token in rus_tokens if token not in
                          russian_stopwords and token != " " and
                          token.strip() not in punctuation]
            
            # take only substantive:
            
            rus_sub_tokens = []
            
            for token in rus_tokens:
                try:
                    if mystem.analyze(token)[0]['analysis'][0]['gr'][0] == 'S':
                        rus_sub_tokens.append(token)
                except:
                    pass

            eng_tokens = [token for token in eng_tokens if token not in
                          english_stopwords and token != " " and
                          token.strip() not in punctuation]

            text = " ".join(rus_sub_tokens) + ' ' + " ".join(eng_tokens)
            text_list.append(text)
        
        return text_list
