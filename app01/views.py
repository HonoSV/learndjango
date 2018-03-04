from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.


def login(request):
    models.UserGroup.objects.create(caption='dba')
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfoEX.objects.filter(username=u, password=p).first()
        if obj:
            return redirect('/cmd/index/')
        else:
            return render(request, 'login.html')
    else:
        return redirect('/cmd/index')


def orm(request):
    # 创建
    # models.UserInfoEX.objects.create(
    #     username='root',
    #     password='123'
    # )
    # obj = models.UserInfoEX(username='nova', password='123')
    # obj.save()
    # dic = {'username': 'dajuge', 'password': '234'}
    # models.UserInfoEX.objects.create(**dic)

    # 查
    # result = models.UserInfoEX.objects.all()
    # for row in result:
    #     print(row.id, row.username, row.password)
    # result = models.UserInfoEX.objects.filter(username='root')
    # for row in result:
    #     print(row.id, row.username, row.password)

    # 删除
    # models.UserInfoEX.objects.filter(id=3).delete()

    # 一对多
    # models.UserInfoEX.objects.create(
    #     username='xin',
    #     password='666',
    #     email='tencent@qq.com',
    #     test='sd',
    #     user_group_id=models.UserGroup.objects.filter(uid=1).first()
    # )
    models.UserInfoEX.objects.create(
        username='xin',
        password='666',
        email='tencent@qq.com',
        test='sd',
        user_group_id=1
    )

    # 更新
    models.UserInfoEX.objects.filter(id=4).update(password='69')
    return HttpResponse('orm')


def index(request):
    return render(request, 'index.html')


def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfoEX.objects.all()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_info.html', {'user_list': user_list, 'group_list': group_list})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        g_id = request.POST.get('group_id')
        models.UserInfoEX.objects.create(username=u, password=p, user_group_id=g_id)
        return redirect('/cmd/user_info/')


def user_group(request):
    pass


def user_detail(request, nid):
    obj = models.UserInfoEX.objects.filter(id=nid).first()
    return render(request, 'user_detail.html', {'obj': obj})


def user_del(request, nid):
    models.UserInfoEX.objects.filter(id=nid).delete()
    return redirect('/cmd/user_info/')


def user_edit(request, nid):
    if request.method == 'GET':
        obj = models.UserInfoEX.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    if request.method == 'POST':
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfoEX.objects.filter(id=nid).update(username=u, password=p)
        return redirect('/cmd/user_info/')
