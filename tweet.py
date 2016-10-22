from twython import Twython, exceptions
import urllib2
import json


def create_auth():
    with open("access.json", "r") as a:
        access = json.load(a)
        return Twython(
            access["API_Key"], access["API_Secret"],
            access["Access_Token"], access["Access_Token_Secret"]
        )


def post_tweet(status):
    tweet = create_auth()
    try:
        tweet.update_status(status=status)
    except exceptions.TwythonError:
        status_update = get_status()
        if len(status_update) <= 140:
            post_tweet(status_update)


def get_status():
    # url = "http://quotes.rest/bible/verse.json"
    # url = "http://api.icndb.com/jokes/random"
    url = "http://ron-swanson-quotes.herokuapp.com/v2/quotes"
    data = urllib2.urlopen(url)
    status_update = json.load(data)
    print "%s" % (status_update[0],)
    return status_update


if __name__ == "__main__":
    # post_tweet(get_status())
    status = get_status()
    if len(status) <= 140:
        post_tweet(status)
    else:
        print "Long Status"
