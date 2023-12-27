from django.shortcuts import render, redirect
from mysite2.models import Post, Mood
from mysite2.forms import ContactForm, Postform, UserRegisterForm, LoginForm

def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all
    if request.method == 'GET':
        return render(request, 'myform.html', locals())
    elif request.method == 'POST':
        try:
            user_id=request.POST[user_id]
            user_pass=request.POST[user_pass]
            user_post=request.POST[user_post]
            user_mood=request.POST[user_mood]
            mood = Mood.objects.get(status=user_mood)
            print(mood)
            post = Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_mood)
            post.save()
            print('save')
            message = f'成功儲存 ! 請記得你的編輯密碼[{user_pass}]! 訊息需經審查後才會顯示'
            return redirect("test-new")
        except:
            message = '出現錯誤'
            return render(request, 'myform.html', locals())
    else:
        pass

def delpost(request, pid=None, del_pass=None):
    if del_pass and pid:
        try:
            post = models.Post.objects.get(id=pid)
            if post.del_pass == del_pass:
                post.delete()
        except:
            pass
    return redirect('/')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'myContact.html', locals())
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            form.user_name
            user_message = form.cleaned_data['user_message']
            print('user_name', user_name)
        return render(request, 'myContact.html', locals())
    else:
        message = "ERROR"
        return render(request, 'myContact.html', locals())
    
def post2db(request):
    if request.method == 'GET':
        form = Postform()
        return render(request, 'myPost2DB.html', locals())
    elif request.method == 'POST':
        form = Postform(request.POST)
        if form._is_valid():
            form.save()
        return render(request, 'myPost2DB.html', locals())
    else:
        message = 'ERROR'
        return render(request, 'myPost2DB.html', locals())



from django.contrib.auth.models import User

def register(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            user_name=form.cleaned_data['user_name']
            user_email=form.cleaned_data['user_email']
            user_password=form.cleaned_data['user_password']
            user_password_confirm=form.cleaned_data['user_name']
            if user_password == user_password_confirm:
                user = user.objects.create_user(user_name, user_email, user_password)
                message = f'註冊成功!'
            else:
                f'兩次密碼不一致!'

        return render(request, 'register.html', locals())
    else:
        message = "ERROR"
        return render(request, 'register.html', locals())


     


