import pandas as pd
import spacy
from utils import load_stopwords
import os
model = spacy.load(os.getenv('SPACY_MODEL'))
model.add_pipe('sentencizer')
stopwords = load_stopwords()

VALID_POS = {
    'ADJ':'a',
    'NOUN':'n',
    'PROPN':'n',
    'VERB':'v',
}

def preprocess(documents, split_sentences = True):
    docs = []
    for document in model.pipe(documents, disable=['parser','ner', 'attribute_ruler']):
        doc = {'texts':[],'lemmas':[],'pos':[]}
        if split_sentences:
            doc['sentences'] = []
            for sentence in document.sents:
                doc['sentences'].append(sentence.text)
                texts = []
                lemmas = []
                pos = []
                for token in sentence:
                    if token.text not in stopwords and token.lemma_ not in stopwords and token.pos_ in VALID_POS:
                        texts.append(token.text)
                        lemmas.append(token.lemma_)
                        pos.append(VALID_POS[token.pos_])
                doc['texts'].append(texts)
                doc['lemmas'].append(lemmas)
                doc['pos'].append(pos)
        else:
            for token in document:
                if token.text not in stopwords and token.lemma_ not in stopwords and token.pos_ in VALID_POS:
                    doc['texts'].append(token.text)
                    doc['lemmas'].append(token.lemma_)
                    doc['pos'].append(VALID_POS[token.pos_])
        docs.append(doc)

    return pd.DataFrame.from_records(docs)
                