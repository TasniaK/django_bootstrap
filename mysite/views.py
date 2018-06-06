# Create your views here.
from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .models import Page, Section
#import pdb


# each page needs a view
# generic views ListView and DetailView used here
# template_name specified to prevent Django using a default template
# get request is faster than post requests but not used for secure data
# get request gives you what you request: matches address to a view, and view returns a html page



class IndexView(View):
    template_name = 'mysite/index.html'

    def get(self, request):
        # use try and except to quickly skip to an empty page if get(id=1) errors (does not exist)
        try:
            # use id=1 as this is first page instance so id=1
            # .__dict__ makes Page instance into dictionary as loaded page expects a dictionary not Page instance
            context = {}
            page_data = Page.objects.get(name='Home Page')
            section_data = Section.objects.all()
            context['page'] = page_data


        # ObjectDoesNotExist is a django exception
        except ObjectDoesNotExist:
            context = {}


        return render(request, self.template_name, context)

class PollAppView(View):
    template_name = 'mysite/poll_app_page.html'

    def get (self, request):
        return render(request, self.template_name, {})

class ChemBlogView(View):
    template_name = 'mysite/chem_blog.html'

    def get(self, request):
        return render(request, self.template_name, {})

class BootstrapProjectView(View):
    template_name = 'mysite/bootstrap_project_page.html'

    def get(self, request):
        return render(request, self.template_name, {})

class CheerleadingView(View):
    template_name = 'mysite/cheerleading_page.html'

    def get(self, request):
        return render(request, self.template_name, {})

class AnimationView(View):
    template_name = 'mysite/animation.html'

    def get(self, request):
        return render(request, self.template_name, {})