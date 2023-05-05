from django.shortcuts import render
from . models import jadwal
from . serializers import jadwalSerializer

#rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def readjadwal (request):
 	jadwalimsyak = jadwal.objects.all()
 	serializer = jadwalSerializer(jadwalimsyak, many=True)
 	return Response(serializer.data)
@api_view(['GET'])
def detailjadwal (request, id):
 	jadwalimsyak = jadwal.objects.get(pk=id)
 	serializer = jadwalSerializer(jadwalimsyak, many=False)
 	return Response(serializer.data)
@api_view(['POST'])
def createjadwal (request):
	jadwalimsyak = jadwal.objects.all()
	serializer = jadwalSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response (serializer.data)
@api_view(['PUT'])
def updatejadwal (request, id):
	jadwalimsyak = jadwal.objects.get(pk=id)
	serializer = jadwalSerializer(instance=jadwalimsyak, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response (serializer.data)
@api_view(['DELETE'])
def deletejadwal(request, id):
	jadwalimsyak = jadwal.objects.get(pk=id)
	jadwalimsyak.delete()
	return Response('data di hapus',status=204)

# Create your views here.
