from flask import Flask, render_template, url_for, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import sqlite3

#loading saved model
pickle_in = open('fake_news_pickle_model.pkl', 'rb')
model = pickle.load(pickle_in)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    cv = CountVectorizer()
    if request.method == 'POST':
        url = request.form['url']
        title = request.form['title']

        # news text for prediction
        text = request.form['news_text']
        data = [text]
        vect = cv.transform(data).toarray()
        my_prediction = model.predict(vect)

        if my_prediction == 1:
            label = "Fake"
        elif my_prediction == 0:
            label = "Real"

        # connect to the database and save
        with sqlite3.connect("news_data.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into news (url, title, news_text, label) VALUES(?,?,?,?)",
                        (url, title, text, label))
            con.commit()

    return render_template("result.html", prediction=my_prediction)



if __name__ == "__main__":
    app.run(debug=True)