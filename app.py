from flask import Flask, render_template, url_for, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import sqlite3

#loading saved model
pickle_in = open('', 'rb')
model = pickle.load(pickle_in)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    cv = CountVectorizer()
    if request.method == 'POST':
        text = request.form['comment']
        data = [text]
        vect = cv.transform(data).toarray()
        my_prediction = model.predict(vect)

    return render_template("result.html", prediction=my_prediction)



if __name__ == "__main__":
    app.run(debug=True)