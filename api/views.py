from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Invoice, Transaction
from api.serializers import (InvoiceSerializer,
                             TransactionSerializer,
                             TransactionGetSerializer,
                             InvoiceGetSerializer
                             )


@api_view(["GET", 'POST'])
def invoice_list(request):
    """
        list of all invoice  or create new invoice
        """

    if request.method == 'GET':
        invoices = Invoice.objects.all()

        for invoice in invoices:
            transactions = Transaction.objects.filter(invoice_id=invoice.id)
            invoice.transactions = transactions

        serializer = InvoiceGetSerializer(invoices, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            save = InvoiceSerializer(data=data)
            save.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def invoice_detail(request, pk):
    """ select inovice by  id 
        """
    if request.method == 'GET':
        invoice = Invoice.objects.filter(id=pk)
        #import pdb;pdb.set_trace()
        transactions = Transaction.objects.filter(invoice_id=pk)
        if invoice:
            invoice[0].transactions = transactions
        else:
            return Response({'error':'no data found'}, status=status.HTTP_201_CREATED)
        serializer = InvoiceGetSerializer(invoice, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif  request.method == 'DELETE':
        transactions = Transaction.objects.filter(invoice_id=pk)
        transactions.delete()
        invoice = Invoice.objects.filter(id=pk)
        invoice.delete()
        return Response({'deleted':'success'}, status=status.HTTP_201_CREATED)

