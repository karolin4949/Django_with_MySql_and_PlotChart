from django.shortcuts import render
from django.http import HttpResponse
from .models import UserTest   #实体类（模型）的引入

# Create your views here.
def user_show(request):
    users=UserTest.objects.all()  #获取全部数据
    listx = []
    listy = []
    for user in users:  #遍历，拼横纵坐标
        listx.append(str(user.name))  
        listy.append(int(user.age))
    return render(request, "show.html", {'users':users, 'X':listx, 'Y':listy}) 
#跳转到show.html，并将拼好的数据（{'users':users, 'X':listx, 'Y':listy}）传递到该页面
