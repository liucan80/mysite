from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list=Question.objects.order_by('pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list
    }
    output=','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)
def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
    # return HttpResponse("you are looking at question %d." % question_id)
def results(request,question_id):
    response="you are looking at the results of question %s."
    return  HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("you are voting on question %s." % question_id)