# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

import json
import os






def ShowIndex(request):
    return render(request, "index.html")

def ShowNft(request):
    return render(request, "nft.html")

def ShowPublicSale(request):
    return render(request, "publicSale.html")



def ShowTestNetWorkIndex(request):
    return render(request, "index-test.html")

def ShowTestNetWorkNft(request):
    return render(request, "nft-test.html")

def ShowTestNetWorkPublicSale(request):
    return render(request, "publicSale-test.html")






def Box(request):
    return render(request, "xxx.html")


def ControlBoard(request):
    return render(request, "board.html")





