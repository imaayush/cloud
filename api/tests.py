from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Invoice, Transaction


class InvoiceTests(APITestCase):
    def test_create_invoice(self):
        """
        Ensure we can create a new invoice
        """
        url = '/invoices/'
        data = {
            "customer": "aayush",
            "transactions": [
                {
                    "product": "apple",
                    "quantity": 4,
                    "price": 2,

                },
                {

                    "product": "pen",
                    "quantity": 4,
                    "price": 2,

                }
            ]
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        """
        Ensure we can  update a  invoice
        """
        url = '/invoices/1/'
        data = {
            "id": 1,
            "customer": "aayush",
            "transactions": [
                {
                    "product": "apple",
                    "quantity": 4,
                    "price": 2,

                },
                {

                    "product": "pen",
                    "quantity": 4,
                    "price": 2,

                }
            ]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
