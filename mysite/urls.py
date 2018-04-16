from django.conf.urls import url

from . import views


app_name = 'mysite'

# name='' used to prevent hardcoding url names, so if url names change, they can always be refered to by name='' value
# index regex, if it starts and ends with nothing, go to this view
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

]
