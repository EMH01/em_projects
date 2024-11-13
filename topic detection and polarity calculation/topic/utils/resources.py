import spacy
import os

spacy_model = spacy.load(os.getenv('SPACY_MODEL'))
spacy_model.add_pipe('sentencizer')

def __load_stopwords():
    with open(os.getenv('STOPWORDS_PATH'), 'r') as stopwords_file:
        stopwords = [line.strip() for line in stopwords_file.readlines()]
        return stopwords

stopwords = __load_stopwords()