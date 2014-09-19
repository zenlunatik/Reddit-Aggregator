import json
import urllib2
import pymongo

#connect to mongo
connection = pymongo.Connection("mongodb://localhost", safe=True)

#get a handle to the reddit database
db = connection.reddit

collections = {"Motivation"  : ['ZenHabits','DecidingToBeBetter','SelfImprovement',
                              'HowToNotGiveAFuck','GetMotivated','GetDisciplined', 'Productivity', 'LifeProTips'],
               "Technology"  : ['Technology', 'Geek', 'BuildAPC', 'AmzingTechnology', 'Gadgets', 'startups',
                               'ProgrammerHumor', 'networking', 'apple', 'darknetplan', 'TechNewsToday'],
               "Photography" : ['EarthPorn', 'SpacePorn','CityPorn', 'FoodPorn', 'HistoryPorn', 'CarPorn',
                                'Photography'],
               "Programming" : ['Programming', 'coding', 'compsci', 'dailyprogrammer', 'cscareerquestions', 'netsec',
                                'learnpython', 'Python', 'cpp'],
               "Soccer"      : ['soccer', 'gunners'],
               "linux"       : ['linux', 'Kernel', 'GNU', 'LinuxAdmin', 'LinuxDevices', 'LinuxQuestions'],
               "Fitness"     : ['Fitness'],
               "Interesting" : ['History', 'Psychology', 'AskHistorians', 'TrueReddit', 'ExplainLikeImFive',
                                'Art', 'Futurology', 'Fascinating', 'Food', 'DIY', 'BestOf', 'Anime', 'Movies', 'Television', 'YSK',
                                'DepthHub', 'Anime'],
               "Travel"      : ['travel', 'japan', 'SoloTravel', 'Camping', 'RoadTrip', 'CouchSurfing', 'travelpartners',
                                'Outdoors', 'Backpacking', 'IWantOut'],
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


for collection,subreddits in collections.items() :
    mongodbCollection = db[collection]
    for subreddit in subreddits :
        url = 'http://www.reddit.com/r/' + subreddit + '/.json'
        print url
        user_agent = 'redditAgg/1.0 by zenlunatik64'
        headers = { 'User-Agent' : user_agent}
        req = urllib2.Request(url,None, headers)
        response = urllib2.urlopen(req)
        parsed = json.loads(response.read())
        for item in parsed['data']['children']:
            mongodbCollection.insert(item['data'])

