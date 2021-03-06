import random
import time
from django.utils.text import slugify


def slug_creator(name=None):
    """
    Accepted name of category or product
    :param name: of category or product
    :return: slugify string
    """
    if name:
        return slugify(str(name) + '-' + str((random.choice(random.sample(range(15000), 15))) +
                       random.choice(random.sample(range(int(time.time())), 5))))
    return slugify((random.choice(random.sample(range(15000), 15))) +
                   random.choice(random.sample(range(int(time.time())), 5)))


def get_ip_from_request(request):
    """
    :param request: HTTP request
    :return: ip address
    """
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return str(ip)
