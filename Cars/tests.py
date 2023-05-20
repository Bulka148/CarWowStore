from django.test import TestCase
from CarWowStore.wsgi import *
from Cars.models import *


class CarsTestCases(TestCase):
    def setUp(self):
        self.firm = Firm(name='test',
                         country='test')

        self.car_p = Car_passport(category='test',
                                  body_type='test',
                                  passport_series='test',
                                  passport_number='test',
                                  weight=1234,
                                  engine_power=1234)

        self.car = Car(model=self.firm,
                       price=1234,
                       city='test')

        self.car_shop = Car_shop(address='test',
                                 firm=self.firm)

        self.sale = Sale(buyer=User(username='test', email='test@test.test', password='test'),
                         car=self.car)

    def test_str_Firm(self):
        str_firm = self.firm.name
        self.assertEquals(str(self.firm), str_firm)

    def test_str_Car_passport(self):
        str_car_p = self.car_p.passport_series + ' ' + self.car_p.passport_number + ' - ' + self.car_p.body_type
        self.assertEquals(str(self.car_p), str_car_p)

    def test_str_Car(self):
        str_car = self.car.model.name + ' ' + str(self.car.price) + 'руб'
        self.assertEquals(str(self.car), str_car)

    def test_str_Sale(self):
        str_sale = self.sale.buyer.username + ' ' + self.sale.car.model.name
        self.assertEquals(str(self.sale), str_sale)

    def test_str_Car_shop(self):
        str_car_shop = self.car_shop.firm.name + ' ' + self.car_shop.address
        self.assertEquals(str(self.car_shop), str_car_shop)
