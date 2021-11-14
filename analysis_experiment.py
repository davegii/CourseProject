from typing import Text
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# textblob gives polarity(sentiment ranging from -1 to 1) and subjectivity (ranging 0 to 1) values. 
# text1 = "The food at Bankok Thai is good"
# text2 = "Thanksgiving is comming soon"
# text3 = "The ball is blue"

# complex_text = "This does not taste good" # inaccurate when not is used
# blob1 = TextBlob(text1)
# blob2 = TextBlob(text2)
# blob3 = TextBlob(text3)

# blob_complex_text = TextBlob(complex_text)
# print(blob1.sentiment)
# print(blob2.sentiment)
# print(blob3.sentiment)
# print(blob_complex_text.sentiment)


pos_count = 0
pos_correct = 0

file_positive = open("positive.txt","r")
file_positive_lines = file_positive.readlines()
for line in file_positive_lines:
    analysis = TextBlob(line)

    # if analysis.sentiment.subjectivity >= 0.0001: # find optimal threshold
    if analysis.sentiment.polarity > 0: # find optimal threshold
        pos_correct += 1
    pos_count +=1


neg_count = 0
neg_correct = 0

file_negative = open("negative.txt","r")
file_negative_lines = file_negative.readlines()
for line in file_negative_lines:
    analysis = TextBlob(line)

        #if analysis.sentiment.subjectivity > 0.0001: # find optimal threshold
    if analysis.sentiment.polarity <= 0: # find optimal threshold
        neg_correct += 1
    neg_count +=1

print("Positive accuracy using textBlob= {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy using textBlob= {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

print("Using vaderSentiment")
analyzer = SentimentIntensityAnalyzer()

# The Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1(most extreme negative) and +1 (most extreme positive).
# positive sentiment : (compound score >= 0.05) 
# neutral sentiment : (compound score > -0.05) and (compound score < 0.05) 
# negative sentiment : (compound score <= -0.05)

pos_count = 0
pos_correct = 0

file_positive = open("positive.txt","r")
file_positive_lines = file_positive.readlines()
for line in file_positive_lines:
    v = analyzer.polarity_scores(line)
    if v['neg'] < 0.1:
        if v['pos']-v['neg'] > 0 or v['compound'] >= 0.5:
            pos_correct += 1
    pos_count += 1

neg_count = 0
neg_correct = 0

file_negative = open("negative.txt","r")
file_negative_lines = file_negative.readlines()
for line in file_negative_lines:
    v = analyzer.polarity_scores(line)
    if v['pos'] < 0.1:
        if v['pos']-v['neg'] <= 0 or v['compound'] <= -0.5: # The "=" makes it better
            neg_correct += 1
    neg_count += 1


print("Positive accuracy using vader= {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy using vader= {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
print(" ")



def overall_sentiment(text):
    v = SentimentIntensityAnalyzer()
    percent_sentiment = v.polarity_scores(text)
    print("Text is:", text)
    print("Breakdown: ", percent_sentiment)
    print("Text was rated as ", percent_sentiment['neg']*100, "% Negative")
    print("Text was rated as ", percent_sentiment['neu']*100, "% Neutral")
    print("Text was rated as ", percent_sentiment['pos']*100, "% Positive")

    print("Sentence overall rated As", end = " ")
 
    if percent_sentiment['neg'] < 0.1:
        if percent_sentiment['pos']-percent_sentiment['neg'] > 0 or percent_sentiment['compound'] >= 0.5:
            print("Positive")
 
    elif percent_sentiment['pos'] < 0.1:
        if percent_sentiment['pos']-percent_sentiment['neg'] <= 0 or percent_sentiment['compound'] <= -0.5: # The "=" makes it better
            print("Negative")
        
    else :
        print("Neutral")
    print(" ")

overall_sentiment("Yesterday was the worst day of my life.")