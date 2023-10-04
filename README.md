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



---
## Tugas 4
>1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

Django `UserCreationForm` adalah salah satu form yang disediakan oleh Django, sebuah *framework* pengembangan web
yang populer untuk Python. Form ini digunakan untuk membuat form registrasi pengguna (*user registration form*) dalam aplikasi
web yang menggunakan Django. Form ini memungkinkan pengguna untuk mendaftar ke sebuah website dengan mengisi informasi seperti nama
pengguna (*username*), kata sandi (*password*), dan data tambahan lainnya yang mungkin diperlukan oleh aplikasi.
* Kelebihan:
    * Pengembangan Yang Cepat - Hal ini dapat menyederhanakan proses pembuatan form registrasi pengguna, menghemat waktu, dan tenaga
    untuk membangunnya dari awal.
    * Integrasi dengan Autentikasi Django - `UserCreationForm` terintegrasi dengan sistem autentikasi bawaan Django dengan lancar,
    menangani pembuatan pengguna, enkripsi kata sandi, dan validasi secara otomatis.
* Kekurangan:
    * Penyesuaian Terbatas - Meskipun dapat disesuaikan, untuk form registrasi pengguna yang kompleks dengan persyaratan unik, pengguna
    mungkin merasa terbatas dan perlu membuat form khusus dari awal.
    * Ketergantungan pada Django - Jika kita memutuskan untuk menggunakan *framework* web yang berbeda atau berpindah dari Django, kita
    mungkin perlu menulis ulang form registrasi pengguna akibat ketergantungan `UserCreationForm` pada Django.

>2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi adalah proses verifikasi identitas pengguna. Autentikasi berarti memeriksa apakah pengguna yang mencoba mengakses aplikasi
web adalah pengguna yang yang sesungguhnya. Dalam Django, autentikasi sering melibatkan verifikasi nama pengguna (*username*) dan kata
sandi (*password*). Pengguna harus memberikan kombinasi yang benar dari kedua informasi ini untuk dianggap berhasil diotentikasi. Django
memiliki sistem autentikasi bawaan yang mengelola autentikasi pengguna dengan menggunakan *default user model* atau *user model* yang
sudah disesuaikan. Ini juga menyediakan berbagai metode otentikasi tambahan seperti otentikasi berbasis token atau OAuth.

Sedangkan, otorisasi adalah proses yang memutuskan apa yang diizinkan atau tidak diizinkan oleh pengguna setelah pengguna
diautentikasi. Otorisasi berkaitan dengan hak akses dan perizinan. Dalam Django, otorisasi berhubungan dengan aturan yang mengatur siapa yang memiliki akses ke bagian tertentu dari aplikasi web dan apa yang dapat mereka lakukan setelah diotentikasi. Ini dilakukan dengan menggunakan peran (*roles*) dan izin (*permissions*). Django memiliki sistem otorisasi bawaan yang memungkinkan pengembang untuk
mendefinisikan peran (seperti "admin" atau "pengguna biasa") dan mengaitkan izin dengan peran tersebut. Ini memungkinkan pengembang
untuk mengontrol akses ke *views*, objek, atau fitur tertentu berdasarkan peran dan izin pengguna.

Autentikasi dan otorisasi penting karena autentikasi membantu memastikan bahwa hanya pengguna yang diautentikasi yang dapat mengakses
sumber daya tertentu dalam aplikasi dan otorisasi memastikan bahwa pengguna hanya memiliki akses ke sumber daya yang mereka izinkan
berdasarkan peran dan izin mereka. Autentikasi dan otorisasi juga memungkinkan aplikasi untuk menjaga privasi data pengguna dan
memastikan bahwa pengguna hanya dapat mengakses atau mengubah data yang seharusnya mereka akses atau ubah.


>3. Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan *cookies* untuk mengelola data sesi pengguna?

*Cookies* adalah file teks kecil yang disimpan di komputer atau perangkat pengguna saat mereka mengunjungi sebuah situs web. *Cookies*
digunakan dalam konteks aplikasi web untuk menyimpan informasi yang dapat digunakan secara berkelanjutan selama sesi pengguna atau
bahkan dalam beberapa kunjungan pengguna ke situs web yang sama. Dalam Django, *cookies* digunakan untuk mengelola data sesi pengguna
dan mengimplementasikan serta mengelola sesi pengguna. Sesuai dengan paradigma *stateless* HTTP, *cookies* membantu menyimpan data
pengguna antar permintaan web sehingga aplikasi dapat mengenali pengguna yang berbeda dan menjaga konteks atau keadaan selama sesi
mereka di situs web.

