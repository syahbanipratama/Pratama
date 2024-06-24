from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from berita.serializers import BiodataSerializer, KategoriSerializer, ArtikelSerializers
from berita.models import Kategori, Artikel
from pengguna.models import Biodata

@api_view(['GET'])
def api_author_list(request):
    biodata = Biodata.objects.all()
    serializer = BiodataSerializer(biodata, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_kategori_list(request):
    kategori = Kategori.objects.all()
    serializer = KategoriSerializer(kategori, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_kategori_detail(request, id_kategori):
    try:
        kategori = Kategori.objects.get(id=id_kategori)
        serializer = KategoriSerializer(kategori, many=False)
        return Response(serializer.data)
    except:
        return Response({'message:data kategori tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def api_kategori_add(request):
    serializer = KategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def api_artikel_list(request):
    artikel = Artikel.objects.all()
    serializer = ArtikelSerializers(artikel, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_artikel_detail(request, id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
        serializer = ArtikelSerializers(artikel, many=False)
        return Response(serializer.data)
    except:
        return Response({'message:data artikel tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)