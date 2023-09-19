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
 2. Membuat *virtual environment* dengan menjalankan perintah ```python -m venv env```. Virtual 
 environment ini berguna untuk mengisolasi *package* serta *dependencies* dari aplikasi sehingga tidak
 bertabrakan dengan versi lain yang ada pada komputer saya. *Virtual environment* dapat diaktifkan dengan 
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

7. Menghentikan server dengan menekan ```CTRL + C``` dan menonaktifkan *virtual environment* dengan
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

![image_for_tugas2](https://github.com/widyaprms/beautiful-brews/assets/124958742/22b60bb6-3732-41be-b59a-10cf2dadfee5)



>3. Jelaskan mengapa kita menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?

*Virtual environment* dapat digunakan dalam pengembangan aplikasi web, termasuk aplikasi berbasis Django
yang saat ini sedang saya pelajari. *Virtual environmnet* memungkinkan untuk membuat lingkungan
terisolasi untuk setiap proyek yang dikembangkan. Setiap *virtual environment* memiliki salinan 
terisolasi dari interpreter Python dan pustaka yang diperlukan, yang digunakan untuk menghindari konflik 
antara pustaka proyek yang berbeda. Dengan mengisolasi pustaka dan *dependencies* dalam *virtual 
environment*, saya dapat dengan mudah mengelola dan membersihkan proyek yang dikembangkan.



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



---
## Tugas 3
>1. Apa perbedaan antara form POST dan form GET dalam Django?

Pada dasarnya, POST dan GET adalah dua metode pengiriman data dalam HTTP *request* yang digunakan untuk mengirimkan data dari *client* 
(pengguna) ke server. Namun, kedua metode ini memiliki perbedaan cara pengiriman data yang cukup signifikan.

Metode POST mengirimkan data dalam bentuk *request body*. *Request body* adalah bagian dalam HTTP *request* yang berisi data yang ingin
dikirimkan oleh pengguna ke server. Ketika pengguna mengirimkan data melalui metode POST, data tersebut tidak terlihat atau tersimpan
pada URL. Sehingga dari segi keamanan, data yang dikirimkan dengan metode POST lebih terjaga.

Sedangkan, metode GET mengirimkan data dalam bentuk *query parameters* yang terdapat pada URL *request*. *Query parameters* ini terdiri
dari pasangan *key-value* atau nama dan nilai data yang diinginkan. Berbeda dengan POST, data pada GET akan terlihat secara jelas pada
URL dan terbuka untuk siapa saja yang memiliki akses ke URL tersebut. Sehingga dari segi keamanan, data yang dikirimkan dengan metode
GET tidak terjaga.


>2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

XML adalah bahasa markup yang digunakan untuk mendefinisikan data dengan struktur hierarki. Ini berarti, kita dapat membuat dokumen
yang memungkinkan kita untuk mewakili data dengan tingkat kompleksitas yang tinggi. XML sering digunakan untuk pertukaran data antara
aplikasi, penyimpanan data, konfigurasi, dan dalam protokol seperti SOAP dalam layanan web. XML menggunakan tag yang didefinisikan oleh
pengguna untuk mendefinisikan data dan atribut dalam elemen. Ini fleksibel tetapi dapat menyebabkan dokumen yang lebih besar dan
kompleks. Parsing XML memerlukan lebih banyak kerja karena kita harus membaca tag dan hierarki.

JSON adalah format data yang ringkas dan ringan yang menggunakan struktur objek. Data disajikan dalam bentuk pasangan key-value. JSON
sangat populer dalam pengembangan web dan layanan web RESTful. Ini juga digunakan untuk penyimpanan konfigurasi dan pertukaran data
antara klien dan server dalam aplikasi web modern. JSON memiliki sintaks yang sederhana dan mudah dipahami. Ini lebih efisien dalam hal
ukuran file dan lebih mudah diuraikan oleh mesin dan manusia. Ini sangat cocok untuk pertukaran data di antara komponen-komponen
aplikasi dan penggunaan di seluruh internet.

Sedangkan, HTML adalah bahasa markup yang digunakan untuk membuat struktur dan tampilan halaman web. Ini tidak dirancang untuk
pertukaran data struktural, tetapi untuk representasi konten yang ditampilkan dalam browser web. HTML digunakan untuk membuat tampilan
halaman web yang dapat diakses oleh pengguna melalui browser web. Ini mengandung tag-tag yang mendefinisikan elemen-elemen seperti
teks, gambar, tautan, tabel, dan formulir. HTML memiliki sintaks yang ketat dan spesifik untuk membuat tampilan halaman web. Ini bukan
format data, tetapi bahasa yang digunakan untuk menggambarkan cara tampilan halaman web seharusnya. Data yang ditampilkan dalam halaman
HTML biasanya disediakan oleh server dan tidak disimpan dalam format HTML itu sendiri.


>3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON atau JavaScript Object Notation, sangat sering digunakan untuk memfasilitasi komunikasi di antara aplikasi web kontemporer karena
sifatnya yang ramah pengguna, efisien, dan mudah beradaptasi. JSON menggunakan struktur yang tidak rumit seperti objek dan array,
sehingga pemahaman data menjadi lebih cepat. Tidak hanya itu, keunggulan dari JSON meluas ke kompatibilitas dengan berbagai bahasa
pemrograman, sehingga memungkinkan komunikasi antar aplikasi yang mulus. JSON juga mudah diurai oleh komputer, bahkan di berbagai
pustaka yang berbeda.

Selain itu, JSON memiliki keunggulan dalam efisiensi transmisi data di seluruh jaringan. JSON merender data dalam format yang ringan,
sehingga mengurangi waktu dan sumber daya yang diperlukan untuk transfer. Fleksibilitasnya yang melekat terbukti sangat berharga untuk
merepresentasikan berbagai tipe data dengan mudah. Selain itu, JSON juga digunakan sebagai pilihan yang aman untuk pertukaran data web,
menghindari risiko keamanan yang terkait dengan beberapa format lain. Akibatnya, banyak aplikasi web modern memilih JSON sebagai media
komunikasi utama mereka.


>4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

  - [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.

  1. Membuat berkas baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur *form* yang dapat menerima data produk
baru. Tambahkan kode berikut.
```text
from django.forms import ModelForm
from main.models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```
2. Menambahkan beberapa import pada berkas `views.py` yang ada pada folder `main`.
```text
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
```
3. Membuat fungsi baru yang bernama `create_item` pada berkas `views.py`. Tambahkan potongan kode berikut untuk menghasilkan formulir
yang dapat menambahkan data produk secara otomatis ketika data di-*submit* dari *form*.
```text
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
4. Mengubah fungsi `show_main` yang sudah ada pada berkas `views.py` menjadi sebagai berikut.
```text
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Arini Widya Pramesti', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'items': items
    }

    return render(request, "main.html", context)
```
5. Membuka berkas `urls.py` pada folder `main` dan *import* fungsi `create_item` dengan menambahkan 
`from main.views import show_main, create_item`.
6. Menambahkan *path url* ke dalam `urlpatterns` pada `urls.py` di `main` dengan menambahkan
`path('create-item', create_item, name='create_item'),` untuk mengakses fungsi yang sudah di*import*.
7. Membuat berkas HTML yang baru dengan nama `create_item.html` pada direktori `main/templates` dan isilah berkas tersebut dengan kode
berikut.
```text
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
8. Membuka `main.html` dan menambahkan kode berikut untuk menampilkan data item dalam bentuk *table* dan tombol "Add New Item" yang
akan *redirect* ke halaman *form*.
```text
...
 <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data item di bawah baris ini {% endcomment %}
    
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
    
    {% endblock content %}
```
 

  - [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by ID*, dan 
  JSON *by ID*.
  
  1. Menambahkan import berikut ke berkas `views.py` pada folder `main`.
  ```text
  from django.http import HttpResponse
  from django.core import serializers
  ```
  2. Menambahkan fungsi yang menerima parameter *request* dengan nama `show_xml` dan `show_json`. Lalu, menambahkan *return function* dalam bentuk `HttpResponse`.
  ```text
  def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

  def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```
  3. Menambahkan fungsi yang menerima parameter *request* dan id dengan nama `show_xml_by_id` dan `show_json_by_id` untuk mengembalikan
  data produk berdasarkan id.
  ```text
  def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

  def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```


  - [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.

  1. Membuka berkas `urls.py` pada folder `main` lalu menambahkan import beberapa fungsi yang sudah dibuat.
  `from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id `
  2. Menambahkan *path url* ke dalam `urlpatterns` yang ada pada berkas `urls.py`.
  ```text
  ...
  path('xml/', show_xml, name='show_xml'), 
  path('json/', show_json, name='show_json'), 
  path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
  path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
  ...
  ```


  - [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat *screenshot* dari hasil akses URL pada Postman, dan
menambahkannya ke dalam `README.md`.
- HTML
  ![html](https://github.com/widyaprms/beautiful-brews/assets/124958742/310216ca-93d4-406b-9ae4-a2eeaae83a9d)
- XML
  ![Screenshot (6)](https://github.com/widyaprms/beautiful-brews/assets/124958742/ff556b1a-9204-461d-bb08-a8e2c16d298b)
- JSON
  ![Screenshot (5)](https://github.com/widyaprms/beautiful-brews/assets/124958742/3d3e3630-e9a5-4b3c-a1df-2fbeaa8ec012)
- XML BY ID
  ![xml by id](https://github.com/widyaprms/beautiful-brews/assets/124958742/3fb7420f-6865-4664-8945-33c89bcf3cc8)
- JSON BY ID
![json by id](https://github.com/widyaprms/beautiful-brews/assets/124958742/baf0e622-b98b-40e2-8c5a-29ca1b59d53b)
