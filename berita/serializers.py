from rest_framework import serializers 
from django.contrib.auth.models import User
from berita.models import Kategori, Artikel
from pengguna.models import Biodata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class BiodataSerializer(serializers.ModelSerializer):
     user = UserSerializer()
     class Meta:
        model = Biodata
        fields = ['user', 'alamat', 'telpon', 'foto']

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama']

class ArtikelSerializers(serializers.ModelSerializer):
    author = UserSerializer()
    kategori = KategoriSerializer()
    class Meta:
        model = Artikel
        fields = ['id', 'judul', 'isi', 'kategori', 'author', 'thumbnail', 'created_at', 'slug']