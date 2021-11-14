from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#analyzer = SentimentIntensityAnalyzer()

def overall_sentiment(text):
    v = SentimentIntensityAnalyzer()
    percent_sentiment = v.polarity_scores(text)
    #print("Text is:", text)
    print("Text is:", text.strip())
    print("Breakdown: ", percent_sentiment)
    print("Text was rated as ", percent_sentiment['neg']*100, "% Negative")
    print("Text was rated as ", percent_sentiment['neu']*100, "% Neutral")
    print("Text was rated as ", percent_sentiment['pos']*100, "% Positive")

    #print("Sentence overall rated as", end = " ")
 
    if percent_sentiment['neg'] < 0.1:
        if percent_sentiment['pos']-percent_sentiment['neg'] > 0 or percent_sentiment['compound'] >= 0.5:
            print("Sentence overall rated as positive")
            print("\n")
            #print("Positive")
            return "Positive"
 
    if percent_sentiment['pos'] < 0.1:
        if percent_sentiment['pos']-percent_sentiment['neg'] <= 0 or percent_sentiment['compound'] <= -0.5: # The "=" makes it better
            print("Sentence overall rated as positive")
            print("\n")
           #print("Negative")
            return "Negative"
        
    else :
        print("Sentence overall rated as positive")
        print("\n")
        #print("Neutral")
        return "Neutral"
    


pos_count = 0
pos_correct = 0

file_positive = open("positive.txt","r")
file_positive_lines = file_positive.readlines()
for line in file_positive_lines:
    sentiment = overall_sentiment(line)
    if sentiment == "Positive":
            pos_correct += 1
    pos_count += 1

neg_count = 0
neg_correct = 0

file_negative = open("negative.txt","r")
file_negative_lines = file_negative.readlines()
for line in file_negative_lines:
    sentiment = overall_sentiment(line)
    if sentiment == "Negative":
        neg_correct += 1
    neg_count += 1

print("Positive accuracy using vader= {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy using vader= {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
