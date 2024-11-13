from flask import Flask, request, Response
from dotenv import load_dotenv
load_dotenv()
from request import Request
from services import ClusterSentences

app = Flask(__name__)

TOPIC_DETECTOR = {
    'KMEANS': ClusterSentences
}

@app.route('/get_topics', methods=['POST'])
def get_topics():
    req = Request(**request.json)
    result = TOPIC_DETECTOR[req.detector]().get_topics(req)
    return Response(result, mimetype='application/json')


#corre el microservicio en el puerto 5000 en el servidor local
if __name__ == '__main__':
    app.run('127.0.0.1',5000)


