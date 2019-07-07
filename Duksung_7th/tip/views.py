from django.shortcuts import render,get_object_or_404,redirect
from .forms import TipForm
from login.forms import LoginForm
from .models import Tip
from login.models import Login
from django.utils import timezone
from django.http import HttpResponseRedirect,Http404,HttpResponse
import os
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
###############################################################################################3
# Create your views here.
@login_required
def post(request):
    if request.method=="POST":
        form=TipForm(request.POST,request.FILES)
        if form.is_valid():
            tip=form.save(commit=False)
            tip.update_date=timezone.now()
            tip.save()
            return HttpResponseRedirect('/tip/post_list')

    else:
        form=TipForm()
        return render(request,'post.html',{'form':form})


#def show(request):
 #   tips=Tip.objects.order_by('-id')
  #  return render(request,'show.html',{'tips':tips})


def detail(request,tip_id):
    tip_detail=get_object_or_404(Tip,pk=tip_id)

    return render(request,'detail.html',{'tip':tip_detail})

@login_required
def edit(request,pk):

    tip=get_object_or_404(Tip,pk=pk)
    if request.method=="POST":
        form=TipForm(request.POST,request.FILES,instance=tip)
        if form.is_valid():
            tip=form.save(commit=False)
            tip.update_date=timezone.now()
            tip.save()
            return HttpResponseRedirect('/tip/post_list')

    else:
        if tip.u_id == User.objects.get(username = request.user.get_username()):
            form=TipForm(instance=tip)
            return render(request,'edit.html',{'form':form})

@login_required
def delete(request,pk):
    tip=Tip.objects.get(id=pk)
    if tip.u_id == User.objects.get(username = request.user.get_username()):
        tip.delete()
        return redirect('post_list')

def deleteall(request):
    tips=Tip.objects.all()
    for tip in tips:
        tip.delete()
    return render(request,'show.html',{'tips':tips})


@login_required
def download(request,pk):
    upload=get_object_or_404(Tip,pk=pk)
    file_url=upload.file.url[1:]
    if os.path.exists(file_url):
        with open(file_url,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/octet-stream")
            response['attachment']='inline:filename='+os.path.basename(file_url)
            return response
        raise Http404   
  

@login_required
def post_list(request):
    PAGE_ROW_COUNT=10
    PAGE_DISPLAY_COUNT=5

    total_list=Tip.objects.all().order_by('-id')
    paginator=Paginator(total_list,PAGE_ROW_COUNT)
    pageNum=request.GET.get('pageNum')

    toPageCount=paginator.num_pages

    try:
        total_list=paginator.page(pageNum)
    except PageNotAnInteger:
        total_list=paginator.page(1)
        pageNum=1
    except EmptyPage:
        total_list=paginator.page(paginator.num_pages)
        pageNum=paginator.num_pages
    pageNum=int(pageNum)
    
    if pageNum<=PAGE_DISPLAY_COUNT:
         startPageNum=1
    else:
        startPageNum=1+((pageNum-1)/PAGE_DISPLAY_COUNT)*PAGE_DISPLAY_COUNT
    
    endPageNum=startPageNum+PAGE_DISPLAY_COUNT-1
    if toPageCount<endPageNum:
        endPageNum=toPageCount
   

    bottomPages=range(int(startPageNum),int(endPageNum+1))
    
    #no

    tipsnum=range(int(Tip.objects.count()),int(1))
    


    return render(request,'show.html',{
        'tipsnum':tipsnum,
        'total_list':total_list,
        'pageNum':pageNum,
        'bottomPages':bottomPages,
        'toPageCount':toPageCount,
        'startPageNum':startPageNum,
        'endPageNum':endPageNum})


