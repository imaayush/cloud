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

    def create(self, validated_data, method):
        transactions_data = validated_data.pop('transactions')
        validated_data['total_quantity'] = 0
        validated_data['total_amount'] = 0

        if method == 'POST':
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
        elif method == 'PUT':
            transaction = []
            validated_data['total_quantity'] = 0
            validated_data['total_amount'] = 0
            invoice = Invoice.objects.get(id=validated_data.get('id'))
            transactions_in_db = Transaction.objects.filter(invoice_id=validated_data.get('id'))
            transactions_in_db=[transaction_id.id for transaction_id in transactions_in_db if transaction_id.id]
            transaction_in_request = [transaction_id.get('id') for transaction_id in transactions_data if transaction_id.get('id')]
            remove_transactions = list(set(transactions_in_db) - set(transaction_in_request))

            for remove_transaction in remove_transactions :
                transaction_to_remove = Transaction.objects.filter(id=remove_transaction)
                transaction_to_remove.delete()

            for transaction_data in transactions_data:

                if transaction_data.get('id'):
                    validated_data['total_quantity'] = validated_data['total_quantity'] + transaction_data.get('quantity')
                    validated_data['total_amount'] = validated_data['total_amount'] + transaction_data.get('price') * transaction_data.get('quantity')
                    transaction_data['line_total'] = transaction_data.get('price')*transaction_data.get('quantity')
                    update_transaction = Transaction.objects.get(id=transaction_data.get('id'))
                    update_transaction.product = transaction_data.get('product')
                    update_transaction.quantity = transaction_data.get('quantity')
                    update_transaction.price = transaction_data.get('price')
                    update_transaction.line_total = transaction_data.get('line_total')
                    transaction.append(update_transaction.save())
                else:
                    validated_data['total_quantity'] = validated_data['total_quantity'] + transaction_data.get('quantity')
                    validated_data['total_amount'] = validated_data['total_amount'] + transaction_data.get('price') * transaction_data.get('quantity')    
                    transaction_data['line_total'] = transaction_data.get('price')*transaction_data.get('quantity')
                    transaction.append(Transaction.objects.create(invoice=invoice, **transaction_data))

            invoice = Invoice.objects.get(id=validated_data.get('id'))
            invoice.customer = validated_data.get('customer')
            invoice.total_quantity = validated_data.get('total_quantity')
            invoice.total_amount = validated_data.get('total_amount')
            invoice = invoice.save()
            return invoice


class TransactionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'product', 'quantity', 'price','line_total' )


class InvoiceGetSerializer(serializers.ModelSerializer):
    transactions = TransactionGetSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('id','customer', 'total_quantity', 'total_amount', 'transactions')