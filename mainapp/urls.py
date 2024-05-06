from django.urls import path
from mainapp.views import master,home,edetails,search,update,delete,all

urlpatterns = [
    path('master',master),
    path('home',home),
    path('edetails',edetails),
    path('search',search),
    path('update',update),
    path('delete',delete),
    path('all',all),
]