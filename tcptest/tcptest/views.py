from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

class HomeView(View):
    #transform into class-based view with context
    template_name = 'hometemplate.html'
    context = Context({'user' : request.user})

    '''
    def get(self, request, *args):
        template_name = 'hometemplate.html'
        context = Context({'user' : request.user})
        return render(request, template_name, context)
    '''
