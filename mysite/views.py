# Create your views here.
from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .models import Page, Section


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
            page_data = Page.objects.get(id=1).__dict__
        # ObjectDoesNotExist is a django exception
        except ObjectDoesNotExist:
            page_data = {}

        return render(request, self.template_name, page_data)

    def get(self, request):
        # use try and except to quickly skip to an empty page if get(id=1) errors (does not exist)
        try:
            # use id=1 as this is first section instance so id=1
            # .__dict__ makes Section instance into dictionary as loaded page expects a dictionary not Section instance
            section_data = Section.objects.get(id=1).__dict__
        # ObjectDoesNotExist is a django exception
        except ObjectDoesNotExist:
            section_data = {}

        return render(request, self.template_name, section_data)