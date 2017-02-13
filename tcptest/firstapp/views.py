from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

from models import Item

# Create your views here.
class IndexView(View):
    #transform into class-based view with context
    def get(self, request, *args):
        template_name = 'list_template.html'
        context = Context({'user' : request.user, 'items' : self.get_items()})
        return render(request, template_name, context)

    def get_items(self):
        return Item.objects.all()
