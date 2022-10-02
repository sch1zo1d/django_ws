from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'gallery/index.html', context)

def albums(request):
    return HttpResponse('Альбомы')

def detail(request, album_id):
    return HttpResponse('Это альбом номер %s' % album_id)