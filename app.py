from flask import Flask, request, jsonify
import requests

API_URL = "https://api-inference.huggingface.co/models/nickmuchi/yolos-small-plant-disease-detection"
headers = {"Authorization": "Bearer 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"}

app = Flask(__name__)
@app.route("/index", methods=['GET','POST'])
def index():
    return 'hello there'
def query(data):
    # with open(filename, "rb") as f:
    #     data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

@app.route("/predict", methods=["GET","POST"])
def predict():
    urlimg2 = "https://firebasestorage.googleapis.com/v0/b/farmlabslogin.appspot.com/o/users%2F3jD7eKKvx0RNnTRerAGZh3juhch2%2Fuploads%2F"
    if request.method == "GET":
        img = request.args['img']
        datas = img.split('/')
        urlimg2 = urlimg2 + datas[-1]
        urlimg2 = urlimg2 + '&token=' + request.args['token']
    #contents = urllib2.urlopen(urlimg2).read()
    contents = requests.get(urlimg2).content
    return jsonify(query(contents))

if __name__ == "__main__":
    app.run(debug=True)

# files = {'file': open('test.jpg', 'rb')}
# r = requests.post(url, files=files)