Berikut adalah cara Django menggunakan cookies untuk mengelola data sesi pengguna:
- Mengidentifikasi Pengguna - Setelah pengguna *login*, Django dapat menggunakan *cookies* untuk menyimpan ID sesi pengguna atau
informasi lain yang mengidentifikasi pengguna tersebut. Informasi ini kemudian digunakan untuk mengenali pengguna di permintaan
selanjutnya.
- Penyimpanan Data Sesi - Django dapat menggunakan *cookies* untuk menyimpan data sesi pengguna seperti preferensi, *shopping list*,
atau informasi lainnya yang harus diingat antar permintaan web. Data ini dapat digunakan untuk memberikan pengalaman yang lebih
personal dan nyaman kepada pengguna.
- Keamanan *Cookies* - Django memiliki dukungan keamanan yang kuat untuk *cookies*, yaitu termasuk opsi untuk mengenkripsi dan
menandatangani *cookies*. Hal ini yang menjaga integritas dan kerahasiaan data yang disimpan di dalamnya dan mencegah pengguna dari
memodifikasi cookies dengan data yang tidak sah.
- Pengaturan *Cookies* - Dalam pengaturan proyek Django, kita dapat mengkonfigurasi berbagai aspek terkait *cookies*, termasuk nama
*cookie*, lama waktu penyimpanan, domain yang dapat mengakses *cookie*, dan lain-lain. Hal ini memberikan fleksibilitas dalam mengelola
*cookies* sesuai dengan kebutuhan aplikasi kita.
- Menghapus *Cookies* - Django juga memberikan cara untuk menghapus *cookies* sesi pengguna saat sesi mereka berakhir, biasanya setelah
pengguna keluar atau sesi mereka berakhir.


>4. Apakah penggunaan *cookies* aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan *cookies* dalam pengembangan web dapat aman jika diimplementasikan dengan baik dan memperhatikan praktik-praktik keamanan
yang tepat. Namun, ada beberapa risiko potensial yang harus diwaspadai ketika menggunakan *cookies*:
- *Cookie Tampering* - Pengguna jahat dapat mencoba memanipulasi atau mencuri *cookies* dari pengguna lain. Misalnya, jika *cookies*
mengandung data sesi atau token otentikasi, pencuri *cookies* dapat mencoba menggunakan informasi tersebut untuk mengakses akun
pengguna tanpa izin.
- Penyerangan Terhadap *Cookies* - Serangan terhadap *cookies* biasanya ada dua jenis, yaitu *cross-site scripting* (XSS) dan
*cross-site request forgery* (CSRF). XSS dapat digunakan untuk mencuri *cookies* dari pengguna. Jika aplikasi web tidak memvalidasi
atau menghindari input pengguna dengan benar, penyerang dapat menyisipkan *script* jahat yang mencuri *cookies* pengguna saat
dijalankan oleh pengguna yang lain. Sedangkan, CSRF menargetkan *cookies* yang digunakan untuk mengotentikasi pengguna. Penyerang dapat
memaksa pengguna yang sudah login untuk melakukan tindakan tanpa izin pada situs web tertentu.
- *Cookie Clutter* - Terlalu banyak *cookies* dapat mempengaruhi kinerja aplikasi web dan pengalaman pengguna. Memantau dan mengelola 
*cookies* yang digunakan oleh aplikasi kita merupakan hal yang penting untuk dilakukan supaya kinerja aplikasi web kita tidak menurun.


>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan
lancar.

- Membuat Fungsi Registrasi
1. Membuka berkas `views.py` pada subdirektori `main` dan menambahkan *import*.
text
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
2. Menambahkan potongan kode di bawah ini pada fungsi `register` yang sudah dibuat.
```text
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
3. Membuat berkas HTML baru dengan nama `register.html` pada folder `main/templates` dan mengisi dengan kode di bawah.
```text
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
4. Membuka berkas `urls.py` pada subdirektori `main` dan *import* fungsi `from main.views import register` serta tambahkan *path url* 
`path('register/', register, name='register'),` ke dalam `urlpatterns`.

