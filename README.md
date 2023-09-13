# BeautyBrews Co.
```text
Arini Widya Pramesti
2206830271
PBP E
```


## Tugas 2
>1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Proyek (*Project*) adalah keseluruhan proyek web yang dibangun dengan menggunakan Django. Django itu sendiri adalah sebuah *framework full-stack* untuk membuat aplikasi web dengan bahasa pemrograman Python. 

 - [x] Membuat sebuah proyek Django baru.

 1. Membuat direktori baru dengan nama `beautiful_brews`. Lalu, membuat repositori baru dengan nama 
 `beautiful-brews` dan inisiasi repositori tersebut sebagai repositori Git. Setelah itu, masuk ke dalam
 direktori baru yang sudah dibuat dan buka *command prompt*. 
 2. Membuat virtual environment dengan menjalankan perintah ```python -m venv env```. Virtual 
 environment ini berguna untuk mengisolasi *package* serta *dependencies* dari aplikasi sehingga tidak
 bertabrakan dengan versi lain yang ada pada komputer saya. Virtual environment dapat diaktifkan dengan 
 menjalankan perintah ```env\Scripts\activate.bat```. 
 3. Membuat berkas ```requirements.txt``` dan menambahkan beberapa *dependencies*.
 ```text
 django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Lalu, pasang *dependencies* tersebut dengan perintah ```pip install -r requirements.txt```.

4. Membuat proyek Django dengan nama `beautiful_brews` dengan perintah ```django-admin startproject
beautiful_brews .```

5. Pergi ke berkas ```settings.py``` lalu tambahkan ```*``` pada ```ALLOWED_HOSTS```. Dengan menambahkan
```*```, berarti saya mengizinkan akses dari semua host.

6. Memeriksa apakah Django sudah terinstall dengan perintah ```python manage.py runserver``` lalu
membuka http://localhost:8000/. Apabila laman tersebut menampilkan gambar roket, maka proyek Django
sudah berhasil.

7. Menghentikan server dengan menekan ```CTRL + C``` dan menonaktifkan virtual environment dengan
perintah ```deactivate.```


 - [x]  Membuat aplikasi dengan nama `main` pada proyek tersebut.

1. Membuat aplikasi baru dengan nama `main` dengan perintah `python manage.py startapp main`.
2. Mendaftarkan aplikasi `main` ke dalam proyek dengan membuka berkas `settings.py` dan tambahkan
`'main'` ke dalam variabel `INSTALLED_APPS`.
```text
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```


 - [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.

1. Mengonfigurasi *routing* URL aplikasi `main` dengan cara membuat berkas `urls.py` dan isi berkas
tersebut dengan kode berikut.
```text
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Berkas `urls.py` pada aplikasi `main` bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi `main`.

2. Mengonfigurasi *routing* URL proyek untuk menghubungkannya ke tampilan `main` dengan cara membuka
   berkas`urls.py` di dalam direktori `beautiful_brews`, lalu impor fungsi `include` dari `django.urls`
   dengan kode ```from django.urls import path, include```. Setelah itu, tambahkan rute URL
   seperti berikut untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns` dengan kode
   ```path('main/', include('main.urls')),```. Berkas `urls.py` pada proyek bertanggung jawab untuk 
   mengatur rute URL tingkat proyek.

 - [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    + `name` sebagai nama *item* dengan tipe `CharField`.
    + `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    + `description` sebagai deskripsi *item* dengan tipe `TextField`.

1. Membuka berkas `models.py` pada direktori aplikasi `main`.
2. Mengisi berkas `models.py` dengan kode berikut.
```text
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
3. Membuat migrasi model dengan perintah `python manage.py makemigrations`. Migrasi model adalah cara
 Django melacak perubahan pada model basis data. Lalu, menerapkan migrasi ke dalam basis data lokal 
 dengan perintah `python manage.py migrate`. Perlu diingat bahwa setiap kali melakukan perubahan pada
 model, perlu melakukan migrasi untuk merefleksikan perubahan tersebut.


 - [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

1. Membuka berkas `views.py` di dalam berkas aplikasi `main`.
2. Menambahkan `from django.shortcuts import render` di bagian paling atas berkas.
3. Menambahkan fungsi `show_main`di bawah impor.
```text
def show_main(request):
    context = {
        'name': 'Arini Widya Pramesti',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
```


 - [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

1. Membuka berkas `urls.py` di dalam direktori `beautiful_brews`.
2. Mengimpor fungsi `include` dari `django.urls` dengan kode ```from django.urls import path,include```.
   Setelah itu, tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan `main` di dalam 
   variabel `urlpatterns` dengan kode ```path('main/', include('main.urls')),```.



>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Alt text] (Downloads/image_for_tugas2.png)



>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment dapat digunakan dalam pengembangan aplikasi web, termasuk aplikasi berbasis Django
yang saat ini sedang saya pelajari. Virtual environmnet memungkinkan untuk membuat lingkungan terisolasi
untuk setiap proyek yang dikembangkan. Setiap virtual environment memiliki salinan terisolasi dari
interpreter Python dan pustaka yang diperlukan, yang digunakan untuk menghindari konflik antara pustaka
proyek yang berbeda. Dengan mengisolasi pustaka dan *dependencies* dalam virtual environment, saya dapat
dengan mudah mengelola dan membersihkan proyek yang dikembangkan.



>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola
desain yang berbeda yang digunakan dalam pengembangan perangkat lunak, terutama dalam konteks
pengembangan aplikasi berbasis antarmuka pengguna (UI). 

MVC (Model-View-Controller):
Model: Mewakili data dan aturan bisnis aplikasi.
View: Menampilkan data kepada pengguna dan menerima input dari pengguna.
Controller: Bertindak sebagai perantara antara Model dan View. Controller mengontrol alur aplikasi,
menerima input dari View, memperbarui Model sesuai permintaan, dan memperbarui tampilan saat Model berubah.
Perbedaan:
- MVC adalah pola desain yang terpisah dengan jelas antara Model, View, dan Controller.
- Controller bertanggung jawab untuk mengontrol alur aplikasi dan mengelola interaksi antara Model dan
View.

MVT (Model-View-Template):
Model: Seperti dalam MVC, mewakili data dan aturan bisnis aplikasi.
View: Menampilkan data kepada pengguna dan menerima input dari pengguna.
Template: Merupakan bagian yang paling mirip dengan Controller dalam MVC. Template mengatur tampilan dan
menentukan bagaimana data dari Model akan ditampilkan di View.
Perbedaan:
- MVT adalah varian dari MVC yang sering digunakan dalam framework web seperti Django (Python). Dalam MVT, Template menggantikan peran Controller yang ada dalam MVC.
- Template bertanggung jawab untuk mengatur tampilan dan format data.

MVVM (Model-View-ViewModel):
Model: Mewakili data dan aturan bisnis aplikasi.
View: Menampilkan data kepada pengguna dan menerima input dari pengguna.
ViewModel: Merupakan perantara antara Model dan View. ViewModel bertanggung jawab untuk memformat data
dari Model agar sesuai untuk ditampilkan di View dan mengelola tindakan pengguna. Ini sering digunakan
dalam pengembangan aplikasi berbasis antarmuka pengguna (UI) dengan teknologi seperti WPF (Windows
Presentation Foundation) dan Angular.
Perbedaan:
- MVVM memisahkan secara jelas tugas presentasi (ViewModel) dari tampilan (View) dan data (Model).
- ViewModel tidak hanya mengontrol alur aplikasi, tetapi juga mengelola tampilan data dan tindakan
pengguna.

