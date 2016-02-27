from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Invoice, Transaction
from api.serializers import InvoiceSerializer

@api_view(["GET" ,'POST'])
def invoice_list(request):
    """
        list of all invoice  or create new invoice
        """
       
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        #import pdb;pdb.set_trace() 
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return    Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return     Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def invoice_detail(request, pk):
    """ select inovice by  id 
        """
    if request.method == 'GET':
        pass