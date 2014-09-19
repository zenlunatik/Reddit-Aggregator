Reddit-Aggregator
=================

A reddit aggregator using MongoDB, PyMongo, Bottle, urllib2

redditAggregator.py: This script will connect to reddit.com and fetch various subreddits in JSON.
                     Contents of each subreddit are stored as documents in mongodb as collections. Ideally, this should                       run periodically and drop the database before fetching new content. 
                     Here are the set of collections currently being fetched. You can change this to fetch whatever you                       are intertested in.
      collections = {"Motivation"  : ['ZenHabits','DecidingToBeBetter','SelfImprovement',
                                      'HowToNotGiveAFuck','GetMotivated','GetDisciplined', 'Productivity',                                                     'LifeProTips'],
                     "Technology"  : ['Technology', 'Geek', 'BuildAPC', 'AmzingTechnology', 'Gadgets', 'startups',
                                      'ProgrammerHumor', 'networking', 'apple', 'darknetplan', 'TechNewsToday'],
                     "Photography" : ['EarthPorn', 'SpacePorn','CityPorn', 'FoodPorn', 'HistoryPorn', 'CarPorn',
                                      'Photography'],
                     "Programming" : ['Programming', 'coding', 'compsci', 'dailyprogrammer', 'cscareerquestions',                                              'netsec', 'learnpython', 'Python', 'cpp'],
                     "Soccer"      : ['soccer', 'gunners'],
                     "linux"       : ['linux', 'Kernel', 'GNU', 'LinuxAdmin', 'LinuxDevices', 'LinuxQuestions'],
                     "Fitness"     : ['Fitness'],
                     "Interesting" : ['History', 'Psychology', 'AskHistorians', 'TrueReddit', 'ExplainLikeImFive',
                                      'Art', 'Futurology', 'Fascinating', 'Food', 'DIY', 'BestOf', 'Anime', 'Movies',                                          'Television', 'YSK',
                                      'DepthHub', 'Anime'],
                    "Travel"      : ['travel', 'japan', 'SoloTravel', 'Camping', 'RoadTrip', 'CouchSurfing',                                                  'travelpartners', 'Outdoors', 'Backpacking', 'IWantOut'],
                    "Books and writing" : ['Literature', 'FoodForThought', 'Books', 'QuotePorn', 'Quotes', 'Cyberpunk',
                                      'scifi', 'worldbuilding', 'FanTheories' , 'ComicBooks'],
                    "News"              : ['WorldNews', 'worldevents', 'Photoessay', 'india'],
                    "Money"             : ['Frugal', 'Economics', 'Greed'],
                    "Science"           : ['Science', 'askscience'],
                    "Video"             : ['TED', 'Interview', 'Documentaries'],
                    "Music"             : ['ListenToThis', 'HipHopHeads', 'Music'],
                    "Misc"              : ['Photoessay', 'DepthHub', 'SocialEngineering'],
                    "Telelevision and Movies" : ['Television', 'Movies']
              }

frontend.py : This will start a webserver and create a front end that can be accessed at  http://localhost:8082/

views: Contains a sample template that bottle can use
                     
