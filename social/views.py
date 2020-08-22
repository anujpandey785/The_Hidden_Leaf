
from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q

from django.views import View
from social import models,forms
# Create your views here.


class Wall(LoginRequiredMixin,ListView):
    context_object_name ='posts'
    template_name = 'social/wall.html'
    login_url= 'auth/login'

    def get_queryset(self):
        friendIds = [ friend.person2.id for friend in  models.Friends.objects.filter(person1 = self.request.user) ]
        friendIds = friendIds + [ friend.person1.id for friend in  models.Friends.objects.filter(person2 = self.request.user) ]

        return models.Post.objects.filter(user__in = friendIds).order_by('-created_at')

class Home(LoginRequiredMixin,ListView):
    context_object_name='posts'
    template_name='social/home.html'
    login_url='auth/login'

    def get_queryset(self):
        return models.Post.objects.filter(user = self.request.user
        )


    
    def get_context_data(self, **kwargs):
        data = super(Home, self).get_context_data(**kwargs)
        data['post_form'] = forms.PostForm()
        return data
    

class Post(View):
    def post(self,request):
        form=forms.PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/home')

class PostLike(View):
    model=models.Post
    def post(self,request,pk):
        post = self.model.objects.get(pk=pk)
        models.Like.objects.create(post=post,user=request.user)
        return HttpResponse(code = 204)


class PostComment(View):
    model=models.Post
    form=forms.PostCommentForm

    def post(self,request,pk):
        post = self.model.objects.get(pk=pk)
        form = self.form(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.user=request.user
            comment.save()
            return HttpResponse(code = 204)
        return HttpResponse('Error')