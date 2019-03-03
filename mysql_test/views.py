from django.shortcuts import render
from django.http import HttpResponse
from .models import minitest,userinfo
# Create your views here.
def test(request):
    title = 'Nice to meet you'
    return render(request, 'lean.html', {'Title':title})
def index(request):
    user_list_obj1 = minitest.objects.all()
    title1 = 'Nice to meet you ,boy!!'
    return render(request, 'mysql.html', {'li':user_list_obj1},{'Title':title1})
def db_handle(request):
      user_list_obj2 = userinfo.objects.all()
      return render(request,'Showmysql.html',{'li':user_list_obj2})