from  django.urls import path,include
from . import views

urlpatterns = [
    path('checkserver/', views.index, name = 'index'),
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('restricted/',views.restricted)
   

]