- Membuat Fungsi *Login*
1. Membuka berkas `views.py` pada subdirektori `main` dan menambahkan *import* `from django.contrib.auth import authenticate, login`.
2. Menambahkan potongan kode di bawah ini pada fungsi `login` yang sudah dibuat.
```text
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
3. Membuat berkas HTML baru dengan nama `login.html` pada folder `main/templates` dan mengisi dengan kode di bawah.
text
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
4. Membuka berkas `urls.py` pada subdirektori `main` dan *import* fungsi `from main.views import login_user` serta tambahkan *path url*
`path('login/', login_user, name='login'),` ke dalam `urlpatterns`.

- Membuat Fungsi *Logout*
1. Membuka berkas `views.py` pada subdirektori `main` dan menambahkan *import* `from django.contrib.auth import logout`.
2. Menambahkan potongan kode di bawah ini pada fungsi `logout` yang sudah dibuat.
```text
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
3. Membuka berkas `main.html` pada folder `main/templates` lalu menambahkan potongan kode di bawah ini setelah *hyperlink tag* untuk
*Add New Item*.
```text
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
4. Membuka berkas `urls.py` pada subdirektori `main` dan *import* fungsi `from main.views import logout_user` serta tambahkan 
*path url* `path('logout/', logout_user, name='logout'),` ke dalam `urlpatterns`.


- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya
 untuk setiap akun di lokal.
Contoh Akun Pengguna :
- Akun 1
![Screenshot (9)](https://github.com/widyaprms/beautiful-brews/assets/124958742/1664a4f0-2732-4959-ad2a-c8fbd914ebd1)

- Akun 2
![Screenshot (10)](https://github.com/widyaprms/beautiful-brews/assets/124958742/78a60277-0e80-421d-852a-8bf94f878359)


- [x] Menghubungkan model `Item` dengan `User`.

1. Membuka berkas `models.py` pada subdirektori `main` dan tambahkan kode `from django.contrib.auth.models import User` untuk *import*
model.
2. Menambahkan potongan kode di bawah ini pada model `Item` yang sudah dibuat.
```text
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
3. Membuka berkas `views.py` pada subdirektori `main` dan ubah potongan kode pada fungsi `create_item`.
```text
def create_item(request):
 form = ItemForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))
```
4. Mengubah fungsi `show_main`.
```text
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
    }
...
```
5. Menyimpan semua perubahan dan melakukan migrasi dengan menjalankan perintah `python manage.py makemigrations` lalu 
`python manage.py migrate`.


- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada
 halaman utama aplikasi.
 
 1. Membuka `views.py` pada subdirektori `main` dan tambahkan *import*.
 ```text
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
2. Menambahkan fungsi untuk menambahkan *cookies* yang bernama `last_login` pada fungsi `login_user`.
```text
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
3. Menambahkan potongan kode `last_login` pada fungsi `show_main`.
```text
context = {
    'name': 'Arini Widya Pramesti',
    'class': 'PBP E',
    'products': products,
    'last_login': request.COOKIES['last_login'],
}
```
4. Membuka berkas `main.html` dan tambahkan potongan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>` untuk menampilkan data
*last login*.


---
## Tugas 5
>1. Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya.

- *Element Selector*
*Element Selector* memungkinkan kita mengubah properti untuk semua elemen yang memiliki tag HTML yang sama.
Contoh penggunaan *Element Selector*:
```text
<body>
  <div>
    <h1>Halo nama saya A</h1>
    <h2>Halo kalau saya B</h2>
  </div>
  ...
</body>
```
- ID *Selector*
ID *selector* menggunakan ID pada tag sebagai selector-nya. ID bersifat unik dalam satu halaman web. ID dapat ditambahkan pada halaman
template HTML.
Contoh penggunaan ID *Selector* pada *template* HTML:
```text
<body>
  <div id="header">
    <h1>Halo nama saya A</h1>
  </div>
  ...
