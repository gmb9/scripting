import feedparser
import datetime
import locale
from time import mktime

def parse_feed(url, url2):
    feed = feedparser.parse(url)
    feed2 = feedparser.parse(url2)
    an_hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
    recent_posts = [entry for entry in feed.entries if datetime.datetime.fromtimestamp(mktime(entry.updated_parsed)) > an_hour_ago]
    recent_posts += [entry for entry in feed2.entries if datetime.datetime.fromtimestamp(mktime(entry.updated_parsed)) > an_hour_ago]

    recent_posts.sort(key = lambda x: x.published_parsed)

    for post in recent_posts:
        print("(", post.updated, ") ", '\n', 'Title: ', post.title, sep="")
        

    #show only items from last hour
    print("finished")



if __name__ == '__main__':
    parse_feed('http://feeds.skynews.com/feeds/rss/us.xml', 'http://rssfeeds.usatoday.com/usatoday-newstopstories&x=1')
