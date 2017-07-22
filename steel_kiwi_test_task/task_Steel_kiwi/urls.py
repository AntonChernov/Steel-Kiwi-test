from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^last_added_products/$', last_add_item),
    url(r'^(?P<slug>[-\w]+)/$', show_all_category_products),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', show_product_detail),
    url(r'^$', show_all_categories),
]