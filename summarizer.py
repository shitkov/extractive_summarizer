from api_summarizer import Ext_summarizer
from api_preprocessor import Preprocessor

path = ''

if __name__ == '__main__':
    prep = Preprocessor()
    summ = Ext_summarizer()

    text = 'In general there are two types of summarization, abstractive and extractive summarization. Abstractive Summarization: Abstractive methods select words based on semantic understanding, even those words did not appear in the source documents. It aims at producing important material in a new way. They interpret and examine the text using advanced natural language techniques in order to generate a new shorter text that conveys the most critical information from the original text.It can be correlated to the way human reads a text article or blog post and then summarizes in their own word.Input document → understand context → semantics → create own summary.2. Extractive Summarization: Extractive methods attempt to summarize articles by selecting a subset of words that retain the most important points.This approach weights the important part of sentences and uses the same to form the summary. Different algorithm and techniques are used to define weights for the sentences and further rank them based on importance and similarity among each other.Input document → sentences similarity → weight sentences → select sentences with higher rank.The limited study is available for abstractive summarization as it requires a deeper understanding of the text as compared to the extractive approach.Purely extractive summaries often times give better results compared to automatic abstractive summaries. This is because of the fact that abstractive summarization methods cope with problems such as semantic representation,inference and natural language generation which is relatively harder than data-driven approaches such as sentence extraction.There are many techniques available to generate extractive summarization. To keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. One benefit of this will be, you don’t need to train and build a model prior start using it for your project.It’s good to understand Cosine similarity to make the best use of code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Since we will be representing our sentences as the bunch of vectors, we can use it to find the similarity among sentences. Its measures cosine of the angle between vectors. Angle will be 0 if sentences are similar.'

    sentences = prep.clean_text(text)
    sentence_similarity_martix = summ.build_similarity_matrix(prep.normalize(sentences, path))
    summary = summ.summarize(sentences, sentence_similarity_martix)
    print(summary)
