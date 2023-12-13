from django.shortcuts import render, redirect
from mysite2.models import Post, Mood

def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all
    if request.method == 'GET':
        return render(request, 'myform.html', locals())
    elif request.method == 'POST':
        try:
            user_id=
            user_pass=
            user_post=
            user_mood=
            mood = Mood.objects.get(status=user_mood)
            post = Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_mood)
            post.save
            message = f'成功儲存 ! 請記得你的編輯密碼[{user_pass}]! 訊息需經審查後才會顯示'
            return redirect("test-new")
        except:
            message = '出現錯誤'
            return render(request, 'myform.html', locals())
    else:
        pass
    

    return render(request, 'index.html', locals())
     


