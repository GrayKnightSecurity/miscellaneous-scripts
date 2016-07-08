"""
Pulls data from RSS feeds, looks for a specific date, and returns that day's postings in Markdown-ready format.
Update feedslist to include whatever RSS feeds you're looking for.
Pulldate variable is the date to match, formatted as a (Y, M, D) tuple, e.g. (2016, 6, 27).
By default this looks just for today's news.
"""

import feedparser
import datetime
import slacker

feedslist = ["http://www.us-cert.gov/current/index.rdf","http://feeds.trendmicro.com/Anti-MalwareBlog/","http://threatpost.com/feed","http://www.fireeye.com/blog/feed","http://thirdcertainty.com/feed/","http://www.theregister.co.uk/security/headlines.atom","http://thehackernews.com/feeds/posts/default","http://feeds.feedburner.com/Securityweek","http://www.schneier.com/blog/index.rdf","http://nakedsecurity.sophos.com/feed/","http://www.microsoft.com/technet/security/bulletin/secrss.aspx","http://feeds.feedburner.com/darknethackers","http://krebsonsecurity.com/feed/","http://feeds.feedburner.com/SansInstituteNewsbites","http://feeds2.feedburner.com/security-awareness-tip-of-the-day"]

pulldate = datetime.date.today().timetuple()[:3]

def feedpuller(feedslist):
    link_list = []
    for feed in feedslist:
        d = feedparser.parse(feed)
        for entry in d['entries']:
            try:
                entry_date = entry.published_parsed[:3]
                if entry_date == pulldate:
                    new_link = '[' + entry.title + '](' + entry.link + ')'
                    link_list.append(str(new_link))
            except:
                try:
                    entry_date = entry.updated_parsed[:3]
                    if entry_date == pulldate:
                        new_link = '[' + entry.title + '](' + entry.link + ')'
                        link_list.append(str(new_link))
                except:
                    pass
    return link_list

def slack_push():
    message = feedpuller(feedslist)
    slack = slacker.Slacker('token')
    for i in message[0:]:
        slack.chat.post_message('#headlines', i)

    

if __name__ == "__main__":
    slack_push()
    #print feedpuller(feedslist)
