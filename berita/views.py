from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from berita.models import Kategori, Artikel
from berita.forms import ArtikelForm

# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    template_name = "dashboard/index.html"
    context = {
        'title' : 'Halaman Dashboard'
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/autentikasi/logout')
def kategori_list(request):
    template_name = "dashboard/snippets/kategori_list.html"
    kategori = Kategori.objects.all()
    print(kategori)
    context = {
        'title' : 'Halaman Kategori',
        'kategori' : kategori
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/autentikasi/logout')
def kategori_add(request):
    template_name = "dashboard/snippets/kategori_add.html"
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        Kategori.objects.create(
                nama = nama_input
            )
        return redirect(kategori_list) 
    context = {
        'title' : 'Tambah Kategori',
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/autentikasi/logout')
def kategori_update(request, id_kategori):
    template_name = "dashboard/snippets/kategori_update.html"
    try:
        kategori = Kategori.objects.get(id=id_kategori)
    except:
        return redirect(kategori_list)
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        kategori.nama = nama_input
        kategori.save()
        return redirect(kategori_list) 
    context = {
        'title' : 'Update Kategori',
        'kategori' : kategori
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/autentikasi/logout')
def kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
    except:
        pass
    return redirect(kategori_list)

@login_required
def artikel_list(request):
    template_name = "dashboard/snippets/artikel_list.html"
    if request.user.groups.filter(name='Operator'):
        artikel = Artikel.objects.all()
    else:
        artikel = Artikel.objects.filter(author=request.user)
    context = {
        'title' : 'Daftar Artikel',
        'artikel' : artikel
    }
    return render(request, template_name, context)

@login_required
def artikel_add(request):
    template_name = "dashboard/snippets/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
        else:
            print(forms.error_class)
    forms = ArtikelForm()
    context = {
        'title' : 'Tambah Artikel',
        'forms' : forms
    }
    return render(request, template_name, context)

@login_required
def artikel_detail(request, id_artikel):
    template_name = "dashboard/snippets/artikel_detail.html"
    artikel = Artikel.objects.get(id=id_artikel)
    context = {
        'title' : artikel.judul,
        'artikel' : artikel
    }
    return render(request, template_name, context)

@login_required
def artikel_update(request, id_artikel):
    template_name = "dashboard/snippets/artikel_forms.html"
    artikel = Artikel.objects.get(id=id_artikel)

    if request.user.groups.filter(name='Operator'):
        pass
    else:
        if artikel.author == request.user:
            return redirect('/')

    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)

    forms = ArtikelForm(instance=artikel)
    context = {
        'title' : 'Tambah Artikel',
        'forms' : forms
    }
    return render(request, template_name, context)

@login_required
def artikel_delete(request, id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
    
        if request.user.groups.filter(name='Operator'):
            pass
        else:
            if artikel.author == request.user:
                return redirect('/')
        artikel.delete()
    except:pass
    return redirect(artikel_list)