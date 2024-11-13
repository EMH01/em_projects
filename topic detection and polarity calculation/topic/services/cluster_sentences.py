import json
from sklearn import cluster
#paquete que tiene varios metodos de IA y ML
from request import Request
from utils.preprocess import preprocess_clusters
#preprocesamientos al texto pa luego hacer el agrupamiento
from sklearn.cluster import KMeans
import numpy as np

class ClusterSentences:

    def get_topics(self, req:Request):
        docs = preprocess_clusters(req.documents)
        clusters = self.cluster_docs(docs,req.n_topics)
        #por cada c de los clusters generar lista de sentencias del cluster, resulta una lista que se pasa a json
        return json.dumps([[e.sent for e in c] for c in clusters.values()], ensure_ascii=False)

    def cluster_docs(self, docs, n_clusters=10):
        clusterer = KMeans(n_clusters=n_clusters)
        #ir por cada label agrupando los cluster por topicos
        labels = clusterer.fit(docs['vector'].to_list()).labels_
        clstrs = {}
        for idx,l in enumerate(labels):
            try:
                #cluster en l anade en el idx
                clstrs[l].append(docs.loc[idx])
            except:
                clstrs[l] = [docs.loc[idx]]
        clstrs = self.sort_by_weight(clstrs, clusterer.cluster_centers_)
        #organiza por peso de forma ascendente segun distancias con el centro
        return clstrs


    def sort_by_weight(self, clstrs, cluster_centers):
        for idx, c in clstrs.items():
            for e in c:
                e['distance'] = np.sqrt(np.sum(np.square(e['vector'] - cluster_centers[idx])))
            c = sorted(c,key=lambda x: x['distance'])
            clstrs[idx] = c
        return clstrs