# PyAllEars
![logo](https://user-images.githubusercontent.com/17233710/42123523-c11d385a-7c7d-11e8-9393-a3d2a598f6e9.png)

PyAllEars is a project done for analyzing what people say to measure their sentiment value. This was done a means of social media "Eavesdropping". In this project we use "Twitter" as thre Social Media platform. We also wanted to do it in both Facebook and Twitter. However recently they have enforced a very STRICT POLICY on sharing information publicly.

# In this project out work contain 2 major Methods 

<strong>Method 1</strong> Text mining and Analysis on twitter

<strong>Method 2</strong> Online twitter Sentiment Analysis AND Twitter Profile Analyzer SEE ONLINE NOW! http://178.128.40.132/

VIDEOS: PART A : https://youtu.be/pYV1jdDVlfA  PART B : https://youtu.be/rqMQ-VtBidA

[ ALL TWITTER KEYS HAVE BEEN REMOVED IN THE ABOVE CODES. PLEASE GET YOUR OWN KEYS FROM https://apps.twitter.com AND PLACE IT INSIDE THE CODE FOR IT TO WORK ]

# Method 1:Text mining and Analysis on twitter
In this part we use Twitter API to capture all tweets from our interest with the realtime filter tweet an
## Getting Started

First of all you need to run this project in Jupyter Notebook in order to inspect the work and description You can either install <a href='https://www.anaconda.com/download/'> Anaconda</a> that already contained neccessary environmentsand these are Necessary libraries that we'll use for this project:

```
- Json
- pandas
- matplotlib
- re
- matplotlib
- Tweepy

```
then you'll need to create your own twitter app for using Twitter API from this <a href='https://apps.twitter.com' >Link</a>

### Installing

[Anaconda](https://www.anaconda.com/download/)

```
$ pip install tweepy

```
## Running the tests
Run Jupyter Notebook in Terminal

```
$ Jupyter Notebook

```
After It run you can see in the directory [PyAllEars/twitter_Streaming_API/Tweet_Mining and Deep_analyze/](https://github.com/shahud1/PyAllEars/tree/master/twitter_Streaming_API/Tweet_Mining%20and%20Deep_analyze)
It contains  

```
2 Directories
- data
- img

2 python files 
- Tweet Mining and Analyzing.ipynb
- Twitter_stream_api.py

```
Select 
```
Tweet Mining and Analyzing.ipynb
```

And follow along the description inside Jupyter notebook.

## 🤓 Happy Data Science!

# Method 2 Online Twitter Sentimental Analysis AND Twitter profile analyzer

This project contains 2 parts.
### Part A: Online Twitter Sentimental Analysis. ( HOSTED ONLINE )
![alt text](https://github.com/shahud1/PyAllEars/raw/master/Img/Screen%20Shot%202561-06-30%20at%2020.03.25.png)
![alt text](https://github.com/shahud1/PyAllEars/raw/master/Img/Screen%20Shot%202561-06-30%20at%2020.03.38.png)

### Part B: Twitter profile analyzer ( ON THE WAY TO HOST ONLINE )
We tried to analyze @bnk48official 
![alt text](https://github.com/shahud1/PyAllEars/raw/master/Img/Screen%20Shot%202561-06-30%20at%2020.32.04.png)
![alt text](https://github.com/shahud1/PyAllEars/raw/master/Img/Screen%20Shot%202561-06-30%20at%2020.33.30.png)
![alt text](https://github.com/shahud1/PyAllEars/raw/master/Img/Screen%20Shot%202561-06-30%20at%2020.34.06.png)



## Getting Started
Part A: We are hosting this version online as installing this is a difficult task. You can check it out by visiting : http://178.128.40.132/ ( if it doesn't work try the IP address only ). It is hosted on DigitalOceans free version. Hence, there might be some delays. Also, since there is a process running the task of collecting tweets 24/7 the database is pretty huge and so to prevent lag the databse is truncated every 5 days. ( It can get as large as 10 GB in a week! ). Installation of this code will bee demonstrated in the next part. Also, the code for this part was demonostrated by Sentdex in his video. However I have some modifications to that code.

Part B: First of all sorry for not being able to host online. With free version only one can be hosted :/
In this part a Dash app from Flask was created to run the python code demonstraed by x0rz. This is a really powerful code since it allows you to download public profile's any number of tweets. It then does a beautiful analysis about the user which in my opinion is really relavent for an social media eavesdropping app.

### Installing ( For PART A and PART B )
Pip install the following:
- tweepy
- tqdm
- ascii_graph
- numpy
- vaderSentiment
- unidecode
- dash
- dash-renderer
- dash-html-components
- dash-core-components
- plotly
- pandas
- regex
- python-memcached

## VADERsentiment! ALGORITHM used for sentiment analysis ( from https://github.com/cjhutto/vaderSentiment )

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.

## About the Scoring ( from https://github.com/cjhutto/vaderSentiment )
The compound score is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive). This is the most useful metric if you want a single unidimensional measure of sentiment for a given sentence. Calling it a 'normalized, weighted composite score' is accurate.

It is also useful for researchers who would like to set standardized thresholds for classifying sentences as either positive, neutral, or negative. Typical threshold values (used in the literature cited on this page) are:

positive sentiment: compound score >= 0.05
neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
negative sentiment: compound score <= -0.05
The pos, neu, and neg scores are ratios for proportions of text that fall in each category (so these should all add up to be 1... or close to it with float operation). These are the most useful metrics if you want multidimensional measures of sentiment for a given sentence.


## Deployment

Both of these parts can be tested ONLINE and OFFLINE. So we kind of did both.
See the following videos on how we did it!

PART A : https://youtu.be/pYV1jdDVlfA
PART B : https://youtu.be/rqMQ-VtBidA

## Built With
* DASH
* FLASK
* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://github.com/shahud1/PyAllEars/tree/master/twitter_Streaming_API/Tweet_Mining%20and%20Deep_analyze) for details on our code of conduct, and the process for submitting pull requests to us.

## Contributor 

* **Shahud Mohamed**   🏝 (https://github.com/shahud1)
* **Punchok Kerdsiri** 🐲 (https://github.com/punch872)
* **Pathipan Phinkaew**🏯(https://github.com/boycatbay)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

https://matplotlib.org
https://apps.twitter.com
https://developer.twitter.com
http://www.tweepy.org
http://en.wikipedia.org/wiki/Text_mining
http://en.wikipedia.org/wiki/Word-sense_disambiguation
http://en.wikipedia.org/wiki/Regular_expression

