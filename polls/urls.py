from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^registred/$', views.RegisterView.as_view(), name='registred'),
    url(r'^catalogue/$', views.CatalogueView.as_view(), name='catalogue'),
    url(r'^categories/$', views.CategoryView.as_view(), name='categories'),
    # url(r'^categories/(?P<category_name>[0-9]+)$', views.CatalogueView.as_view(), name='categories'),
    url(r'^ajax/catalogue/filtred/$', views.CatalogueView.as_view(), name='filtred'),
    url(r'^brands/$', views.BrandsView.as_view(), name='brands'),
    # url(r'^product/(?P<id>\d+)/$', views.ProductDetail, name='ProductDetail'),
]