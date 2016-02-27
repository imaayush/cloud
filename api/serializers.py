from rest_framework import serializers

from api.models import Invoice, Transaction


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ('id', 'customer', 'date', 'total_quantity', 'total_amount')



class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction 
		fields = {'id', 'product', 'quantity', ' price', 'line_total', 'Invoice_id '}       