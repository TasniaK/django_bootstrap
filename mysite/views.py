# Create your views here.
from django.shortcuts import render
from django.views import View

# generic views ListView and DetailView used here
# template_name specified to prevent Django using a default template


class IndexView(View):
    template_name = 'mysite/index.html'

    def get(self, request):
        return render(request, self.template_name, {})