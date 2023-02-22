from django.urls import path
from . import views

urlpatterns = [
    path("", views.CategoryViewSet.as_view({
        'get' : 'list',
        'post' : 'create',
    })), #as_view : class를 가져오기위한 규칙
    path("<int:pk>", views.CategoryViewSet.as_view({
        'get' : 'retrieve', #전체에서 한개 가져오는 매소드
        'put' : 'partial_update',
        'delete' : 'destroy',
    })),
]