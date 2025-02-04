from django.shortcuts import render, redirect
from .models import Destination, Comments, IPAddress
from django.contrib import messages
from django.utils.html import strip_tags
from django.http import HttpResponseRedirect



# Create your views here.
def index(request):
    dests = Destination.objects.all()
    if request.user.is_authenticated:
        return render(request,'index.html',{"dests":dests,"user":request.user})
    return render(request,'index.html',{"dests":dests})
    



def destinations(request, id):
    destination = Destination.objects.get(id=id)
    user_liked = destination.liked_by.filter(id=request.user.id).exists()
    user_disliked = destination.disliked_by.filter(id=request.user.id).exists()
    if request.method == 'POST':
        
        if 'like' in request.POST:
            if user_liked:
                destination.liked_by.remove(request.user)
            else:
                destination.liked_by.add(request.user)
                
                
        
        if 'dislike' in request.POST:
            if user_disliked:
                destination.disliked_by.remove(request.user)
            else:
                destination.disliked_by.add(request.user)
                    
        destination.save()
        return HttpResponseRedirect(request.path)
                    
    areas = destination.details.all()
    comments = destination.comments.all()
    likes = destination.liked_by.count()
    dislikes = destination.disliked_by.count()
        
    for comment in comments:
        comment.content = strip_tags(comment.content)
            
        
    print(f"Returning response for destination ID: {id}")
    return render(request,'destinations.html',{"areas":areas,"destination":destination,"comments":comments,"count":len(comments),"likes":likes,"dislikes":dislikes,"user_liked": user_liked,"user_disliked": user_disliked})
    
    
        

def comments(request,id):
    if request.method == 'POST':
        user_comment = request.POST['comment-inp']
        parent_id = request.POST['parent_id']
        parent = None
        if parent_id:
            parent = Comments.objects.get(id = parent_id)
        dest = Destination.objects.get(id = id)
        if not request.user.is_authenticated:
            return redirect('login')
        
        new_comment = Comments.objects.create(
            user=request.user,  
            content=strip_tags(user_comment),
            destination = dest,
            parent_comment=parent
            
        )
        new_comment.save()
        messages.info(request,"Comment Saved") 
        return redirect('destinations',id=id)
    

    