from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using TextBlob.

    Parameters:
    text (str): The input text whose sentiment needs to be analyzed.

    Returns:
    tuple: A tuple containing the sentiment polarity and subjectivity score.
    """
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment from the TextBlob object
    sentiment = blob.sentiment
    
    # Return the polarity and subjectivity
    return sentiment.polarity, sentiment.subjectivity

# Example usage
text = "I love sunny days. They make me feel so happy!"
polarity, subjectivity = analyze_sentiment(text)
print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")
 
