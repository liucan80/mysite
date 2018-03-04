from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(Request):
    return HttpResponse('hello')
def detail(request,question_id):
    return HttpResponse("you are looking at question %d." % question_id)
def results(request,question_id):
    response="you are looking at the results of question %s."
    return  HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("you are voting on question %s." % question_id)