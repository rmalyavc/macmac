from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

app_name="social"

urlpatterns = [
    url(r'^$', views.Index, name='Index'),
    url(r'^news/(?P<ad_slug>[-\w]+)$', views.News, name='News'),
    url(r'^search/$', views.Search, name='Search'),
    url(r'^categories/$', views.CategoryList, name='CategoryList'),
    url(r'^categories/(?P<category_slug>[-\w]+)/$', views.SubCats, name='SubCats'),
    url(r'^brands/$', views.Brands, name='Brands'),
    url(r'^brands/search/$', views.Search, name='Search'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^brands/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.BrandDetail, name='BrandDetail'),
    url(r'^brands/(?P<id>\d+)/(?P<slug>[-\w]+)/search/$', views.Search, name='Search'),
    url(r'^catalogue/(?P<category_slug>[-\w]+)/search/$', views.Search, name='Search'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/search/$', views.Search, name='Search'),
    url(r'^cart/search/$', views.Search, name='Search'),
    url(r'^catalogue$', views.ProductList, name='ProductList'),
    url(r'^catalogue/(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^delivery/$', views.Delivery, name='Delivery'),
    url(r'^register/$', views.Register, name='Register'),
    url(r'^fakecatalogue/$', views.FakeList, name='FakeList'),
    url(r'^fakecatalogue/(?P<category_slug>[-\w]+)/$', views.FakeList, name='FakeListByCategory'),
    url(r'^filted_goods/$', views.FiltedGoods, name='filted_goods'),
    # path('accounts/', include('allauth.urls')),
    # url(r'^social/', include('rest_framework_social_oauth2.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)