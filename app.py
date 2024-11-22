from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment, polarity, subjectivity = analyze_sentiment(text)
    return render_template(
        'index.html', text=text, sentiment=sentiment, polarity=polarity, subjectivity=subjectivity
    )

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.polarity
    subjectivity = analysis.subjectivity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, polarity, subjectivity

if __name__ == "__main__":
    app.run(debug=True)
