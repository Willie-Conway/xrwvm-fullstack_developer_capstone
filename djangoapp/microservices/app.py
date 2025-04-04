from flask import Flask
from nltk.sentiment import SentimentIntensityAnalyzer
import json

app = Flask("Sentiment Analyzer")

sia = SentimentIntensityAnalyzer()

@app.get('/')
def home():
    return "Welcome to the Sentiment Analyzer. \
    Use /analyze/<text> to get the sentiment."

@app.get('/analyze/<input_txt>')
def analyze_sentiment(input_txt):
    scores = sia.polarity_scores(input_txt)
    print(scores)
    
    pos = float(scores['pos'])
    neg = float(scores['neg'])
    neu = float(scores['neu'])
    
    # Set thresholds for sentiment classification
    if pos > 0.1:
        res = "positive"
    elif neg > 0.1:
        res = "negative"
    else:
        res = "neutral"

    print(f"Sentiment Scores: pos={pos}, neg={neg}, neu={neu}")
    print(f"Resulting sentiment: {res}")
    
    result = json.dumps({
        "sentiment": res,
        "scores": scores  # Return the actual sentiment scores for more insight
    })
    return result

if __name__ == "__main__":
    app.run(debug=True)
