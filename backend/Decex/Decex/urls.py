"""Decex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from DecexDisplay.views import ShowIndex
from DecexDisplay.views import ShowNft
from DecexDisplay.views import ShowPublicSale
from DecexDisplay.views import Box
from DecexDisplay.views import ShowTestNetWorkIndex
from DecexDisplay.views import ShowTestNetWorkNft
from DecexDisplay.views import ShowTestNetWorkPublicSale
from InviteAPI.views import InviteIntoPageAPI
from DecexDisplay.views import ControlBoard
from InviteAPI.views import getInviteReward
from InviteAPI.views import run_job

urlpatterns = [
    #
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    # path('vvue/', TemplateView.as_view(template_name="index.html"), name='index'),
    # url(r'^', include('InviteAPI.urls')),
    # path('publicSale/', ShowPublicSale),
    # path('mainpage/', ShowIndex),
    # path('nft/', ShowNft),
    # path('xxx/', Box),
    #
    # path('publicSale-test/', ShowTestNetWorkPublicSale),
    # path('mainpage-test/', ShowTestNetWorkIndex),
    # path('nft-test/', ShowTestNetWorkNft),
    # path('board/', ControlBoard),
    #
    # re_path('^invite/$', InviteIntoPageAPI),
    url(r'^api/queryInviteReward/$', getInviteReward),
    url(r'^api/record/$', run_job),

    # path('testBrython/', testContract.testBrython),

]
