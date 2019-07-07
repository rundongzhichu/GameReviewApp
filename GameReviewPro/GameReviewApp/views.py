import random
import GameReviewApp.storeData as store
from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse,HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from GameReviewApp import models
import datetime


import logging

from GameReviewApp.lfm import Corpus, LFM

logger = logging.getLogger("console")
# Create your views here.
#前端参考网站
#https://www.cnblogs.com/jl-bai/p/5843322.html


#客户端通过get方式访问注册界面，post方式提交注册信息
class Register(View):
    @csrf_exempt
    def get(self,request):
        return render(request,'register3.html')

    @csrf_exempt
    def post(self,request):
        ret = {"status": 400, "msg": "调用方式错误"}
        userName =request.POST.get('username')
        passWord =request.POST.get('password')
        try:
            user = models.Register.objects.create(userName=userName, passWord=passWord)
            user.save()

            ret['status'] = 200
            ret['msg'] = "注册成功"
            return JsonResponse(ret)
        except Exception as e:
            ret = {"status": 400, "msg": "调用方式错误"}
            return JsonResponse(ret)



class Login(View):
    def get(self,request):
        #如果用户登录了,get('IS_LOGIN', False)如果'IS_LOGIN'存在，就返回TRUE,否则FALSE
        if request.session.get('IS_LOGIN', False):
            return redirect(reverse('master'))
        return render(request,'login.html')

    def post(self,request):
        ret = {"status": 400, "msg": "登录失败！"}
        userName= request.POST.get('username')
        passWord = request.POST.get('password')
        # 验证用户,前面加上models可以防止报错
        user = models.Register.objects.get(userName=userName)

        if user is not None and user.passWord == passWord:
            # 该机制用于将用户信息保存于会话中
            request.session['IS_LOGIN'] = True
            request.session['userName'] = userName
            ret["status"]=200
            ret["msg"] = "登录成功！"
            #如果用户名正确，重定向到主界面, master 为urls中指定的name=参数，reverse 对该名称进行解析，得到它所对应的路径
            return JsonResponse(ret)
        else:
            return JsonResponse(ret)

def registerSuccess(request):
    return render(request, 'registersuccess.html')

def logout(request):
    #删除会话中的用户登录信息
    if request.session.get('IS_LOGIN', False):
        del request.session['IS_LOGIN']
    if request.session.get('userName', False):
        del  request.session['userName']

    return redirect(reverse('master'))


def master(request):

    if request.session.get('IS_LOGIN', False):
        # 查询数据库记录
        # try:
        userName = request.session['userName']

        # user = models.Register.objects.get(userName=userName)
        #
        # lfm =  LFM()
        # #TODO 加载模型用userId进行预测
        # gameId = lfm.predict(user.userId,top_n=6)

        # moviesTemp = []
        # for i in range(6):
        #     moviesTemp.append(models.GameSum.objects.get(gameId=gameId%500))


        gamesum = models.GameSum.objects.all()

        index = random.randint(0,5)
        moviesTemp = []

        for i in range(6):
            moviesTemp.append(gamesum[index])
            index+=1

        # 后端传给前端的交互字典
        gamere = {
            "username": userName,
            "movies": moviesTemp
        }

        return render(request, 'homeSuccess.html', gamere)
        # except Exception as e:
        #     return HttpResponse(e.args, content_type="text/plain")
    else:
        #查询数据库记录，随机的向前端返回六个游戏概要信息
        # try:
        gamesum = models.GameSum.objects.all()

        index = random.randint(0,5)
        moviesTemp = []

        for i in range(6):
            moviesTemp.append(gamesum[index])
            index+=1

        #后端传给前端的交互字典
        gamere = {
            "movies":moviesTemp
        }
        return  render(request, 'home(HTML).html',gamere)
        # except Exception as e:
        #     return HttpResponse(e.args, content_type="text/plain")


def detailGame(request):
    if request.session.get('IS_LOGIN', False):
        # 查询数据库记录，随机的向前端返回六个游戏概要信息
        # try:
        gameId = request.GET["gameId"]

        # 获取概要
        gameS = models.GameSum.objects.get(gameId=gameId)
        gameD = models.GameDetail.objects.get(gameId=gameId)
        gameR = models.GameReviewInfo.objects.filter(gameId=gameId)

        # register = {}
        # for r in gameR:
        #     register[r] = models.Register.objects.get(userId=r.userId).userName


        gameInfo = {
            "gameS": gameS,
            "gameD": gameD,
            "gameR": gameR,
            "username": request.session['userName']
        }
        return render(request, "detailGame.html", gameInfo)
        # except Exception as e:
        #     return HttpResponse(e.args, content_type="text/plain")
    else:
        #查询数据库记录，随机的向前端返回六个游戏概要信息
        # try:
        gameId = request.GET["gameId"]

        logger.debug(gameId)
        # 获取概要
        gameS = models.GameSum.objects.get(gameId=gameId)
        gameD = models.GameDetail.objects.get(gameId=gameId)
        gameR = models.GameReviewInfo.objects.filter(gameId=gameId)

        gameInfo = {
            "gameS": gameS,
            "gameD": gameD,
            "gameR": gameR,
            "username":""
        }
        return render(request, "detailGame1.html", gameInfo)
        # except Exception as e:
        #     return HttpResponse(e.args, content_type="text/plain")


def storeReview(request):
    ret = {"status": 400, "msg": "调用方式错误"}
    content = request.POST.get("content")
    date = request.POST.get("date")

    username = request.POST.get("username")
    gameName = request.POST.get("gameName")

    userId = models.Register.objects.get(userName=username)
    gameId = models.GameSum.objects.get(gameName=gameName)


    logger.debug(username)

    try:
        user = models.GameReviewInfo.objects.create(userId=userId,reviewInfo=content,date=date,gameId=gameId)
        user.save()

        ret['status'] = 200
        ret['msg'] = "注册成功"
        ret['username'] = username
        return JsonResponse(ret)

    except Exception as e:
        logger.debug(e.args)
        ret = {"status": 400, "msg": e.args}
        ret['username'] = username

        return JsonResponse(ret)

def PreDeal(request):
    #插入数据
    try:
        store.storData()
    except Exception as e:
        logger.debug(e.args)

    request.session.flush()

def StoreRating(request):
    if request.session.get('IS_LOGIN', False):
        ret = {"status": 400, "msg": "调用方式错误"}
        rating = request.POST.get("rating")


        logger.debug(rating)

        gameId = request.POST.get("gameId")
        userName = request.session["userName"]

        try:
            register = models.Register.objects.get(userName=userName)
            gameSum = models.GameSum.objects.get(gameId=gameId)
            logger.debug(userName)
            user = models.Star.objects.create(userId=register,star=rating, gameId=gameSum)
            user.save()

            ret['status'] = 200
            ret['msg'] = "评价成功"
            ret['username'] = userName
            return JsonResponse(ret)

        except Exception as e:
            logger.debug(e.args+" ，发生异常！！")
            ret = {"status": 400, "msg": e.args}
            ret['username'] = userName

            return JsonResponse(ret)
    else:
        ret = {"status": 400, "msg": "用户未登录，不能进行评论！！！"}
        return JsonResponse(ret)

# def submitReview(request):
#
#
# def showGameSum(request):
#
# def showGameReviewInfo(request):