</body>
```
- *Class Selector*
*Class Selector* memungkinkan kita untuk mengelompokkan elemen dengan karakteristik yang sama.
Contoh penggunaan *Class Selector* pada *template* HTML:
```text
...
<div id="main">
    <div class="content_section">
        <p class="date">published: 3 Oktober 2023</p>
        <h2><a href="">Tugas 5 ku</a></h2>
        <p id="content_1">Tugas sudah selesai</p>
    </div>
    <div class="content_section">
        <p class="date ">published: 4 Oktober 2023</p>
        <h2><a href="">Tugas 5 mu</a></h2>
        <p id="content_2">Tugas dalam proses pengerjaan</p>
    </div>
    <div class="content_section">
        <p>published: 5 Oktober 2023</p>
        <h2><a href="">Tugas 5 semua</a></h2>
        <p id="content_3">Tugas belum dikerjakan</p>
    </div>
</div>
...
```



 >2. Jelaskan HTML5 Tag yang kamu ketahui.

HTML5 adalah versi terbaru dari bahasa markup HTML (*Hypertext Markup Language*) yang digunakan untuk membangun dan merancang halaman
web. Beberapa HTML5 Tag yang saya ketahui, yaitu:

- `<header>`: Tag ini digunakan untuk mendefinisikan *header* dari sebuah halaman web atau bagian dari sebuah elemen konten.
- `<nav>`: Tag ini digunakan untuk mendefinisikan bagian navigasi dari sebuah halaman web, seperti menu utama atau menu samping.
- `<section>`: Tag ini digunakan untuk mengelompokkan konten yang memiliki tema atau topik tertentu dalam halaman web.
- `<footer>`: tag ini digunakan untuk mendefinisikan *footer* dari sebuah halaman web atau bagian dari sebuah elemen konten.
- `<main>`: Tag ini digunakan untuk menandai konten utama dari sebuah halaman web, dan biasanya hanya boleh ada satu elemen `<main>`
dalam satu halaman.
- `<form>`: Tag ini digunakan untuk membuat formulir yang memungkinkan pengguna untuk mengirimkan data ke server web.
- `<input>`: Tag ini digunakan dalam formulir untuk membuat berbagai jenis input, seperti teks, *password*, *check button*, 
*radio button*, dan lain-lain.
- `<a>`: Tag ini digunakan untuk membuat *link* ke halaman web lain atau ke berkas lain di dalam situs web yang sama.
- `<ul>`, `<ol>`, dan `<li>`: Tag ini digunakan untuk membuat *unordered list*, *ordered list*, dan *item* daftar dalam HTML.
- `<div>`: Tag ini digunakan untuk mengelompokkan elemen-elemen HTML ke dalam sebuah blok kontainer yang dapat diatur tampilannya
dengan CSS.
- `<span>`: Tag ini digunakan untuk mengelompokkan elemen-elemen dalam baris teks dan memungkinkan kita untuk mengaplikasikan *style*
atau pemrosesan khusus pada teks tersebut.


 >3. Jelaskan perbedaan antara *margin* dan *padding*.

*Margin* adalah bagian ruang di luar batas elemen dalam halaman web atau dalam tata letak elemen HTML. Dalam CSS, *margin* digunakan
untuk mengatur jarak antara elemen tersebut dan elemen-elemen lain di sekitarnya. Kita dapat mengatur *margin* atas, bawah, kiri, dan
kanan dari suatu elemen secara independen. *Margin* juga menciptakan ruang kosong di sekitar elemen, yang berfungsi sebagai isolator
untuk elemen tersebut. Hal ini dapat memastikan bahwa elemen tidak terlalu berdekatan dengan elemen lain, sehingga meningkatkan
estetika halaman web. Selain itu, apabila dua elemen bertabrakan atau saling tumpang tindih, *margin* dapat digunakan untuk mengatasi
konflik tersebut dengan memberikan ruang ekstra di antara mereka.

Sedangkan, *padding* adalah bagian dari tata letak elemen HTML yang berada di antara batas elemen tersebut dan kontennya sendiri. Dalam
CSS, *padding* digunakan untuk mengatur jarak antara konten dalam elemen dan batas elemen yang memungkinkan kita untuk mengontrol
seberapa jauh konten berada dari tepi elemen. *Padding* juga membantu mengisolasi konten elemen dari elemen-elemen lain di sekitarnya,
sehingga kita dapat memastikan bahwa konten elemen tidak terlalu dekat atau tumpang tindih dengan elemen lain. Selain itu, *padding*
dapat memengaruhi ukuran total elemen, sebagai contoh apabila kita memiliki elemen dengan *padding* yang cukup besar, ukuran elemen
tersebut akan lebih besar daripada kontennya.



 >4. Jelaskan perbedaan antara *framework* CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

| Tailwind CSS                             | Bootstrap                                 |
|-----------------------------------------|-------------------------------------------|
| Membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya. | Menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung. |
| Memiliki file CSS yang lebih kecil sedikit dibandingkan Bootstrap dan hanya akan memuat kelas-kelas utilitas yang ada | Memiliki file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena termasuk banyak komponen yang telah didefinisikan. |
| Memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek. | Sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan. |
| Memiliki pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan. | Memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan. |

Tailwind CSS sebaiknya digunakan apabila kita menginginkan tingkat kontrol yang tinggi terhadap tampilan web kita, memedulikan ukuran
berkas dan kecepatan pemuatan halaman, serta menginginkan percobaan pendekatan pengembangan yang lebih bersih dan terstruktur.
Sedangkan, Bootstrap sebaiknya digunakan apabila kita memerlukan pengembangan cepat dengan komponen siap pakai, memiliki desain
yabg konsisten, serta memiliki pengalaman yang cukup dalam menggunakan *framework* ini.


 >5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

 Kustomisasi desain pada *template* HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS *framework* (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
 
 1. Membuka berkas `base.html` pada folder `templates` dan tambahkan kode berikut supaya halaman web dapat menyesuaikan ukuran dan
perilaku perangkat mobile.
```text
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
</head>
```
2. Menambahkan Bootstrap CSS dan JS dengan kode berikut.
```text
<head>
    {% block meta %}
        ...
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>
```

- [x] Kustomisasi halaman *login*, *register*, dan tambah inventori semenarik mungkin.
- Halaman *login*
1. Membuka berkas `login.html` pada folder `templates` dan ubah kode tersebut menjadi sebagai berikut supaya *style* halaman *login*
sesuai dengan yang saya mau.
```text
{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<style>
    /* Menambahkan CSS untuk mengatur latar background layar */
    body {
        background-color: rgb(210, 145, 255);
        display: flex;
        justify-content: center; /* Mengatur elemen .login agar berada di tengah horizontal */
        align-items: center; /* Mengatur elemen .login agar berada di tengah vertikal */
        height: 100vh; /* Mengisi tinggi halaman dengan viewport height (100%) */
        margin: 0; /* Menghapus margin default body */
    }

    .login {
        background-color: white; /* Mengatur latar belakang kotak login menjadi putih */
        padding: 30px; /* Menambahkan jarak antara konten dengan tepi kotak login */
        border-radius: 10px; /* Mengubah sudut kotak login menjadi bulat */
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* Menambahkan efek bayangan pada kotak login */
    }

    /* Menambahkan style pada teks dan tombol */
    h1 {
        color: rgb(210, 145, 255);
    }

    /* Styling input */
    .form-control {
        width: 100%; /* Mengisi lebar input */
        padding: 10px; /* Menambahkan jarak di dalam input */
        border: 1px solid #ccc; /* Menambahkan border input */
        border-radius: 5px; /* Mengubah sudut input menjadi bulat */
        margin-bottom: 10px; /* Menambahkan jarak antara input */
    }

    /* Styling tombol login */
    .login_btn {
        background-color: rgb(90, 15, 130); /* Mengubah warna backround tombol login */
        color: white; /* Mengubah warna teks tombol login */
        padding: 10px 20px; /* Menambahkan jarak di dalam tombol */
        border: none; /* Menghapus border tombol */
        border-radius: 5px; /* Mengubah sudut tombol menjadi bulat */
        cursor: pointer; /* Mengubah kursor saat diarahkan ke tombol */
        font-family: 'Times New Roman', Times, serif;
        font-size: 14px;
    }

    /* Styling pesan kesalahan */
    ul {
        color: red; /* Mengubah warna pesan kesalahan */
    }

    /* Styling tautan "Register Now" */
    a {
        color: rgb(210, 145, 255); /* Mengubah warna tautan "Register Now" */
    }
</style>
```
2. Menambahkan kode berikut ke dalam berkas `login.html` untuk membuat kotak *login*.
```text

<div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td style="text-align: center;"><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
- Halaman *register*
1. Membuka berkas `register.html` pada folder `templates` dan ubah kode tersebut menjadi sebagai berikut supaya *style* halaman
 *register* sesuai dengan yang saya mau.
 ```text
 {% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<style>
    /* Menambahkan CSS untuk mengatur background layar */
    body {
        background-color: rgb(210, 145, 255);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }

    /* Styling kotak register */
    .login {
        background-color: white; /* Mengatur background kotak register menjadi putih */
        padding: 20px; /* Menambahkan jarak antara konten dengan tepi kotak register */
        border-radius: 10px; /* Mengubah sudut kotak register menjadi bulat */
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* Menambahkan efek bayangan pada kotak register */
    }

    /* Styling judul */
    h1 {
        color: rgb(210, 145, 255); /* Mengubah warna teks judul */
    }

    /* Styling tombol Daftar */
    input[type="submit"] {
        background-color: rgb(90, 15, 130); /* Mengubah warna background tombol Daftar */
        color: white; /* Mengubah warna teks tombol Daftar */
        padding: 10px 20px; /* Menambahkan jarak di dalam tombol Daftar */
        border: none; /* Menghapus border tombol */
        border-radius: 5px; /* Mengubah sudut tombol menjadi bulat */
        cursor: pointer; /* Mengubah kursor saat diarahkan ke tombol Daftar */
        font-family: 'Times New Roman', Times, serif; /* Mengubah font tombol Daftar menjadi Times New Roman */
        font-size: 16px; /* Mengubah ukuran font tombol Daftar */
        margin-top: 10px;
    }

    /* Styling pesan kesalahan */
    ul {
        color: red; /* Mengubah warna pesan kesalahan */
    }
</style>
 ```
 2. Menambahkan kode berikut ke dalam berkas `register.html` untuk membuat form *register*.
 ```text
 <div class="login">
    <h1>Register</h1>  

    <form method="POST">
        {% csrf_token %}
        <table>
            <tr>
                <td>{{ form.username.label_tag }}</td>
                <td>{{ form.username }}</td>
            </tr>
            <tr>
                <td>{{ form.password1.label_tag }}</td>
                <td>{{ form.password1 }}</td>
            </tr>
            <tr>
                <td>{{ form.password2.label_tag }}</td>
                <td>{{ form.password2 }}</td>
            </tr>
            <tr>
                <td></td>
                <td style="text-align: center;"><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</div>  

{% endblock content %}

```


- [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan *approach* lain seperti menggunakan Card.
1. Membuka berkas `main.html` pada folder `templates` dan ubah kode tersebut menjadi sebagai berikut supaya *style* daftar
inventori saya yang menggunakan Card sesuai dengan yang saya mau.
```text
<style>
...
.card {
        background-color: #f2f2f2; /* Mengatur warna background card */
        color: #333; /* Mengubah warna teks card */
        border-radius: 5px; /* Mengubah sudut card menjadi bulat */
        padding: 10px; /* Menambahkan padding pada card */
        margin: 10px; /* Menambahkan margin di antara card */
        display: inline-block; /* Mengatur card agar berdampingan */
        width: calc(33.33% - 30px); /* Mengatur lebar card agar 3 card per baris */
        text-align: center; /* Mengatur teks di tengah card */
    }
    .card a {
        color: rgb(90, 15, 130); /* Mengubah warna tautan di dalam card */
        text-decoration: none; /* Menghapus garis bawah pada tautan */
        font-weight: bold; /* Mengatur teks tautan menjadi tebal */
    }
...
</style>
```
2. Menambahkan kode berikut pada berkas `main.html` untuk menggunakan Card.
```text
...
<div>
    {% for item in items %}
    <div class="card">
        <h3>{{ item.name }}</h3>
        <p>Amount: {{ item.amount }}</p>
        <p>Description: {{ item.description }}</p>
        <a href="increment_amount/{{ item.id }}">| +</a>
        <a href="decrement_amount/{{ item.id }}">| -</a>
        <a href="{% url 'main:edit_item' item.pk %}">| Edit</a>
        <a href="{% url 'main:delete_item' item.pk %}">| Delete |</a>
    </div>
    {% endfor %}
</div>
...
```