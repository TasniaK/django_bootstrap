from django.conf.urls import url

from . import views


app_name = 'mysite'

# name='' used to prevent hardcoding url names, so if url names change, they can always be refered to by name='' value
# index regex, if it starts and ends with nothing, go to this view
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url("animation", views.AnimationView.as_view(), name='animation'),
    url("poll_app_page", views.PollAppView.as_view(), name='poll_app_page'),
    url("chem_blog", views.ChemBlogView.as_view(), name='chem_blog'),
    url("bootstrap_project_page", views.BootstrapProjectView.as_view(), name='bootstrap_project_page'),
    url("cheerleading_page", views.CheerleadingView.as_view(), name='cheerleading_page'),

]

