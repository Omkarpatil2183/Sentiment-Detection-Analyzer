from textblob import TextBlob

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
    user_input = input("Enter text to analyze: ")
    sentiment, polarity, subjectivity = analyze_sentiment(user_input)
    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity:.2f}")
    print(f"Subjectivity: {subjectivity:.2f}")
