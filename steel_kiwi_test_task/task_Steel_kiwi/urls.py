from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^last_added_products/$', ShowLastAddProductsForThe24Hours.as_view(), name='24_hours_products'),
    url(r'^(?P<slug>[-\w]+)/$', ShowProductsInCategory.as_view(), name='category_products'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', ShowDetailProductInfo.as_view(), name='product_info'),
    url(r'^$', ShowAllCategories.as_view(), name='categories'),
]