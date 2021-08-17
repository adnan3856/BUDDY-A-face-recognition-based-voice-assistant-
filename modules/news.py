from gnewsclient import gnewsclient
from modules import speakingFile


# Live news
def todays_news(topic_item):
    client = gnewsclient.NewsClient(language='english',location='india',topic=topic_item,max_results=5)
    news_list = client.get_news()
    for item in news_list:
        print(item['title'])
        speakingFile.speak(item['title'])
        print("")

