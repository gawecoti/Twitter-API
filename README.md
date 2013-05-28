Twitter-API
===========

This repository contains Python scripts that interact with the Twitter API to conduct rudimentary sentiment analysis.

1. tweet_sentiment.py - Computes the sentiment of each tweet by taking the sum of the scores of each term in the tweet.
2. term_sentiment.py - Computes the sentiment of terms not provided in AFINN-111.txt
3. frequency.py - Outputs the frequency of each term from a set of tweets
4. happiest_state.py - Returns the happiest state from a set of tweets
5. top_ten.py - Determines the top ten hashtags from a set of tweets

Run
===========

> 1,2 and 4. Python tweet_sentiment.py <file 1> <file 2>
> 3 and 5. Python frequency <file>
