# Perancangan-Analisis-Algoritma-Tugas1
<img src="https://www.thedataschool.com.au/wp-content/uploads/2022/01/logo-data-structures-algorithms.png" width="34" height="34">

Repositori ini berisi penjelasan mengenai materi dari tugas yang dikerjakan oleh mahasiswa. Penjelasan beserta link setiap tugas telah tertera di bawah.

Dosen : Randi Proska Sandra, M.Sc<br>
Kode Kelas : INF1.62.4001 <br>
Seksi : 202423430074<br>
Mahasiswa : Whenny Zenica (23343022)<br><br>

## Prim's-Algorithm

<img src="https://upload.wikimedia.org/wikipedia/en/9/96/Prim-animation.gif">

<p align="justify">
<b> Algoritma Prim (Prim’s Algorithm)</b> adalah metode dalam teori graf yang digunakan untuk menemukan Minimum Spanning Tree (MST) pada graf berbobot dan terhubung. MST adalah subgraf yang mencakup semua simpul dengan total bobot sisi minimum tanpa membentuk siklus. 
id.wikipedia.org.<br><br>
  
  Algoritma ini dimulai dengan memilih sembarang simpul sebagai titik awal. Selanjutnya, secara iteratif, algoritma menambahkan sisi dengan bobot terkecil yang menghubungkan simpul yang sudah terhubung ke simpul yang belum terhubung, hingga semua simpul tergabung dalam MST. Kompleksitas waktu algoritma Prim bervariasi tergantung pada implementasinya:
</p>

* **Menggunakan adjacency matrix dan pencarian minimum langsung: O(V²).**
* **Menggunakan priority queue (Heap) dan adjacency list: O(E log V).**
   
<p align="justify">
<b> Sejarah dan Pengembang</b>
  Algoritma ini pertama kali diperkenalkan oleh matematikawan Vojtěch Jarník pada tahun 1930 dan kemudian secara independen oleh ilmuwan komputer Robert C. Prim pada tahun 1957. Pada tahun 1959, Edsger W. Dijkstra juga menemukan algoritma serupa. Oleh karena itu, algoritma ini sering disebut sebagai algoritma DJP (Dijkstra-Jarník-Prim) atau algoritma Jarník dalam beberapa literatur. 
id.wikipedia.org </p>
