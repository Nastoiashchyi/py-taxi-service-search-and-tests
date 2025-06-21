from django.test import TestCase
from taxi.forms import DriverSearchForm, CarSearchForm, ManufacturerSearchForm

class SearchFormTests(TestCase):

    def test_driver_search_form_defaults_to_empty(self):
        f = DriverSearchForm(data={})
        self.assertTrue(f.is_valid())
        self.assertEqual(f.cleaned_data['username'], "")

    def test_driver_search_form_accepts_username(self):
        f = DriverSearchForm(data={'username': 'alice'})
        self.assertTrue(f.is_valid())
        self.assertEqual(f.cleaned_data['username'], 'alice')

    def test_car_search_form_defaults_to_empty(self):
        f = CarSearchForm(data={})
        self.assertTrue(f.is_valid())
        self.assertEqual(f.cleaned_data['model'], "")

    def test_car_search_form_accepts_model(self):
        f = CarSearchForm(data={'model': 'Corolla'})
        self.assertTrue(f.is_valid())
        self.assertEqual(f.cleaned_data['model'], 'Corolla')

    def test_manufacturer_search_form_defaults_to_empty(self):
        f = ManufacturerSearchForm(data={})
        self.assertTrue(f.is_valid())
        self.assertEqual(f.cleaned_data['name'], "")

    def test_manufacturer_search_form_accepts_name(self):
        f = ManufacturerSearchForm(data={'name': 'Toyota'})
        self.assertTrue(f.is_valid())
        self.assertEqual(f.cleaned_data['name'], 'Toyota')
