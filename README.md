**Daegu Apartement Price Prediction**

**Business Problems :**
Daegu merupakan wilayah kota metropolitan terbesar ke-4 dalam hal populasi (5,05 juta jiwa), dan menjadi kota perdagangan terbesar ke-3 di Korea Selatan. Populasi Daegu cukup homogen dengan sejumlah imigran [(Source)](https://id.wikipedia.org/wiki/Daegu)

Salah satu tantangan yang dihadapi oleh masyarakat Daegu adalah kebutuhan tempat tinggal, kebutuhan tersebut berhadapan langsung dengan biaya yang harus dikeluarkan untuk mendapatkannya. Apartement muncul sebagai salah satu solusi pemenuhan tempat tinggal masyarakat Daegu, keberadaan apartemen menjadi salah satu terobosan yang menawarkan tempat tinggal dengan penggunaan lahan yang lebih efisien dan menawarkan aksesibilitas yang baik bagi penghuninya beserta kelengkapan fasilitas didalamnya.

Dalam konteks ini, sangatlah penting untuk memahami dan menganalisis lebih lanjut, terkait faktor-faktor yang mempengaruhi harga jual / beli / sewa dari apartement. Secara umum harga apartement dipengaruhi oleh variabel internal berupa : kondisi fisik (meliputi tahun pembangunan dan ukuran apartement), jumlah fasilitas yang tersedia didalamnya, dan faktor lainnya. Selain itu, terdapat faktor eksternal yang juga dapat mempengaruhinya, yakni : lokasi apartemen, aksesibilitas ke fasilitas umum (meliputi perkantoran, sekolah, pasar, stasiun), dan kenyamanan ataupun keamanan lingkungan apartement.

Kondisi tersebut tercermin dari harga per meter persegi hunian yang berada dipusat kota dan luar pusat kota Daegu memiliki perbedaan yang signifikan, hal ini menunjukkan harga apartemen dipengaruhi oleh jumlah permintaan yang tinggi yang disebabkan oleh faktor lokasi apartement.


**Problems Statement:**
Dengan mempertimbangkan situasi tersebut diatas, timbul kebutuhan bagi para pemilik apartement / agen property dan juga pihak pembeli / penyewa apartemen agar dapat menentukan harga jual / harga beli / harga sewa yang tepat.

Bagi pemilik apartemen atau agen property membutuhkan suatu acuan harga yang dijadikan dasar dalam melakukan penawaran unit apartement, sehingga dengan menggunakan acuan tersebut baik pemilik atau agen property terhindar dari kesulitan mendapatkan calon pembeli / penyewa disebabkan penetapan harga jual yang jauh lebih tinggi dari harga wajar, dan juga harga acuan tersebut dapat menghindarkan pemilik / agen property dari kehilangan potensi keuntungan akibat menetapkan harga yang terlalu rendah.

Kebalikan dari kondisi diatas, bagi calon pembeli / penyewa menggunakan acuan harga sebagai bahan pertimbangan dalam mengambil keputusan, unit apartement mana yang akan dibeli / disewa. Mereka mendapatkan gambaran yang lebih jelas terkait dengan harga apartement yang mereka inginkan, sehingga pada akhirnya pembeli / penyewa mendapatkan transparansi harga dari apartement.

Untuk itu, diperlukan **analisis mendalam terhadap faktor internal dan eksternal yang mempengaruhi harga apartemen**. Selain itu, juga diperlukan suatu **alat ukur yang mampu menghasilkan prediksi harga jual** suatu unit apartement


**Goals / Tujuan :**
Dengan mengetahui lebih lanjut mengenai **faktor-faktor yang paling berpengaruh** terhadap harga jual apartement, maka baik penjual maupun pembeli akan memiliki **pertimbangan lebih terukur** dalam mengambil keputusan.

Selain itu, dengan memanfaatkan teknik analisis data **akan dibuat suatu model prediksi yang menghasilkan harga** jual / harga beli wajar dari unit apartement di Kota Daegu secara lebih akurat.

Model ini nantinya diharapkan dapat membantu pihak pemilik / agen property dalam menentukan harga jual yang kompetitif sehingga dapat mengoptimalkan profit yang diperoleh, sedangkan bagi pihak pembeli / penyewa dapat memutuskan apartement mana yang sesuai dengan kebutuhan namun masih masuk dalam kemampuan finansialnya.


**Analytics Approach / Pendekatan Analisis :**
**1. Analisis faktor yang mempengaruhi harga jual apartement**

- Dengan memanfaatkan teknik analisis statistik, melakukan identifikasi faktor apa yang paling berpengaruh terhadap harga jual apartement, dan mengukur korelasi antar faktor / feature yang mempengaruhi dengan harga jual apartement tersebut

**2. Pembuatan Prediction Machine Learning**

- Machine Learning yang akan dikembangkan berupa model prediksi harga jual apartement. Model ini menggunakan `metode regresi`, mengingat target yang diinginkan berupa harga yang bersifat kontinu

- Dalam hal pengembangan model prediksi, juga akan memperhatikan faktor / feature apa saja yang digunakan, dan berusaha untuk menghindari adanya overfitting atau underfitting terhadap model, yang nantinya mempengaruhi performa model dalam menghasilkan suatu prediksi harga jual


- **Metrics Evaluation :**
- Untuk menguji performa model regresi dalam memprediksi harga jual apartement, terdapat 3 (tiga) metrik evaluasi yang digunakan :

**1. Root Mean Square Error (RMSE)**

- Merupakan nilai rata-rata dari akar kuadrat dari selisih antara nilai prediksi dengan nilai aktualnya.

**2. Mean Absolute Error (MAE)**

- Merupakan nilai rata-rata dari selisih absolut antara prediksi dengan nilai aktualnya.

**3. Mean Absolute Percentage Error (MAPE)**

- Merupakan nilai rata-rata dari persentase kesalahan absolut dari dihasilkan oleh suatu model.

Hasil dari ketiga metrik tersebut mengindikasikan tingkat keakuratan dari prediksi harga yang dihasilkan, semakin rendah nilai metrik maka hasil prediksi model semakin akurat.


**Batasan Data / Model**
Terdapat beberapa batasan yang digunakan dalam pengembangan model, yakni :

1. Model dikhususkan untuk prediksi harga properti di Kota Daegu saja

2. Data yang digunakan meliputi faktor : jarak, lokasi, fasilitas (berupa kantor public, subway, sekolah, parkir), ukuran dan tahun pembangunan apartement


**KESIMPULAN :*

1. Machine Learning yang dibuat model finalnya menggunakan algoritma **DecisionTree Regressor**

- Hal ini didasarkan pada serangkaian uji coba terhadap beberapa jenis algoritma regresi, kemudian dilakukan perbandingan hasil metrics evaluasi, dan telah dilakukan Hyperparameter Tuning, serta memperhatikan Feature Importance. 

- Algoritma **DecisionTree Regressor** memiliki nilai error yang rendah dimana mampu memprediksikan harga jual apartement dengan besaran error (MAPE) sebesar 18.69% dari harga jual aktual apartement.

- Algoritma **DecisionTree Regressor** juga memiliki feature importance yang lebih beragam jika dibandingkan dengan algoritma **XGBoost Regression** yang merupakan algoritma dengan nilai error terendah, namun memiliki keterbatasan pada feature importancenya yang hanya didominasi oleh 1 feature saja, hal ini sangat dimungkinkan model akan underfitting saat dilakukan deploy.

2. Terdapat dengan 5 faktor / features utama yang memiliki pengaruh signifikan terhadap harga jual apartement, adalah :

    **a. Fasilitas(ETC)**, menjadi faktor yang paling berpengaruh thd harga apartement, dengan score feature importance sebesar 0.29. Jumlah fasilitas (taman, pusat perbelanjaan) yang dekat dengan apartement, menjadi salah satu faktor yang diperhitungkan karena penghuni apartement membutuhkan fasilitas tsb untuk memenuhi kebutuhannya, hal ini menjadikan apartement yang memenuhi kriteria tsb dapat menaikkan harga jualnya lebih tinggi daripada apartement dengan kondisi sebaliknya.

    **b. Ukuran Apartement**, ukuran apartement menjadi faktor penting lainnya yang dapat mempengaruhi harga jual apartement dengan nilai feature importance sebesar 0.28. Pembeli secara umum, akan memilih apartement dengan ukuran yang lebih besar, guna kenyamanan yang lebih baik. Sehingga permintaan yang banyak akan apartement dengan ukuran yang lebih besar, dapat menjadi pemicu kenaikan harga jualnya.

    **c. YearBuilt**, apartement dengan tahun pembangunan yang lebih muda, dianggap memiliki faktor kenyamanan dan keamanan yang lebih baik bagi penghuninya, dan biasanya apartement tersebut sudah dilengkapi fasilitas yang lebih memadai daripada apartement bangunan lama. Sehingga tahun pembangunan apartement memberikan pengaruh yang signifikan terhadap harga jual apartement, score feature importance sebesar 0.13.

    **d. Kedekatan dengan Fasilitas Sekolah**, memiliki pengaruh yang signifikan dengan score feature importance sebesar 0.09. Kedekatan apartement dengan fasilitas sekolah menjadi salah satu keuntungan yang dipunyai apartement karena banyak pembeli berminat untuk melakukan pembelian unit apartement tersebut, hal ini juga menjadi faktor pendorong suatu harga unit apartement naik

    **e. Fasilitas Apartement**, feature importance ini mempunyai score sebesar 0.05. Fasilitas apartement yang ditawarkan menjadi daya tarik tersendiri bagi pembeli yang menginginkan tambahan nilai dari tempat huniannya, fasilitas tsb sebagai contoh adanya kolam renang, fasilitas gym, ruang hijau, dll. Fasilitas tsb menjadi salah satu faktor pendorong untuk dapat menaikkan harga jual unit apartement.

    Faktor-faktor tersebut diatas juga dapat dijadikan sebagai bahan strategi pemasaran untuk mengikat calon pembeli

3. Dengan menggunakan Machine Learning Prediksi ini, akan memberikan manfaat berupa :

    **a. Pemilik / Agen Property**

    - Model prediksi ini dapat membantu dengan **mudah dan terukur** dalam menentukan harga jual apartement, karena model ini menghasilkan prediksi harga jual yang sudah disesuaikan dengan beberapa faktor yang mempengaruhi, sehingga para pemilik atau agen property dapat menggunakannya sebagai salah satu acuan yang cukup memadai. Namun perlu diingat terdapat error / kesalahan model dalam memprediksi yang tercermin dari besaran nilai MAPE yang mengindikasikan terdapat perbedaan sebesar 18,69% harga prediksi dari harga jual aktual.

    - Dengan menggunakan acuan harga prediksi model, menjadikan pemilik / agen property terhindar dari kerugian akibat penetapan harga yang jauh lebih rendah dari harga wajarnya, ataupun dapat menghasilkan keuntungan yang optimal karena dapat menjual apartement diharga yang sesuai (terhindar dari tidak laku karena penetapan harga yang ketinggian).

    **b. Pembeli / Penyewa**

    - Hasil dari model prediksi dapat membantu para pembeli mempertimbangkan unit apartemen tang diinginkan untuk disesuaikan dengan kemampuan yang dimilikinya, selain itu juga memberikan rasa nyaman kepada pembeli karena mendapatkan **tranparansi harga** unit apartement.

    **c. Data Driven**

    - Keputusan yang diambil dengan mempertimbangkan hasil prediksi model, menjadi dasar yang kuat untuk mengurangi adanya ketergantungan terhadap intuisi dan meningkatkan tingkat objektivitas dalam mengambil suatu keputusan.

4. Machine Learning ini memiliki beberapa batasan yang harus diperhatikan :

    a. Terkait data yang dipelajari merupakan data apartement di Kota Daegu, maka model ini hanya berlaku untuk memprediksi harga jual apartement di Kota Daegu saja

    b. Masih terdapat besaran error yang harus menjadi perhatian bagi para penggunanya, sehingga tidak sampai menjadikan hasil prediksi model sebagai **harga yang mengikat** dan dijadikan acuan utama dalam menetapkan harga jual



**REKOMENDASI :**

Berikut rekomendasi berdasarkan hasil prediksi Machine Lerning :

1. Hasil prediksi yang dihasilkan model, sebaiknya dijadikan salah satu bahan pertimbangan dalam penentuan harga jual apartement, hal ini mengingat masih adanya error yang dihasilkan oleh model prediksi.

2. Hasil prediksi yang dihasilkan oleh Machine Learning haruslah dilakukan evaluasi secara berkala, guna memastikan keakuratan dari prediksi yang dihasilkan, mengingat property adalah salah satu jenis usaha yang berkembang dengan pesat (dipengaruhi adanya demand yang sangat tinggi, selera konsumen, dan tingkat perekonomian)

3. Model yang digunakan dalam Machine Learning prediksi, dapat dikembangkan dengan menggunakan algoritma lain yang lebih komplek dengan harapan mendapatkan pendekatan yang lebih baik (tingkat error yang jauh lebih rendah) dibandingkan dengan model / algoritma yang saat ini digunakan yakni : **DecisionTree Regression**

4. Terdapat usulan penambahan feature yang dinilai memiliki pengaruh signifikan terhadap harga jual, yakni : **asuransi bangunan, tipe full-furnished atau semi-furnish, diskon yang ditawarkan**. 

5. Machine learning ini memiliki keterbatasan jumlah data yang dipelajari, yakni dari data awal berjumlah 4123 data, menjadi 2611 data saja yang dapat dipelajari (dihapus karena duplicated atau outliers), hal ini dapat dijadikan catatan dalam pengembangan lebih lanjut kedepannya, yaitu menambahkan jumlah data untuk dipelajari oleh model, sehingga model diharapkan dapat memberikan hasil prediksi yang lebih akurat lagi.
