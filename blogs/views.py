from django.shortcuts import render, HttpResponse, redirect


def root(request):
    return HttpResponse("this is index with method root")


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect("/")


def show(request, num):
    return HttpResponse(num)
