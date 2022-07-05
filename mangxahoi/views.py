from datetime import datetime
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, UpdatePostForm, CommentForm

# Create your views here.

#def mangxahoi(request):
#  return render(request, 'mangxahoi/mangxahoi.html', {})

class MangxahoiView(ListView):
    model = Post
    template_name = 'mangxahoi/mangxahoi.html'
    #ordering = ['-id']
    ordering = ['-post_date']

class ChitietView(DetailView):
    model = Post
    template_name = 'mangxahoi/chitiet.html'

    #def get_context_data(self, *args, **kwargs):
    #    context = super(ChitietView, self).get_context_data
    #
    #    stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    #    total_likes = stuff.total_likes()
    #    context["total_likes"] = total_likes
    #    return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'mangxahoi/add_post.html'
    #fields = '__all__'
    #fields = ('title','body')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'mangxahoi/update_post.html'
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'mangxahoi/delete_post.html'
    success_url = reverse_lazy('mangxahoi:mangxahoi')
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('mangxahoi:chitiet', post.pk)
    #return HttpResponseRedirect(reverse('mangxahoi:chitiet', args=[str(pk)]))




class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'mangxahoi/add_comment.html'
    #fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('mangxahoi:chitiet', kwargs={'pk': self.kwargs['pk']})

    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)


class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'mangxahoi/update_comment.html'

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy('mangxahoi:chitiet', kwargs={'pk': post.id})


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'mangxahoi/delete_comment.html'
    
    def get_success_url(self):
        post = self.object.post
        return reverse_lazy('mangxahoi:chitiet', kwargs={'pk': post.id})



def CommentLikeView(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    if comment.cmt_likes.filter(id=request.user.id).exists():
        comment.cmt_likes.remove(request.user)
    else:
        comment.cmt_likes.add(request.user)
    return redirect('mangxahoi:chitiet', comment.post.pk)   