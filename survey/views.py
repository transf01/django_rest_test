from django.core.serializers import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
import datetime
from django_rest_test import settings

from survey.models import Question, Survey, Category, AnswerRadio
from survey.forms import ResponseForm

from django.contrib.auth.models import User


def Index(request):
    return render(request, 'survey/index.html')


def SurveyDetail(request, id):
    survey = Survey.objects.get(id=id)
    category_items = Category.objects.filter(survey=survey)
    categories = [c.name for c in category_items]

    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)

        if form.is_valid():
            response = form.save()
            return HttpResponseRedirect("/survey/confirm/%s" % id)
    else:
        form = ResponseForm(initial={'user_id': request.GET.get('user_id')}, survey=survey)

    print(form)
    return render(request, 'survey/survey.html',
                  {'response_form': form, 'survey': survey, 'categories': categories })


def Confirm(request, survey_id):
    email = settings.support_email
    return render(request, 'survey/confirm.html', {'survey_id': survey_id, "email": email})


def privacy(request):
    return render(request, 'survey/privacy.html')

def stat_grapth(request):
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    return render(request, 'graph/stacked_column_ver3.html', {'user_id':request.GET.get('user_id'), 'start_date': monday})


def sample(request) :
    return render(request, 'graph/stacked.html')

