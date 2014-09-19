Reddit-Aggregator
=================

A reddit aggregator using MongoDB, PyMongo, Bottle, urllib2

redditAggregator.py: This script will connect to reddit.com and fetch various subreddits in JSON.
                     Contents of each subreddit are stored as documents in mongodb as collections. Ideally, this should                         run periodically and drop the database before fetching new content. It has a set of subreddits                             currently being fetched. You can change this to fetch whatever you are intertested in.
      
frontend.py : This will start a webserver and create a front end that can be accessed at  http://localhost:8082/

views: Contains a sample template that bottle can use
                     
