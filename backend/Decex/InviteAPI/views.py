from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect
# Create your views here.
from web3 import Web3, HTTPProvider
import os
from django.http import HttpResponse, JsonResponse
from DecexDisplay.views import ShowTestNetWorkPublicSale
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt

from InviteAPI.models import InviteRelationship
from InviteAPI.models import InviteReward
import json

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/00c930c2612f40c4b2aca8d0ad7b030a'))

airDropAddress = '0x2C1534D301480b3E1D4eC5164eFfA7D6F732ABAE'
publicSellToken = '0x67db178a85247CA34cd8968AFc5A05fB2B1d7fC2'


def GetReceipt(re):
    return w3.eth.getTransactionReceipt(re)


def createLink(account):
    # create link and insert into db
    return True


def queryLink(account):
    # query account from db
    # if exist return invitelink
    # else create invitelink
    return True


@csrf_exempt
@api_view(http_method_names=['post'])  # post
@permission_classes((permissions.AllowAny,))
def GetInviteLinkAPI(request):
    if request.method == "GET" and request.GET:
        hash = request.GET.get('th', None)
        ac = request.GET.get('ac', None)
        if hash is None or ac is None:
            return HttpResponse("can't get the value")
        else:
            if VerifyPurchase(hash, ac):
                data = {
                    'inviteCode': hash,
                    'inviter': ac,
                }
                return JsonResponse(data)


def VerifyPurchase(hash, ac):
    reDic = GetReceipt(hash)

    if ac == reDic['from'] and reDic['to'] == publicSellToken:
        return True
    else:
        return False


def InviteIntoPageAPI(request):
    if request.method == "GET" and request.GET:

        hash = request.GET.get('inviteCode', None)

        if hash is None:
            return HttpResponse("can't get the value")

        print(hash)
        invitor = hash

        if w3.isChecksumAddress(hash):
            print(hash)

    # try:
    #     Inviter = GetReceipt(hash)['from']
    # except:
    #     return HttpResponse("invaild inviteCode")
    #
    # # sql
    request.session['inviteCode'] = hash

    return redirect('/publicSale-test/')


def RecordInvitationAPI():
    return True


@csrf_exempt
@permission_classes((permissions.AllowAny,))
def run_job(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'POST':
        try:
            # 解析请求的json格式入参
            data = JSONParser().parse(request)
        except Exception as why:
            print(why.args)
        else:
            content = {'msg': 'SUCCESS'}

            print(data)

            res = InviteRelationship.objects.raw(
                "select * from InviteAPI_inviterelationship where TransactionReceipt = %s ",
                [data['transactionHS'], ])
            if len(res) == 0 and data['inviter'] != data['buyer']:
                inviteRelationship = InviteRelationship(Inviter=data['inviter'], Invitee=data['buyer'],
                                                        TransactionReceipt=data['transactionHS'],
                                                        TransactionReceiptJson=data['transactionJson'],
                                                        )
                inviteRelationship.save()

                if InviteReward.objects.filter(Account=data['inviter']).exists():
                    currentReward = InviteReward.objects.get(Account=data['inviter']).RewardBalance
                    print(currentReward)
                    InviteReward.objects.filter(Account=data['inviter']).update(
                        RewardBalance=currentReward + int(data['transactionJson']['value']) * 0.05)
                else:
                    inviteReward = InviteReward(Account=data['inviter'],
                                                RewardBalance=int(data['transactionJson']['value']) * 0.05)
                    inviteReward.save()

                if InviteReward.objects.filter(Account=data['buyer']).exists():
                    currentReward = InviteReward.objects.get(Account=data['buyer']).RewardBalance
                    print(currentReward)
                    InviteReward.objects.filter(Account=data['buyer']).update(
                        RewardBalance=currentReward + int(data['transactionJson']['value']) * 0.05)
                else:
                    inviteReward = InviteReward(Account=data['buyer'],
                                                RewardBalance=int(data['transactionJson']['value']) * 0.05)
                    inviteReward.save()

            # 返回自定义请求内容content,200状态码
            return JsonResponse(data=content, status=status.HTTP_200_OK)

    # 如果不是post 请求返回不支持的请求方法
    return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)


def test(request):
    print(GetReceipt('0x654a270911b77ce934dfa44e5d3ec5685f34d2c954ea5af130d9d13fa8025d8a'))
    return render(request, "index.html")


def getInviteReward(request):
    ac = request.GET.get('account', None)
    resp = {}

    if InviteReward.objects.filter(Account=ac).exists():
        currentReward = InviteReward.objects.get(Account=ac).RewardBalance
        resp = {'account': ac, 'balance': currentReward, 'detail': 'Get success'}
        print(currentReward)
    else:
        resp = {'account': ac, 'detail': 'Get failed'}

    return HttpResponse(json.dumps(resp), content_type="application/json")
