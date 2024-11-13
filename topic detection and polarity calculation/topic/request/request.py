class Request:
    def __init__(self, documents, detector = 'KMEANS', n_topics = 5):
        self.documents = documents
        self.detector = detector
        self.n_topics = n_topics