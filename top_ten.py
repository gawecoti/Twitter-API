__author__ = 'Timothy'

import sys
import json
import operator
from collections import defaultdict

def dejsonify(tweet_file):
    tweets = list()
    for line in tweet_file:
        tweets.append(json.loads(line))
    return tweets

def main():
    tweet_file = open(sys.argv[1])
    tweets = dejsonify(tweet_file)

    hashes = defaultdict(float)
    for t in tweets:
        if t.has_key('entities') and t['entities']:
            if t['entities'].has_key('hashtags') and t['entities']['hashtags']:
                hash_tweet = t['entities']['hashtags']
                for h in hash_tweet:
                    if h['text'] not in hashes:
                        hashes[h['text']] = 1
                    else:
                        hashes[h['text']] +=  1

    top_ten = sorted(hashes.iteritems(), key = operator.itemgetter(1), reverse = True)
    if len(top_ten) <= 10:
        for i in range(0,len(top_ten)):
            print (str(top_ten[i][0].encode('utf-8')) + ' ' + str(float(top_ten[i][1])))
    else:
        for i in range(0,10):
             print (str(top_ten[i][0].encode('utf-8')) + ' ' + str(float(top_ten[i][1])))

if __name__ == '__main__':
    main()