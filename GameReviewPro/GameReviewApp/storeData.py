from GameReviewApp import models
import pandas as pd
import random
import os


def storData():
    #解决文件路径问题
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_ROOT = os.path.join(BASE_DIR, 'Static')
    _change_status_root = os.path.join(STATIC_ROOT, 'data')

    file_path1 =os.path.join(_change_status_root,'GameSum.csv')
    file_path2 = os.path.join(_change_status_root,'GameDetail.csv')
    file_path3 =  os.path.join(_change_status_root,'ratings.csv')

    # # sum = pd.read_csv(file_path1)
    # sum = pd.read_csv(file_path1)
    # #插入500条
    # for i in range(500):
    #     gamesum = models.GameSum(gameId= i+1,gameName= sum['title'][i],type= sum['genres'][i],image= sum['cover'][i],platform=sum['platforms'][i])
    #     gamesum.save()


    sum1 = pd.read_csv(file_path2)
    for i in range(500):
        gamesum = models.GameSum.objects.all()
        gamedetail = models.GameDetail(gameId =gamesum[i] ,otherName = sum1['别名'][i],publishTime = sum1['发行日期'][i],issuer = sum1['开发商'][i],intruction="这个游戏非常好，快点入坑吧！！！！！！")
        gamedetail.save()


    # sum2 = pd.read_csv(file_path3)
    # for i in range(6000):
    #     index = random.randint(1, 500)
    #     try:
    #         star = models.Star(userId=sum2['UserID'][i],gameId=index,star=sum2['Rating'][i])
    #         star.save()
    #     except Exception as e:
    #         i-=1


# storData()







# from GameReviewApp.models import *
# import pandas as pd
#
# file_path = "../data/actor.csv"
#
# frame = pd.read_csv(file_path)
#
# #存GameSum信息
# type = frame['genres']
# platform = frame['platforms']
# gameId =frame['id']
#
#
#
# gamesum = GameSum(gameId=)
# gamesum.save()