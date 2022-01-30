from django.db.models import fields
from django.http.response import ResponseHeaders
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import  Post
from .forms import PostForm,EditForm
from django.shortcuts import render ,get_object_or_404
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect , JsonResponse



# Create your views here.

def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked =True
    
    toto_likes =  post.likes.all().count()

    data = {
        'value': liked,
        'likes': toto_likes,
    }
    return JsonResponse(data , safe=False)
  


class HomeView(ListView):
    model = Post
    ordering=['-post_date']
    template_name = 'home.html'



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
        
    def get_context_data(self,*args,**kwargs):
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked= False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked= True
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context

    

class AddpostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'

class UpdatePostViwe(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatePost.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url =reverse_lazy('home')



