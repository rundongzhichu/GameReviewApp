from django.db import models

# Create your models here.

#用户注册信息表
class Register(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    passWord = models.CharField(max_length=20,null=False)

# #游戏类别
# class GameType(models.Model):
#     #每插入一个游戏类型，主键ID自增
#     type = models.CharField(max_length=200,primary_key=True)

#游戏评论信息表
class GameReviewInfo(models.Model):
    userId = models.ForeignKey('Register',to_field='userId')
    gameId = models.ForeignKey('GameSum',to_field='gameId')
    reviewInfo = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    #创建联合主键
    class Meta:
        unique_together = ("userId", "gameId","date")


#游戏概要信息表
class GameSum(models.Model):
    gameId = models.AutoField(primary_key=True)
    gameName = models.CharField(max_length=20)
    platform = models.CharField(max_length=20)
    type = models.CharField(max_length=200)
    #将文件所在路径保存在数据库中，将文件保存在photos文件夹中，会存放在media/photos 文件夹下
    image = models.CharField(max_length=300,default="/Static/image/Game/404.jpg")

    # #创建联合主键
    # class Meta:
    #     unique_together = ("gameId")

# #用户点击游戏记录表
# class UserClickGame(models.Model):
#     userId =  models.ForeignKey('Register',to_field='userId')
#     gameName = models.ForeignKey('GameSum',to_field='gameName')
#     type = models.CharField(max_length=200)
#     date = models.CharField(max_length=40)
#
#     #创建联合主键
#     class Meta:
#         unique_together = ("userId", "gameName","date")

class GameDetail(models.Model):
    gameId = models.ForeignKey('GameSum',to_field='gameId')
    otherName = models.CharField(max_length=200)
    publishTime = models.CharField(max_length=40)
    issuer = models.CharField(max_length=20)
    intruction = models.CharField(max_length=100)

class Star(models.Model):
    gameId = models.ForeignKey('GameSum',to_field='gameId')
    userId = models.ForeignKey('Register',to_field='userId')
    star = models.IntegerField(default=0)
    #创建联合主键
    class Meta:
        unique_together = ("userId", "gameId")