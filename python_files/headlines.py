
def headlines_gnews():
    from pygooglenews import GoogleNews
    gn=GoogleNews(country='IN')
    news=gn.top_news()
    links_lst=[]
    for i in news['entries'][:8]:
        links_lst.append(i['link'])
    return links_lst
def business_gnews():
    from pygooglenews import GoogleNews
    gn=GoogleNews(country='IN')
    news=gn.topic_headlines('BUSINESS',proxies=None,scraping_bee=None)
    links_lst=[]
    for i in news['entries'][:5]:
        links_lst.append(i['link'])
    return links_lst
def world_gnews():
    from pygooglenews import GoogleNews
    gn=GoogleNews(country='IN')
    news=gn.topic_headlines('WORLD',proxies=None,scraping_bee=None)
    links_lst=[]
    for i in news['entries'][:8]:
        links_lst.append(i['link'])
    return links_lst
def health_gnews():
    from pygooglenews import GoogleNews
    gn=GoogleNews(country='IN')
    snews=gn.topic_headlines('SCIENCE',proxies=None,scraping_bee=None)
    hnews=gn.topic_headlines("CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE/sections/CAQiRENCQVNMUW9JTDIwdk1HdDBOVEVTQldWdUxVZENJZzRJQkJvS0NnZ3ZiUzh3TldScVl5b0tFZ2d2YlM4d05XUnFZeWdBKikIAColCAoiH0NCQVNFUW9JTDIwdk1HdDBOVEVTQldWdUxVZENLQUFQAVAB",
    proxies=None,scraping_bee=None)
    links_lst=[]
    for i in hnews['entries'][:2]:
        links_lst.append(i['link'])
    for i in snews['entries'][:2]:
        links_lst.append(i['link'])
    return links_lst
def tech():
    import requests
    from bs4 import BeautifulSoup
    links_lst=[]
    def momentum():
        r=requests.get('https://www.reuters.com/technology/reuters-momentum/').text
        results=BeautifulSoup(r,'html.parser')
        tech=results.find("div",class_="MediaStoryCard__header___2i8Obf")
        print('Momentum Over')
        return ("https://www.reuters.com"+tech.a['href'])
    links_lst.append(momentum())
    print('Momentum appended')
    def disrupted():
        r=requests.get("https://www.reuters.com/technology/disrupted/").text
        results=BeautifulSoup(r,'html.parser')
        tech=results.find("div",class_="MediaStoryCard__header___2i8Obf")
        print('Disrupted Over')
        return ("https://www.reuters.com"+tech.a['href'])
    links_lst.append(disrupted())
    print('Disrupted Appened')
    def charged():
        r=requests.get("https://www.reuters.com/business/charged/").text
        results=BeautifulSoup(r,'html.parser')
        tech=results.find("div",class_="MediaStoryCard__header___2i8Obf")
        print('Charged Over')
        return ("https://www.reuters.com"+tech.a['href'])
    links_lst.append(charged())
    print('Charged Appened')
    return links_lst
def latest():
    import requests
    from bs4 import BeautifulSoup
    r=requests.get("https://www.livemint.com/latest-news").text
    results=BeautifulSoup(r,'html.parser')
    latest=results.find('div',class_="headlineSec")
    return "https://www.livemint.com"+latest.a['href']
print(latest())





