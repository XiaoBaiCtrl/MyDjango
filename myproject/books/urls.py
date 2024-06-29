
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('chat-completion/', views.chat_completion, name='chat_completion')

]

# router = DefaultRouter()  # 可以处理视图的路由器
# router.register(r'books', views.BookInfoViewSet)  # 向路由器中注册视图集
#
# urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
