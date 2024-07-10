from textblob import TextBlob
import matplotlib.pyplot as plt
import tweepy

# Function to authenticate and fetch tweets
def get_tweets(api_key, api_secret, access_token, access_token_secret, query, count=100):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Fetch tweets
    tweets = tweepy.Cursor(api.search, q=query, lang="en").items(count)
    return tweets

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Main function to analyze sentiments and plot results
def main():
    # Twitter API credentials (replace with your own)
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    # Fetch tweets related to women's issues
    query = "women rights OR women empowerment"
    tweets = get_tweets(api_key, api_secret, access_token, access_token_secret, query, count=100)

    # Perform sentiment analysis on fetched tweets
    sentiments = []
    for tweet in tweets:
        sentiments.append(analyze_sentiment(tweet.text))

    # Plotting sentiment analysis results
    plt.figure(figsize=(8, 6))
    plt.hist(sentiments, bins=20, edgecolor='black')
    plt.title('Sentiment Analysis of Tweets on Women\'s Issues')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

if name == "main":
    main()