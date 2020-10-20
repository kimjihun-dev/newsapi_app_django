from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
    newsapi = NewsApiClient(api_key='ea639b3b11674569a687199bf9bc1b19')
    news_headlines = newsapi.get_top_headlines(country='kr')

    data = news_headlines['articles']
    title = []
    desc = []
    url = []
    img = []
    pub = []

    for i in range(len(data)):
        f = data[i]
        title.append(f['title'])
        desc.append(f['description'])
        url.append(f['url'])
        img.append(f['urlToImage'])
        pub.append(f['publishedAt'])

    news_list = zip(title, desc, url, img, pub)
    context = {'news_list': news_list}

    return render(request, 'news/index.html', context)


def business(request):
    newsapi = NewsApiClient(api_key='ea639b3b11674569a687199bf9bc1b19')
    news_headlines = newsapi.get_top_headlines(country='kr', category='business')

    data = news_headlines['articles']
    title = []
    desc = []
    url = []
    img = []
    pub = []

    for i in range(len(data)):
        f = data[i]
        title.append(f['title'])
        desc.append(f['description'])
        url.append(f['url'])
        img.append(f['urlToImage'])
        pub.append(f['publishedAt'])

    news_list = zip(title, desc, url, img, pub)
    context = {'news_list': news_list}

    return render(request, 'news/business.html', context)


def enter(request):
    newsapi = NewsApiClient(api_key='ea639b3b11674569a687199bf9bc1b19')
    news_headlines = newsapi.get_top_headlines(country='kr', category='entertainment')

    data = news_headlines['articles']
    title = []
    desc = []
    url = []
    img = []
    pub = []

    for i in range(len(data)):
        f = data[i]
        title.append(f['title'])
        desc.append(f['description'])
        url.append(f['url'])
        img.append(f['urlToImage'])
        pub.append(f['publishedAt'])

    enterNews_list = zip(title, desc, url, img, pub)
    context = {'enterNews_list': enterNews_list}

    return render(request, 'news/enter.html', context)


def health(request):
    newsapi = NewsApiClient(api_key='ea639b3b11674569a687199bf9bc1b19')
    news_headlines = newsapi.get_top_headlines(country='kr', category='health')

    data = news_headlines['articles']
    title = []
    desc = []
    url = []
    img = []
    pub = []

    for i in range(len(data)):
        f = data[i]
        title.append(f['title'])
        desc.append(f['description'])
        url.append(f['url'])
        img.append(f['urlToImage'])
        pub.append(f['publishedAt'])

    news_list = zip(title, desc, url, img, pub)
    context = {'news_list': news_list}

    return render(request, 'news/health.html', context)


def science(request):
    newsapi = NewsApiClient(api_key='ea639b3b11674569a687199bf9bc1b19')
    news_headlines = newsapi.get_top_headlines(country='kr', category='science')

    data = news_headlines['articles']
    title = []
    desc = []
    url = []
    img = []
    pub = []

    for i in range(len(data)):
        f = data[i]
        title.append(f['title'])
        desc.append(f['description'])
        url.append(f['url'])
        img.append(f['urlToImage'])
        pub.append(f['publishedAt'])

    news_list = zip(title, desc, url, img, pub)
    context = {'news_list': news_list}

    return render(request, 'news/science.html', context)


def sports(request):
    newsapi = NewsApiClient(api_key='ea639b3b11674569a687199bf9bc1b19')
    news_headlines = newsapi.get_top_headlines(country='kr', category='sports')

    data = news_headlines['articles']
    title = []
    desc = []
    url = []
    img = []
    pub = []

    for i in range(len(data)):
        f = data[i]
        title.append(f['title'])
        desc.append(f['description'])
        url.append(f['url'])
        img.append(f['urlToImage'])
        pub.append(f['publishedAt'])

    news_list = zip(title, desc, url, img, pub)
    context = {'news_list': news_list}

    return render(request, 'news/sports.html', context)


def tech(request):
    newsapi = NewsApiClient(api_key='ea639b3b11674569a687199bf9bc1b19')
    news_headlines = newsapi.get_top_headlines(country='kr', category='technology')

    data = news_headlines['articles']
    title = []
    desc = []
    url = []
    img = []
    pub = []

    for i in range(len(data)):
        f = data[i]
        title.append(f['title'])
        desc.append(f['description'])
        url.append(f['url'])
        img.append(f['urlToImage'])
        pub.append(f['publishedAt'])

    news_list = zip(title, desc, url, img, pub)
    context = {'news_list': news_list}

    return render(request, 'news/tech.html', context)