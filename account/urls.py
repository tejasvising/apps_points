from django.urls import path
from . import views
from .views import AndroidAppViewSet  #, TaskViewSet,PhotoViewSet
from rest_framework import routers
from account import views
from .views import TaskCreate
router = routers.DefaultRouter()
router.register(r'apps', AndroidAppViewSet)
#router.register(r'tasks', TaskViewSet)
urlpatterns = [
  #  path('', views.index, name= 'index'),
    path('logout/',views.logout_view, name= 'indexapp'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('',views.indexapp,name="indexapp"),
    path('delete/<int:id>/',views.deleteapp,name="deleteapp"),
    path('update/<int:id>/',views.updateapp,name="updateapp"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec"),
    path('addapp/<int:id>/',views.addapp,name='addapp'),
    path('apprec/<int:id>/', TaskCreate.as_view(),name='apprec'),
    path('profile',views.profile,name='userprofile'),
    path('profile/<int:id>/',views.individual,name="individual"),
  #  path('tasks/create/<int:id>/', TaskCreate.as_view(), name='task_create'),
    path('tasks', views.tasks,name='apprec'),
    #path('approve', views.approval,name='approval_page'),
    path('approverec', views.admin_approval,name='approval_page'),
    path('approve', views.approval,name='approval_page'),
   # path('', views.home, name='home'),
    path('addapp/<int:id>/upload/', TaskCreate.as_view(),name='indexapp'),
]