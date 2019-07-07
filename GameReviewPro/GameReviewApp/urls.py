from django.conf.urls import url

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

#表示控制器传来访问时，根据参数选择要执行的url
urlpatterns = [
    url(r"^register/$",views.Register.as_view(),name='register'),
    url(r"^login/$",views.Login.as_view(),name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r"^master/$",views.master,name='master'),
    url(r"^registerSuccess/$", views.registerSuccess,name='resuccess'),
    # url(r"^homeSuccess/",views.homeSuccess,name='hsuccess'),
    url(r"^detailGame/", views.detailGame,name='gamedetail'),
    url(r"^storeReview/", views.storeReview,name='storeReview'),
    url(r"^predeal/", views.PreDeal,name='predeal'),
    url(r"^rating/", views.StoreRating,name='rating'),
]

#配置js、css的访问路径
urlpatterns += staticfiles_urlpatterns()

#url(r'(\d+)\$',views.detail) 会自动把匹配到的组收集起来，传参给detail
#url(r'(\d+)\$',views.detail)  前一个是正则表达式，后一个是要执行的内容，\$ 表示$本身
#^表示匹配字符串开头