import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from popnews.classify import combine_text_and_image
from popnews.classify import predict_image_bias
from popnews.decorators import autologin
from popnews.predict import pred_bias
from popnews.helpers import clean_url
from popnews.helpers import extract_text_and_image
from popnews.models import Article
from popnews.models import ArticleSave


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
@autologin
@login_required
def save_article(request):
    user = request.user
    data = json.loads(request.body.decode())
    title = data.get('title')
    icon = data.get('icon')
    url = data.get('url')
    if not url:
        return HttpResponseBadRequest('Missing url')

    # Clean url
    url = clean_url(url)

    # Extract text and image
    text, image_url = extract_text_and_image(url)
    print(text[0:100])
    print(image_url)

    # Classify url
    bias = 0.5
    if text:
        bias = pred_bias(text)
        print('text bias', bias)
    if image_url:
        concept, concept_value = predict_image_bias(image_url)
        print('image bias', concept, concept_value)
        bias = combine_text_and_image(bias, concept, concept_value)

    # Cap bias to 0 to 1
    bias = min(bias, 1)
    bias = max(bias, 0)
    print('total bias', bias)

    # Save url
    article, _ = Article.objects.get_or_create(url=url)
    article.bias = bias
    article.title = title
    article.icon = icon
    article.save()
    article_save, _ = ArticleSave.objects.get_or_create(user=user,
                                                        article=article)
    return JsonResponse({'bias': -10})


@autologin
@login_required
def user_stats(request):
    user = request.user
    articles_saved = (ArticleSave.objects.filter(user=user)
                      .values('article__url',
                              'article__title',
                              'article__icon',
                              'article__bias'))
    return JsonResponse({'articles': list(articles_saved)})


@autologin
@login_required
def test_save(request):
    return render(request, 'popnews/test_save.html')
