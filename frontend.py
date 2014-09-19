import pymongo
import bottle
import cgi
import DBReader


__author__ = 'ZenLunatik64'


@bottle.route('/')
def blog_index():
    postsDict = posts.get_posts(100)
    return bottle.template('frontpage_template', dict(myposts=postsDict))



connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.reddit

posts = DBReader.DBReader(database)

bottle.debug(True)
bottle.run(host='localhost', port=8082)         # Start the webserver running and wait for requests

