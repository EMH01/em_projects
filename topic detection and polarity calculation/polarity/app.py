from flask import Flask, request, Response
from request import Request
from dotenv import load_dotenv
load_dotenv()
from services import SentiWordNetWrapper

app = Flask(__name__)

POLARITY_DETECTOR = {
    'SWN': SentiWordNetWrapper
}

@app.route('/get_polarity', methods=['POST'])
def sentences_polarities():
    req = Request(**request.json)
    result = POLARITY_DETECTOR[req.detector]().get_polarity(req)
    return Response(result, mimetype='application/json')



if __name__ == '__name__':
    app.run(host='127.0.0.1')