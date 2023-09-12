# BeautyBrews Co.
`Arini Widya Pramesti`
`2206830271`
`PBP E`


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
4. Membuat proyek Django dengan nama `beautiful_brews` dengan perintah ```django-admin startproject beautiful_brews .```
5. Pergi ke berkas ```settings.py``` lalu tambahkan ```*``` pada ```ALLOWED_HOSTS```. Dengan menambahkan ```*```, berarti saya mengizinkan akses dari semua host.
6. Memeriksa apakah Django sudah terinstall dengan perintah ```python manage.py runserver``` lalu membuka http://localhost:8000/. Apabila laman tersebut menampilkan gambar roket, maka proyek Django sudah berhasil.
7. Menghentikan server dengan menekan ```CTRL + C``` dan menonaktifkan virtual environment dengan perintah ```deactivate.```

 - [x]  Membuat aplikasi dengan nama `main` pada proyek tersebut.

a

 - [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.

a

 - [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    + `name` sebagai nama *item* dengan tipe `CharField`.
    + `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    + `description` sebagai deskripsi *item* dengan tipe `TextField`.

a

 - [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

a

 - [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

a

 - [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

a


>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

a


>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

a

>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.