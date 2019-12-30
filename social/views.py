from django.shortcuts import render
from django.views import View

class Index(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html', locals())

class Profile(View):

    def get(self, request, *args, **kwargs):
        
        return render(request, 'profile.html', locals())

