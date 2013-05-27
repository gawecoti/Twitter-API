import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def create_dict(sent_file):
    scores = {}
    for line in sent_file:
        term,score = line.split('\t')
        scores[term] = int(score)
    return scores

def dejsonify(tweet_file):
    tweets = list()
    for line in tweet_file:
        tweets.append(json.loads(line))
    return tweets

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_dict = create_dict(sent_file)
    tweets = dejsonify(tweet_file)

    tweet_score = list()
    for t in tweets:
        text = t['text'].encode('utf-8')
        score = 0
        for sentiment_key in sent_dict:
            if sentiment_key in text:
                score = score + sent_dict[sentiment_key]
        tweet_score.append(score)

    for score in tweet_score:
        print score


if __name__ == '__main__':
    main()
