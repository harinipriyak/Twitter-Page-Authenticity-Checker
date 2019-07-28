from flask import Flask, redirect, url_for, request, render_template
from keras.models import model_from_json
from prediction_model import Predictor

app = Flask(__name__)

def load_model():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    global loaded_model
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
    loaded_model._make_predict_function()
    print("Loaded model from disk")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        user = request.form['url']
        id = user.split(".com/", 1)[1]
        (result, followers, friends, avg_retweets, avg_likes) = Predictor().predict(id, loaded_model)
        labels = ["Followers", "Followees"]
        values = [followers, friends]
        colors = ["#F7464A", "#46BFBD"]
        return render_template('result.html', result=int(round(result*100)), set=zip(values, labels, colors),
                               followers=followers, friends=friends, avg_retweets=avg_retweets,
                               avg_likes=avg_likes, id=id)


if __name__ == '__main__':
    load_model()
    app.run()
