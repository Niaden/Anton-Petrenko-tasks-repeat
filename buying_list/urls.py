from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anton_petrenko_tasks_repeat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^showlist/$', 'buying_list.views.showlist'),
    url(r'^additem/$', 'buying_list.views.additem'),
    url(r'^contact/$', 'buying_list.views.contact'),
)
