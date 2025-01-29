from django.shortcuts import render, redirect
from .models import Destination, Destination_deatils, Comments
from django.contrib import messages
from django.utils.html import strip_tags

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        dests = Destination.objects.all()
        return render(request,'index.html',{"dests":dests})
    return redirect('login')

def destinations(request, id):
    if request.user.is_authenticated:
        destination = Destination.objects.get(id=id)
        areas = destination.details.all()
        comments = destination.comments.all()
        print(comments)
        return render(request,'destinations.html',{"areas":areas,"destination":destination,"comments":comments})
    return redirect('login')

def comments(request,id):
    if request.method == 'POST':
        user_comment = request.POST['comment-inp']
        dest = Destination.objects.get(id = id)
        if not request.user:
            return redirect('login')
        
        new_comment = Comments.objects.create(
            user=request.user,  
            content=user_comment,
            destination = dest
        )
        new_comment.save()
        messages.info(request,"Comment Saved") 
        return redirect('destinations',id=id)
    

    

def about(request):
    return render(request,'about.html')

def news(request):
    return render(request,'news.html')

def contact(request):
    return render(request,'contact.html')

