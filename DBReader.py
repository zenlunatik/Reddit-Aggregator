__author__ = "ZenLunatik64"

import sys
import time

class DBReader :
    def __init__(self, database) :
        self.db = database
        self.collections = self.db.collection_names()

    def get_posts(self, num_posts) :
        CollectionDict = {}
        for collection in self.collections :
            if collection != "system.indexes" :
                self.db[collection].ensure_index("score", -1)
                cursor = self.db[collection].find().sort('score', direction=-1).limit(num_posts)
                posts = []
                for post in cursor :
                    posts.append({'score' : post['score'],
                                  'url'   : post['url'],
                                  'title' : post['title'],
                                  'subreddit' : post['subreddit'],
                                  'permalink' : 'reddit.com' + post['permalink']
                                 })
                CollectionDict[collection] = posts
        return CollectionDict
