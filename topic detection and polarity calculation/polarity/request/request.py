class Request:
    def __init__(self, documents, detector = 'SWN', granularity = 'SENTENCE'):
        self.documents = documents
        self.detector = detector
        self.granularity = granularity