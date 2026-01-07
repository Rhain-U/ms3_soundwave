from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from .models import Post


# Create your views here.
def my_blog(request):
    return HttpResponse("Welcome to Soundwave!")

