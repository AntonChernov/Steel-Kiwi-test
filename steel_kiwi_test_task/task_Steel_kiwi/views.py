from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Category, Product
import datetime
import logging
from project_utils.utils import get_ip_from_request
# Create your views here.

logger = logging.getLogger(__name__)


def show_all_categories(request):
    """
    :param request:
    :return: all categories or error if request not get
    """
    if request.method == 'GET':
        all_categories = get_list_or_404(Category, is_active=True)
        args = {'categories': all_categories, 'title': 'All categories', 'error': False}
        logger.info('show_all_categories OK')
        return render(request, 'categories.html', args)
    else:
        args = {'error': True, 'msg': 'Invalid request!'}
        logger.error('show_all_categories Invalid request! {0}'.format(get_ip_from_request(request)))
        return render(request, 'categories.html', args, status=400)


def show_all_category_products(request, slug=None):
    """
    :param request:
    :param slug: category slag
    :return: all products in category or error if request not get
    """
    if request.method == 'GET':
        all_products = get_list_or_404(Product, category__slug=slug, is_active=True)
        args = {
            'products': all_products,
            'title': 'Products in {0}'.format(slug),
            'category_slug': slug,
            'error': False
        }
        logger.info('show_all_category_products OK')
        return render(request, 'products.html', args)
    else:
        args = {'error': True, 'msg': 'Invalid request!'}
        logger.error('show_all_category_products Invalid request! {0}'.format(get_ip_from_request(request)))
        return render(request, 'categories.html', args, status=400)


def show_product_detail(request, category_slug=None, slug=None):
    """
    :param request:
    :param category_slug: category slug
    :param slug: product slug
    :return: product detail or error if request not get
    """
    if request.method == 'GET':
        category = get_object_or_404(Category, slug=category_slug)
        product = get_object_or_404(Product, slug=slug, is_active=True)
        args = {
            'name': product.name,
            'title': 'Product {0}'.format(slug),
            'category_slug': category.slug,
            'description': product.description,
            'price': product.price,
            'error': False,
        }
        logger.info('show_product_detail OK')
        return render(request, 'product.html', args)
    else:
        args = {'error': True, 'msg': 'Invalid request!'}
        logger.info('show_product_detail Invalid request! {0}'.format(get_ip_from_request(request)))
        return render(request, 'categories.html', {'data': args}, status=400)


def last_add_item(request):
    """
    :param request:
    :return: return all product if product was created at last 24 hours or error if request not get and user not
    authenticated
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            products = get_list_or_404(Product, created_at__gte=datetime.datetime.now() - datetime.timedelta(days=1),
                                       is_active=True)
            args = {
                'products': products,
                'title': 'Added in the last 24 hours',
                'error': False
            }
            logger.info('last_add_item OK')
            return render(request, '24_h_products.html', args)
        args = {'error': True, 'msg': 'User not authorized!'}
        logger.info('last_add_item User not authorized! {0}'.format(get_ip_from_request(request)))
        return render(request, '24_h_products.html', args, status=401)
    args = {'error': True, 'msg': 'Invalid request!'}
    logger.info('last_add_item Invalid request! {0}'.format(get_ip_from_request(request)))
    return render(request, 'categories.html', {'data': args}, status=400)