import json
import sys

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
    new_term_dict = {}
    for t in tweets:
        if t.has_key('text'):
            text = t['text'].encode('utf-8')
            score = 0
            for sentiment_key in sent_dict:
                if sentiment_key in text:
                    score = score + sent_dict[sentiment_key]

            words = text.split()
            for w in words:
                if w not in sent_dict:
                    if w not in new_term_dict:
                        new_term_dict[w] = score
                    else:
                        new_term_dict[w] = new_term_dict[w] + score

            tweet_score.append(score)

    for term in new_term_dict:
        print (str(term) + ' ' + str(new_term_dict[term]))



if __name__ == '__main__':
    main()
