__author__ = 'Timothy'

import sys
import json

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
    states = {
        'AK': {'score':0, 'num_tweets':0},
        'AL': {'score':0, 'num_tweets':0},
        'AR': {'score':0, 'num_tweets':0},
        'AS': {'score':0, 'num_tweets':0},
        'AZ': {'score':0, 'num_tweets':0},
        'CA': {'score':0, 'num_tweets':0},
        'CO': {'score':0, 'num_tweets':0},
        'CT': {'score':0, 'num_tweets':0},
        'DC': {'score':0, 'num_tweets':0},
        'DE': {'score':0, 'num_tweets':0},
        'FL': {'score':0, 'num_tweets':0},
        'GA': {'score':0, 'num_tweets':0},
        'GU': {'score':0, 'num_tweets':0},
        'HI': {'score':0, 'num_tweets':0},
        'IA': {'score':0, 'num_tweets':0},
        'ID': {'score':0, 'num_tweets':0},
        'IL': {'score':0, 'num_tweets':0},
        'IN': {'score':0, 'num_tweets':0},
        'KS': {'score':0, 'num_tweets':0},
        'KY': {'score':0, 'num_tweets':0},
        'LA': {'score':0, 'num_tweets':0},
        'MA': {'score':0, 'num_tweets':0},
        'MD': {'score':0, 'num_tweets':0},
        'ME': {'score':0, 'num_tweets':0},
        'MI': {'score':0, 'num_tweets':0},
        'MN': {'score':0, 'num_tweets':0},
        'MO': {'score':0, 'num_tweets':0},
        'MP': {'score':0, 'num_tweets':0},
        'MS': {'score':0, 'num_tweets':0},
        'MT': {'score':0, 'num_tweets':0},
        'NA': {'score':0, 'num_tweets':0},
        'NC': {'score':0, 'num_tweets':0},
        'ND': {'score':0, 'num_tweets':0},
        'NE': {'score':0, 'num_tweets':0},
        'NH': {'score':0, 'num_tweets':0},
        'NJ': {'score':0, 'num_tweets':0},
        'NM': {'score':0, 'num_tweets':0},
        'NV': {'score':0, 'num_tweets':0},
        'NY': {'score':0, 'num_tweets':0},
        'OH': {'score':0, 'num_tweets':0},
        'OK': {'score':0, 'num_tweets':0},
        'OR': {'score':0, 'num_tweets':0},
        'PA': {'score':0, 'num_tweets':0},
        'PR': {'score':0, 'num_tweets':0},
        'RI': {'score':0, 'num_tweets':0},
        'SC': {'score':0, 'num_tweets':0},
        'SD': {'score':0, 'num_tweets':0},
        'TN': {'score':0, 'num_tweets':0},
        'TX': {'score':0, 'num_tweets':0},
        'UT': {'score':0, 'num_tweets':0},
        'VA': {'score':0, 'num_tweets':0},
        'VI': {'score':0, 'num_tweets':0},
        'VT': {'score':0, 'num_tweets':0},
        'WA': {'score':0, 'num_tweets':0},
        'WI': {'score':0, 'num_tweets':0},
        'WV': {'score':0, 'num_tweets':0},
        'WY': {'score':0, 'num_tweets':0}
    }

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = create_dict(sent_file)
    tweets = dejsonify(tweet_file)

    tweet_score = list()
    for t in tweets:
        if t.has_key('text'):
            text = t['text'].encode('utf-8')
            score = 0
            for sentiment_key in sent_dict:
                if sentiment_key in text:
                    score = score + sent_dict[sentiment_key]

            if t.has_key('place') and t['place']:
                if t['place'].has_key('full_name') and t['place']['country_code'] == 'US':
                    full_name = t['place']['full_name'].encode('utf-8')
                    state = full_name[len(full_name)-1:-1]
                    if state in states:
                        states[state]['score'] = states[state]['score'] + score
                        states[state]['num_tweets'] = states[state]['num_tweets'] + 1
            elif t.has_key('user'):
                if t['user'].has_key('location') and t['user']:
                    location = t['user']['location'].encode('utf-8')
                    state = location[-2:len(location)]
                    if state in states:
                        states[state]['score'] = states[state]['score'] + score
                        states[state]['num_tweets'] = states[state]['num_tweets'] +  1
            tweet_score.append(score)

    happiest_state = ''
    happiest_state_score = 0
    for state in states:
        try:
            state_score = float(states[state]['score'])/float(states[state]['num_tweets'])
        except:
            state_score = 0
        if state_score > happiest_state_score:
            happiest_state = state

    print happiest_state


if __name__ == '__main__':
    main()