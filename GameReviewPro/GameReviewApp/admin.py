from django.contrib import admin
from GameReviewApp.models import *

# Register your models here.

#自定义管理界面显示数据库表    TODO：// 有待后期改进
class RegisterAdmin(admin.ModelAdmin):
    fields = ('userName','passWord')
    list_per_page = 10
    list_filter = ['userName']

admin.site.register(Register,RegisterAdmin)


class GameReviewInfoAdmin(admin.ModelAdmin):
    fields = ('userName','gameName', 'reviewInfo','date')

    list_per_page = 10
    list_filter = ['userId']

admin.site.register(GameReviewInfo, GameReviewInfoAdmin)

class GameSumAdmin(admin.ModelAdmin):
    fields = ('gameName', 'image','type','platform')

    list_per_page = 10
    list_filter = ['gameName']

admin.site.register(GameSum, GameSumAdmin)

class GameDetailAdmin(admin.ModelAdmin):
    fields = ('gameId','otherName','publishTime','issuer','instruction')
    list_per_page = 10
admin.site.register(GameDetail, GameDetailAdmin)

class StarAdmin(admin.ModelAdmin):
    fields = ('gameId','userId','star')
    list_per_page = 10
admin.site.register(Star, StarAdmin)
