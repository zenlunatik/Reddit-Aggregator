<!DOCTYPE html>
<html>
<head>
<title>Reddit Aggregator</title>
</head>
<body>

<h1>Reddit Aggregated</h1>

%for collection,posts in myposts.items():
<h1>{{collection}}</h1>
% for post in posts:
<a href="{{post['url']}}">{{post['title']}}</a>
<i>{{post['score']}} {{post['subreddit']}}</i>
<a href="{{post['permalink']}}"><i>Comments</i></a><br>
%end
%end
</body>
</html>


