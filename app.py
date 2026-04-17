from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# model & vectorizer load
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['resume']
    data = vectorizer.transform([text])
    prediction = model.predict(data)
    final_output = encoder.inverse_transform(prediction)
    return render_template('index.html', result=final_output[0])

if __name__ == "__main__":
    app.run(debug=True)