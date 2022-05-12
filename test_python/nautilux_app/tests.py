from django.test import TestCase
from .models import Equipment
from django.urls import reverse

class EquipmentListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 40 Equipments for pagination tests
        number_of_equipments = 40

        for equipment_id in range(number_of_equipments):
            Equipment.objects.create(
                name=f'Equipment {equipment_id}',
                slug=f'Equipment_{equipment_id}',
                quantity = 10*equipment_id
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('http://127.0.0.1:8000/nautilux_app/equipments/')
        self.assertEqual(response.status_code, 200)
    
    def test_pagination1(self):
        response = self.client.post('http://127.0.0.1:8000/nautilux_app/equipments/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 30)
    
    def test_pagination2(self):
        response = self.client.post('http://127.0.0.1:8000/nautilux_app/equipments/?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 30)

    def test_pagination3(self):
        response = self.client.post('http://127.0.0.1:8000/nautilux_app/equipments/?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 10)

class EquipmentViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('http://127.0.0.1:8000/nautilux_app/equipment/')
        self.assertEqual(response.status_code, 200)

    def test_equipment_creation(self):
        response = self.client.post('http://127.0.0.1:8000/nautilux_app/equipment/', 
        data= {
        "name": "Equipment 2",
        "slug": "equipment-2",
        "quantity": 555,
        "categories": [
            1,
            2
        ],
        })
        self.assertEqual(response.status_code, 201)

class EquipmentDetailsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 40 Equipments for tests
        number_of_equipments = 1

        for equipment_id in range(number_of_equipments):
            Equipment.objects.create(
                name=f'Equipment {equipment_id}',
                slug=f'Equipment_{equipment_id}',
                quantity = 10*equipment_id
            )

    def test_equipment_get(self):
        response = self.client.get('http://127.0.0.1:8000/nautilux_app/equipment/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_equipment_delete(self):
        response = self.client.delete('http://127.0.0.1:8000/nautilux_app/equipment/1/')
        self.assertEqual(response.status_code, 204)