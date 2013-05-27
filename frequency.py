__author__ = 'Timothy'

import json
import sys

def dejsonify(tweet_file):
    tweets = list()
    for line in tweet_file:
        tweets.append(json.loads(line))
    return tweets

def main():
    tweet_file = open(sys.argv[1])
    tweets = dejsonify(tweet_file)

    tweet_freq = {}

    for t in tweets:
        if t.has_key('text'):
            text = t['text'].encode('utf-8')
            words = text.split()
            for w in words:
                if w in tweet_freq:
                    tweet_freq[w] = tweet_freq[w] + 1
                else:
                    tweet_freq[w] = 1

    total = 0
    for w in tweet_freq:
        total = total + tweet_freq[w]

    for w in tweet_freq:
        print (str(w) + ' ' + str(float(tweet_freq[w])/float(total)))

if __name__ == '__main__':
    main()
