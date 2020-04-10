from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from api.models import SearchResults
from django.http import JsonResponse
from yapaitek import settings
import datetime as dt
import ghasedak
import requests
import praw


def get_news_from_newsapi(limit=10, key=None, category='general'):
    if key is None:
        url = ('http://newsapi.org/v2/top-headlines?'
               'category=' + category + '&'
               'apiKey=' + settings.NEWS_API_TOKEN)
    else:
        save_searched_keywords(key)
        url = ('http://newsapi.org/v2/top-headlines?'
               'q=' + key + '&'
               'category=' + category + '&'
               'apiKey=' + settings.NEWS_API_TOKEN)

    response = requests.get(url)
    result = response.json()
    list_y = []
    for e in result['articles'][:limit]:
        yy = {
            "headline": e['title'],
            "link": e['url'],
            "publishedAt": e['publishedAt'].replace("T", " "),
            "source": "newsapi"
        }
        list_y.append(yy)
    return list_y

def get_news_from_reddit(limit=10, key='all'):
    reddit = praw.Reddit(client_id=settings.reddit_client_id,
                         client_secret=settings.reddit_client_secret,
                         user_agent=settings.reddit_user_agent,
                         username=settings.reddit_username,
                         password=settings.reddit_password)
    list_x = []
    if key != 'all':
        save_searched_keywords(key)

    for submission in reddit.subreddit(key).hot(limit=limit):
        x = {
            "headline": submission.title,
            "link": submission.url,
            "publishedAt": dt.datetime.fromtimestamp(submission.created).strftime("%Y-%m-%d %H:%M:%S"),
            "source": "reddit"
        }
        list_x.append(x)

    return list_x

def save_searched_keywords(key):
    # TODO: check for duplicate entries
    save_this_searched_key = SearchResults(keyword=key, date_time=dt.datetime.now())
    save_this_searched_key.save()
    pass

def mix_news_together(list_a, list_b):
    """
        list a = ['newsapi','newsapi']
        list b = ['reddit','reddit']
        mixed_list = ['reddit','newsapi', 'reddit', 'newsapi']
    """
    mixed_list = [None] * (len(list_a) + len(list_b))
    mixed_list[::2] = list_a
    mixed_list[1::2] = list_b
    return mixed_list

@api_view(['GET'])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
@permission_classes((AllowAny, IsAuthenticated))
def normal_list(request):
    """
        get the news list
        or
        do a search when needed
    """
    if request.method == 'GET':
        if request.GET.get('q'):
            # do the search thing
            keyword = request.GET.get('q')
            news_api_result = get_news_from_newsapi(key=keyword)
            red_dit_result = get_news_from_reddit(limit=10, key=keyword)
            results = mix_news_together(news_api_result, red_dit_result)

        else:
            # show me the news list
            news_api_result = get_news_from_newsapi(category='general')
            red_dit_result = get_news_from_reddit(limit=10)
            results = mix_news_together(news_api_result, red_dit_result)
    else:
        results = {'message': 'POST Request Not Allowed', 'code': '403'}  # not needed

    return JsonResponse(results, safe=False)


@api_view(['POST'])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
# @permission_classes((AllowAny,IsAuthenticated))
def send_code(request):
    """
        Send Code To Mobile / removed
    """
    sms = ghasedak.Ghasedak("x")
    content = {
        'status_code': '200',
        'data_code': '2120',
        'data': sms,
    }
    return JsonResponse(content, status=200)

@api_view(['POST'])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
# @permission_classes((AllowAny,IsAuthenticated))
def verify_code(request):
    """
     Verify Code From Mobile / removed
    """
    # serializer = serializers.AuthMobileSerializer()
    if request.method == "POST":
        time = dt.datetime.now()
        code = request.data['code']
        check_existence = User.objects.filter(tracking_code=code)
        if check_existence.count() == 0:
            content = {'message': ' موجود نیست'}
            return JsonResponse(content, status=200)
        elif check_existence.count() > 0:
            u = check_existence.first()
            if code == u.tracking_code:
                u.tracking_code = None
                u.is_active = True
                u.save()

            refresh = RefreshToken.for_user(u)
            content = {'access': str(refresh.access_token), 'refresh': str(refresh), 'data': u'فعال شد'}

            return JsonResponse(content, status=200)
    else:
        content = {'access': '403'}
        return JsonResponse(content, status=200)
