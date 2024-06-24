from django.contrib import admin
from django.urls import path, include

#ini untuk menampilkan gambar yang sudah di upload pada media
from django.conf import settings
from django.conf.urls.static import static

from latihan.views import home, about, contact, detail_artikel
from latihan.autentikasi import akun_login, akun_registrasi, akun_logout

from berita.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('artikel/<slug:slug>', detail_artikel, name="detail_artikel"),

    path('dashboard/', include('berita.urls')),

    path('api/author/list', api_author_list),

    path('api/kategori/list', api_kategori_list),
    path('api/kategori/add', api_kategori_add), 
    path('api/kategori/detail/<int:id_kategori>', api_kategori_detail),

    path('api/artikel/list', api_artikel_list),
    path('api/artikel/detail/<int:id_artikel>', api_artikel_detail),

    path('autentikasi/login', akun_login, name="akun_login"),
    path('autentikasi/registrasi', akun_registrasi, name="akun_registrasi"),
    path('autentikasi/logout', akun_logout, name="akun_logout"),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
#ini untuk menampilkan gambar yang sudah di uploasd pada media
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
