import numpy as np
import networkx as nx
import nltk
from nltk.cluster.util import cosine_distance

class Ext_summarizer():
    
    def sentence_similarity(self, sent1, sent2):
        '''
        Calculate cosine similarity between two sentences
        '''
        sent1 = sent1.split(' ')
        sent2 = sent2.split(' ')

        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]

        all_words = list(set(sent1 + sent2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        # build the vector for the first sentence
        for w in sent1:
            vector1[all_words.index(w)] += 1

        # build the vector for the second sentence
        for w in sent2:
            vector2[all_words.index(w)] += 1

        return 1 - cosine_distance(vector1, vector2)

    def build_similarity_matrix(self, sentences):
        '''
        Create similarity matrix
        '''
        # Create an empty similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))
    
        for idx1 in range(len(sentences)):
            for idx2 in range(len(sentences)):
                if idx1 == idx2: #ignore if both are same sentences
                    continue 
                similarity_matrix[idx1][idx2] = self.sentence_similarity(sentences[idx1], sentences[idx2])

        return similarity_matrix

    def summarize(self, sentences, sentence_similarity_martix, top_n=3):
        '''
        Return summary
        '''
        sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
        scores = nx.pagerank(sentence_similarity_graph)
        ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
        
        if top_n > len(sentences):
            top_n = 1

        summarize_text = []
        for i in range(top_n):
            summarize_text.append(ranked_sentence[i][1])

        return '. '.join(summarize_text) + '.'