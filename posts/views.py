from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class HelloWorld(View):
    def get(self, request):
        data = {
            'name':'Livingsone Cano Bravo Data',
            'years':28,
            'codes':['Python','Django','React','Vue']
        }

        return render(request,'hello_world.html',context=data)

