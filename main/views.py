from django.shortcuts import render, render_to_response


# Create your views here.
def home(request, *args, **kwargs):

    return render_to_response("main/home.html")
