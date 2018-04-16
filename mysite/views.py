# Create your views here.
from django.shortcuts import render
from django.views import View

# generic views ListView and DetailView used here
# template_name specified to prevent Django using a default template
# get request is faster than post requests but not used for secure data
# get request gives you what you request: matches address to a view, and view returns a html page


class IndexView(View):
    template_name = 'mysite/index.html'

    def get(self, request):
        return render(request, self.template_name, {})