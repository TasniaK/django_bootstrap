from django.conf.urls import url

from . import views


app_name = 'mysite'

# name='' used to prevent hardcoding url names, so if url names change, they can always be refered to by name='' value
# index regex, if it starts and ends with nothing, go to this view
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^[l-p]{4}[_][a-p]{3}[_][a-p]{4}/$', views.PollAppView.as_view(), name='poll_app_page'),
    url(r'^[c-n]{4}[_][b-o]{4}/$', views.ChemBlogView.as_view(), name='chem_blog'),
    url(r'^[a-t]{9}[_][c-t]{7}[_][a-p]{4}/$', views.BootstrapProjectView.as_view(), name='bootstrap_project_page'),
    url(r'^[a-r]{12}[_][a-p]{4}/$', views.CheerleadingView.as_view(), name='cheerleading_page'),

]
