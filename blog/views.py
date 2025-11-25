from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from .models import Event_Post


# Create your views here.
def my_blog(request):
    return HttpResponse("Welcome to Soundwave!")


# Blog Post like function
def Blogpost_like(request, post_id):
    post = get_object_or_404(Event_Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('Event_Post_detail', kwargs={'post_id': post_id}))

class Event_Post_detail(DetailView):
    model = Event_Post
    template_name = 'event_post_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Event_Post, id=self.kwargs['post_id'])
        liked = False 
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data    