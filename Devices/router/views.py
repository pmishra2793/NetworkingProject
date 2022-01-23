from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from router.models import RouterDetails
from router.serializers import RouterDetailsSerializer
# Create your views here.

@api_view(['GET'])
def get_router_details(request):
    ip_start = request.GET.get('ip_start')
    ip_end = request.GET.get('ip_end')
    router_details_obj = RouterDetails.objects.all()
    if ip_start and ip_end:
        router_details_obj = RouterDetails.objects.filter(loopback__gt = ip_start, loopback__lt = ip_end)
    serializer = RouterDetailsSerializer(router_details_obj, many=True)
    return Response({"status": 200, 'payload': serializer.data})

@api_view(['POST'])
def add_router_details(request):
    serializer = RouterDetailsSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({'status':403, 'error': serializer.errors, 'message': 'something went wrong'})
    serializer.save()
    return Response({'status':200, 'payload': serializer.data, 'message': 'sent data'})

@api_view(['PATCH'])
def update_router_details(request, loopback):
    try:
        loopback_obj = RouterDetails.objects.get(loopback = loopback)
        serializer = RouterDetailsSerializer(loopback_obj, data = request.data, partial = True)
        if not serializer.is_valid():
            return Response({'status':403, 'error': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status':200, 'payload': serializer.data, 'message': 'sent data'})
    except:
        return Response({'status':403, 'message' : 'invalid loopback'})


@api_view(['DELETE'])
def delete_router_details(request):
    try:
        id = request.GET.get('id')
        router_details_obj = RouterDetails.objects.get(id = id)
        router_details_obj.delete()
        return Response({'status':200, 'message': 'data deleted'})
    except:
        return Response({'status':403, 'message' : 'invalid id'})

