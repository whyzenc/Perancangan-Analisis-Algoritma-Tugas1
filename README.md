# Perancangan-Analisis-Algoritma-Tugas1

Repositori ini berisi informasi mengenai tugas yang telah diselesaikan oleh mahasiswa. Setiap tugas dilengkapi dengan penjelasan serta tautan yang tersedia di bawah ini.

Dosen : Randi Proska Sandra, M.Sc<br>
Kode Kelas : INF1.62.4001 <br>
Seksi : 202423430074<br>
Mahasiswa : Whenny Zenica (23343022)<br><br>

## Prim's-Algorithm


<p align="justify">
<b> Algoritma Prim (Prim’s Algorithm)</b> adalah metode dalam teori graf yang digunakan untuk menemukan Minimum Spanning Tree (MST) pada graf berbobot dan terhubung. MST adalah subgraf yang mencakup semua simpul dengan total bobot sisi minimum tanpa membentuk siklus. 
sebuah algoritme dalam teori graf untuk mencari pohon rentang minimum untuk sebuah graf berbobot yang saling terhubung. Ini berarti bahwa sebuah himpunan bagian dari edge yang membentuk suatu pohon yang mengandung node, di mana bobot keseluruhan dari semua edge dalam pohon diminimalisasikan. Bila graf tersebut tidak terhubung, maka graf itu hanya memiliki satu pohon rentang minimum untuk satu dari komponen yang terhubung. Algoritme ini ditemukan pada 1930 oleh matematikawan Vojtěch Jarník dan kemudian secara terpisah oleh computer scientist Robert C. Prim pada 1957 dan ditemukan kembali oleh Dijkstra pada 1959. Karena itu algoritme ini sering dinamai algoritme DJP atau algoritme Jarnik.<br><br>

  <p align="justify">
Langkah-langkahnya adalah sebagai berikut:  </p>
<ol>
 <li>buat sebuah pohon yang terdiri dari satu node, dipilih secara acak dari graf</li>
 <li>buat sebuah himpunan yang berisi semua cabang di graf</li>
 <li>loop sampai semua cabang di dalam himpunan menghubungkan dua node di pohon </li>
</ol>

* **hapus dari himpunan satu cabang dengan bobot terkecil yang menghubungkan satu node di pohon dengan satu node di luar pohon**
* **hubungkan cabang tersebut ke pohon**<br><br>

  Algoritma ini dimulai dengan memilih sembarang simpul sebagai titik awal. Selanjutnya, secara iteratif, algoritma menambahkan sisi dengan bobot terkecil yang menghubungkan simpul yang sudah terhubung ke simpul yang belum terhubung, hingga semua simpul tergabung dalam MST. Kompleksitas waktu algoritma Prim bervariasi tergantung pada implementasinya:
</p>

* **Menggunakan adjacency matrix dan pencarian minimum langsung: O(V²).**
* **Menggunakan priority queue (Heap) dan adjacency list: O(E log V).**
   
<p align="justify">
<b> Sejarah dan Pengembang</b>
  Algoritma ini pertama kali diperkenalkan oleh matematikawan Vojtěch Jarník pada tahun 1930 dan kemudian secara independen oleh ilmuwan komputer Robert C. Prim pada tahun 1957. Pada tahun 1959, Edsger W. Dijkstra juga menemukan algoritma serupa. Oleh karena itu, algoritma ini sering disebut sebagai algoritma DJP (Dijkstra-Jarník-Prim) atau algoritma Jarník dalam beberapa literatur. 
id.wikipedia.org </p>
