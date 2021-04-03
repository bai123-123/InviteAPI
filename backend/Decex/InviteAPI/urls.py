from django.conf.urls import url
from InviteAPI import views

urlpatterns = [
    url(r'^runJob/$', views.run_job),
    url(r'^queryInviteReward/$', views.getInviteReward),
    url(r'^run/', views.test),
    url('^queryInviteLink/$', views.InviteIntoPageAPI),
    url(r'^run/', views.test),
]
