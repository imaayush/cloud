from rest_framework import serializers

from api.models import Invoice, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('product', 'quantity', 'price')


class InvoiceSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('customer' ,'transactions')

    def create(self, validated_data):
        transactions_data = validated_data.pop('transactions')
        validated_data['total_quantity'] = 0
        validated_data['total_amount'] = 0
        for transaction_data in transactions_data:
            validated_data['total_quantity'] = validated_data[
                'total_quantity'] + transaction_data.get('quantity')
            validated_data['total_amount'] = validated_data[
                'total_amount'] + transaction_data.get('price') * transaction_data.get('quantity')
        invoice = Invoice.objects.create(**validated_data)
        transaction = []

        for transaction_data in transactions_data:
            transaction_data['line_total'] = transaction_data.get('price')*transaction_data.get('quantity')
            transaction.append(Transaction.objects.create(invoice=invoice, **transaction_data))
        return invoice


class TransactionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'product', 'quantity', 'price','line_total' )


class InvoiceGetSerializer(serializers.ModelSerializer):
    transactions = TransactionGetSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('id','customer', 'total_quantity', 'total_quantity', 'total_amount', 'transactions')