from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import os
# Create your views here.


def login(request):
    # f = open('templates/login.html', 'r', encoding='utf-8')
    # data = f.read()
    # f.close()
    # print(request.method)
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        obj = request.FILES.get('fa')
        filepath = os.path.join('upload', obj.name)
        with open(filepath, mode="wb") as f:
            for i in obj.chunks():
                f.write(i)
        if user == 'root' and pwd == "123":
            return redirect('/home')
        else:
            error_msg = "用户名或密码错误"

    return render(request, 'login.html', {'error_msg': error_msg})


USER_LIST = [
    {'username': 'th', 'email': 'fucking', 'gender': '男'},
]
# for index in range(20):
#     temp = {'username': 'th'+str(index), 'email': 'fucking', 'gender': '男'}
#     USER_LIST.append(temp)


def home(request):
    if request.method == 'POST':
        user = request.POST.get('username', None)
        email = request.POST.get('email', None)
        gender = request.POST.get('gender', None)
        temp = {'username': user, 'email': email, 'gender': gender}
        USER_LIST.append(temp)
    return render(request, 'home.html', {'user_list': USER_LIST})

# def home(request):
#     return HttpResponse('<h1>CMDB</h1>')

