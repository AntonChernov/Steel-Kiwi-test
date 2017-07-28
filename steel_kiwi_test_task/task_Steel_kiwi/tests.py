from django.test import TestCase, Client
from .models import Category, Product
from django.utils.text import slugify
from project_utils.utils import slug_creator
import mimesis
import random
# Create your tests here.


class ProductsDetail(TestCase):
    def setUp(self):
        hardware = mimesis.Hardware()
        text = mimesis.Text()
        for _ in range(5):
            randomize_hardware = random.choice([hardware.cpu(), hardware.graphics()])
            Category.objects.create(name=randomize_hardware,
                                    description=text.text(quantity=3),
                                    slug=slugify(randomize_hardware + '-' + str(slug_creator())), )

        for _ in range(30):
            randomize_hardware = random.choice([hardware.cpu(), hardware.graphics()])
            category_n = Category.objects.order_by('?').first()
            Product.objects.create(
                category=category_n,
                name=randomize_hardware,
                description=text.text(quantity=3),
                price=round(random.uniform(10.00, 1000.00), 2),
                slug=slugify(randomize_hardware + '-' + str(slug_creator())),
            )

    def test_should_return_all_products_from_all_categories(self):
        client = Client()
        request = client.get('/products/')
        request1 = client.post('/products/')
        request2 = client.get('/poroducts/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request1.status_code, 405)
        self.assertEqual(request2.status_code, 404)

    def test_should_return_all_products_in_category_use_category_slug(self):
        client = Client()
        category = Category.objects.order_by('?').first()
        request = client.get('/products/' + category.slug + '/')
        request1 = client.post('/products/', {'slug': category.slug})
        request2 = client.get('/products/' + category.slug + 'qwerty' + '/')
        request3 = client.get('/producasts/' + category.slug + '/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request1.status_code, 405)
        self.assertEqual(request2.status_code, 404)
        self.assertEqual(request3.status_code, 404)

    def test_should_return_product_detail(self):
        client = Client()
        product = Product.objects.order_by('?').last()
        request = client.get('/products/' + product.category.slug + '/' + product.slug + '/')
        request1 = client.post('/products/' + product.category.slug + '/' + product.slug + '/')
        request2 = client.get('/products/' + product.category.slug + 'qwerty' + '/' + product.slug + '/')
        request3 = client.get('/products/' + product.category.slug + '/' + product.slug + 'qwerty' + '/')
        request4 = client.get('/proertducts/' + product.category.slug + '/' + product.slug + '/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request1.status_code, 405)
        self.assertEqual(request2.status_code, 404)
        self.assertEqual(request3.status_code, 404)
        self.assertEqual(request4.status_code, 404)

    def test_should_return_last_add_item_to_authorized_user(self):
        client = Client()
        client.login(username='admin', password='adminadmin')
        request = client.get('/products/last_added_products/')
        request2 = client.get('/products/last_added_producs/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request2.status_code, 404)
        client.logout()
        request3 = client.get('/products/last_added_products/')
        self.assertEqual(request3.status_code, 401)

