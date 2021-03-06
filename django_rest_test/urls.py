"""django_rest_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app_history.views import HistoryView, UserView, HistoryByUserView, StatView, LastHistoryView, StatPeriodView, \
    ExcludedPackageView, UserDetailView, ExperimentInfoView, ExperimentInfoDetailView, InterventionListView, InterventionUserView, GoalView

from django_rest_test import settings
from survey import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/history/$', HistoryView.as_view()),
    url(r'^api/user/$', UserView.as_view()),
    url(r'^api/goal/$', GoalView.as_view()),
    url(r'^api/user/(?P<uuid>.+)$', UserDetailView.as_view()),
    url(r'^api/history/(?P<uuid>.+)/date/(?P<start_date>.+)/time/(?P<start_time>.+)$', HistoryByUserView.as_view()),
    url(r'^api/history/(?P<uuid>.+)/date/(?P<start_date>.+)$', HistoryByUserView.as_view()),
    url(r'^api/history/(?P<uuid>.+)$', HistoryByUserView.as_view()),
    url(r'^api/stat$', StatView.as_view()),
    url(r'^api/stat/(?P<uuid>.+)/date/(?P<start_date>.+)$', StatView.as_view()),
    url(r'^api/stat_graph/(?P<uuid>.+)/date/(?P<start_date>.+)$', StatPeriodView.as_view()),
    url(r'^api/stat/(?P<uuid>.+)$', StatView.as_view()),
    url(r'^api/last_history/', LastHistoryView.as_view()),
    url(r'^api/excluded_package/', ExcludedPackageView.as_view()),
    url(r'^api/exp_info/$', ExperimentInfoView.as_view()),
    url(r'^api/exp_info/(?P<type>.+)$', ExperimentInfoDetailView.as_view()),
    url(r'^api/intervention_list/date/(?P<query_date>.+)$', InterventionListView.as_view()),
    url(r'^api/intervention_list/(?P<uuid>.+)/date/(?P<query_date>.+)$', InterventionUserView.as_view()),

    url(r'^graph/$', views.stat_grapth),
    url(r'^graph/sample$', views.sample),
    url(r'^survey/$', views.Index),
    url(r'^survey/(?P<id>\d+)/$', views.SurveyDetail),
    url(r'^survey/confirm/(?P<survey_id>\w+)/$', views.Confirm),
    url(r'^privacy/$', views.privacy),
]
