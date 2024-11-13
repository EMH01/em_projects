import pandas as pd
from utils import spacy_model, stopwords

def preprocess_clusters(documents):
    data_vectors = []
    #aplica pipe a la lista de documentos y ?
    #por cada doc de la lista de docs
    for doc in spacy_model.pipe(documents, disable=['parser','ner', 'attribute_ruler']):
        #por cada oracion linea del doc en particular
        for sentence in doc.sents:
            #crear diccionario con la oracion que se esta evaluando
            sent = {'sent':sentence.text}
            #por cada token de la oracion
            for tok in sentence:
                #si el token tiene vector, esta categorizado en sust,pron o verbo y no esta dentro de la lista de stopwords
                if tok.has_vector and tok.pos_ in ['NOUN','PROPN','VERB'] and tok.text not in stopwords and tok.lemma_ not in stopwords:
                    try:
                        #anadir al diccionario vector de sent la concatenacion de lo que tiene con el nuevo
                        sent['vector']+=tok.vector
                    except:
                        #anadir a sent otro diccionario con key vector que guarde el vector del token
                        sent['vector']=tok.vector
            if 'vector' in sent.keys():
                #para normalizar lo extenso que pueda volverse el vector de una oracion
                sent['vector']/=len(sent['sent'])
                #anadir a la lista datavectors sent que son diccionarios de la oracion correspondiente y vector 
                data_vectors.append(sent)
    #devuelve un dataframe a partir de la lista de datavectors, tipo matriz de vector con texto
    return pd.DataFrame().from_records(data_vectors)
