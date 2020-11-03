from PIL import Image
import numpy as np
from flask import Flask, request
import json
import hyper as hp
import io
import main



app = Flask(__name__)

@app.route('/check', methods=['GET'])
def check():
    return json.dumps({'respone':'Success'})

@app.route('/predict', methods=['POST'])

def predict():
    data = request.json
    if request.files.get("image"):
        image = request.files["image"].read()
    return json.dumps(data, ensure_ascii=False, cls=None)

if __name__ =="__main__":
    print("App run!")
    app.run(debug=False, host=hp.IP, threaded=False)