from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anton_petrenko_tasks_repeat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^showrequests/$', 'requests.views.showrequests'),
    url(r'^somefunc/$', 'requests.views.somefunc'),
)
