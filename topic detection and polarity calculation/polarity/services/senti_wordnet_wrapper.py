from utils import load_swn, preprocess
from request import Request
import pandas as pd

SWN = load_swn()

class SentiWordNetWrapper:   

    def get_polarity(self, req:Request):
        data = preprocess(req.documents, req.granularity == 'SENTENCE')
        print(data)
        if req.granularity == 'SENTENCE':
            data[['sent_pol','doc_pol']] = data.apply(self.get_sentences_polarity,axis=1)
            data.drop(['texts','lemmas','pos'],axis=1,inplace=True)
        else:
            data['doc_pol'] = data.apply(lambda x:self.get_doc_polarity(zip(x['texts'],x['lemmas'],x['pos'])),axis=1)
            data.drop(['texts','lemmas','pos'],axis=1,inplace=True)
        return data.to_json(orient='records')


    def get_word_polarity(self,text,lemma,pos):
        try:
            positive,negative = SWN[text][pos]
        except:
            try:
                positive,negative = SWN[lemma][pos]
            except:
                positive, negative = 0,0
        print(positive,negative)
        return positive,negative

    
    def get_doc_polarity(self, sentence):
        positive,negative = 0,0
        sent_len = 0
        for text,lemma,pos in sentence:
            sent_len+=1
            temp_pos,temp_neg = self.get_word_polarity(text,lemma,pos)
            positive += temp_pos
            negative += temp_neg 
        return positive/(sent_len or 1), negative/(sent_len or 1)


    def get_sentences_polarity(self,row:pd.Series):
        pol = []
        tot_pol = {'pos':0,'neg':0}
        sents_count = 0
        for s_texts,s_lemmas,s_pos in zip(row['texts'],row['lemmas'],row['pos']):
            sents_count+=1
            polarities = self.get_doc_polarity(zip(s_texts,s_lemmas,s_pos))
            tot_pol['pos']+=polarities[0]
            tot_pol['neg']+=polarities[1]
            pol.append({'pos':polarities[0],'neg':polarities[1]})
        tot_pol['pos']/=sents_count
        tot_pol['neg']/=sents_count
        return pd.Series([pol, tot_pol])