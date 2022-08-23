from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Userform,Loginform,Roomform,Messageform,Questionform,Answerform,Filterform
from .models import User,Message,Room,Question,Answer,Topics,Follows
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):

    form=Userform()
    context={'form':form}
    render(request, 'register.html',context)
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        if (User.objects.filter(username=username).count())>0:
            return HttpResponse('username already exists')
        else:
            user=User(email=email,username=username,password=password)
            user.save()
            return redirect('signin')
    else:
        return render(request, 'register.html',context)

def signin(request):
    form=Loginform()
    context={'form':form}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        res=User.objects.filter(username=username,password=password)
        if res:
            request.session['user']=username
            return redirect('profile')
        else:
            return HttpResponse('invalid user credentials')
    else:
        return render(request,'login.html',context)
def profile(request):
    if 'user' in request.session:
        name=request.session['user']
        user=User.objects.get(username=name)
        r=Room.objects.filter(host=User.objects.get(username=name))
        f=Follows.objects.filter(user=User.objects.get(username=name))
        context={'rooms':r,'follows':f,'user':user}
        return render(request, 'profile.html',context)
    else:
        return redirect('signin')
def create_room(request):
    form=Roomform()
    context={'form':form}
    if request.method=='POST':
        if 'user' in request.session:
            host=User.objects.get(username=request.session['user'])
            name=request.POST.get('name')
            description=request.POST.get('description')
            topic=Topics.objects.get(id=request.POST.get('topic'))
            if (Room.objects.filter(name=name).count())>0:
                return HttpResponse('name already exists')
            room=Room(name=name,host=host,description=description,topic=topic)
            room.save()
            return redirect('profile')
    else:
        return render(request, 'createroom.html',context)
def post_message(request,name):
    if request.method=='POST':
        body=request.POST.get('body')
        room=Room.objects.get(name=name)
        message=Message(body=body,room=room)
        message.save()
        return redirect('profile')
def rooms(request):
    if request.method=='POST':
        rooms=Room.objects.filter(topic=request.POST.get('topic'))
        return render(request,'rooms.html',{'rooms':rooms,'form':Filterform})
    return render(request,'rooms.html',{'form':Filterform})
def room(request,name):
    form=Messageform()
    room=Room.objects.get(name=name)
    messages=Message.objects.filter(room=room)
    user=request.session['user']
    if room.host==User.objects.get(username=user):
        context={'m':messages,'r':room,'form':form}
        return render(request,'ownroom.html',context)
    else:
        follow=Follows.objects.filter(room=Room.objects.get(name=name),user=User.objects.get(username=user)).count()
        context={'m':messages,'r':room,'f':follow}
        return render(request,'room.html',context)
def follow(request,name):
    room=Room.objects.get(name=name)
    user=request.session['user']
    follower=User.objects.get(username=user)
    follow=Follows(room=room,user=follower)
    follow.save()
    return redirect('profile')
def unfollow(request,name):
    room=Room.objects.get(name=name)
    user=request.session['user']
    follower=User.objects.get(username=user)
    follow=Follows.objects.get(room=room,user=follower)
    follow.delete()
    return redirect('profile')
def qaf(request):
    user=request.session['user']
    if request.method=='POST':
        questions=Question.objects.filter(topic=request.POST.get('topic'))
    else:
        questions=Question.objects.exclude(user=User.objects.get(username=user))
    
    form=Filterform()
    yourquestions=Question.objects.filter(user=User.objects.get(username=user))
    context={'user':user,'questions':questions,'yourquestions':yourquestions,'form':form}
    return render(request,'qa.html',context)
def post_q(request):
    if request.method=='POST':
        if 'user' in request.session:
            host=User.objects.get(username=request.session['user'])
            question=request.POST.get('question')
            topic=Topics.objects.get(id=request.POST.get('topic'))
            q=Question(user=host,topic=topic,question=question)
            q.save()
            return redirect('QAF')
    else:
        form=Questionform()
        user=request.session['user']
        context={'user':user,'form':form}
        return render(request,'post_q.html',context)
def view_q(request,id):
    form=Answerform()
    question=Question.objects.get(id=id)
    answers=Answer.objects.filter(question=question)
    user=request.session['user']
    if question.user==User.objects.get(username=user):
        context={'a':answers,'q':question}
        return render(request,'answers.html',context)
    else:
        context={'a':answers,'q':question,'form':form}
        return render(request,'postanswers.html',context)
def post_a(request,id):
    question=Question.objects.get(id=id)
    answer=request.POST.get('answer')
    user=User.objects.get(username=request.session['user'])
    a=Answer(answer=answer,question=question,user=user)
    a.save()
    return redirect('QAF')
def logout(request):
    del request.session['user']
    return redirect('home')
    






    


    

