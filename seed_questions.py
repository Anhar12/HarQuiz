from app import db
from models import QuizTopics, Questions, QuestionOptions

def seed_data():
    data = {
        "Pengembangan kecerdasan buatan dalam python": [
            {
                "q": "Apa tujuan utama dari proses training dalam machine learning?",
                "options": [
                    ("Menyesuaikan parameter model", True),
                    ("Membersihkan dataset", False),
                    ("Mempercepat runtime aplikasi", False),
                    ("Mengurangi jumlah fitur", False)
                ]
            },
            {
                "q": "Library mana yang biasa dipakai untuk membuat model neural network di Python?",
                "options": [
                    ("TensorFlow", True),
                    ("Matplotlib", False),
                    ("Flask", False),
                    ("Requests", False)
                ]
            },
            {
                "q": "Apa itu dataset training?",
                "options": [
                    ("Data yang digunakan untuk melatih model", True),
                    ("Data hanya untuk visualisasi", False),
                    ("File konfigurasi model", False),
                    ("Data hasil prediksi", False)
                ]
            },
            {
                "q": "Apa fungsi activation function?",
                "options": [
                    ("Memberikan nonlinearitas pada model", True),
                    ("Menghapus noise", False),
                    ("Mengatur ukuran batch", False),
                    ("Mempercepat GPU", False)
                ]
            },
            {
                "q": "Metode optimasi yang populer dalam training?",
                "options": [
                    ("Adam", True),
                    ("CRC32", False),
                    ("AES", False),
                    ("Base64", False)
                ]
            },
            {
                "q": "Proses validasi model bertujuan untuk:",
                "options": [
                    ("Menilai performa model pada data yang tidak dilatih", True),
                    ("Memperbesar dataset", False),
                    ("Membersihkan kolom kosong", False),
                    ("Mempercepat training", False)
                ]
            },
            {
                "q": "Batch size digunakan untuk:",
                "options": [
                    ("Menentukan jumlah sampel per iterasi training", True),
                    ("Menentukan jumlah layer", False),
                    ("Menghapus missing value", False),
                    ("Menambah akurasi model", False)
                ]
            },
            {
                "q": "Overfitting terjadi ketika:",
                "options": [
                    ("Model terlalu menyesuaikan data training", True),
                    ("Model terlalu sederhana", False),
                    ("Data terlalu kecil ukurannya", False),
                    ("Training terlalu cepat", False)
                ]
            },
            {
                "q": "Regularization digunakan untuk:",
                "options": [
                    ("Mengurangi overfitting", True),
                    ("Mempercepat epoch", False),
                    ("Menambah dataset otomatis", False),
                    ("Meningkatkan ukuran file model", False)
                ]
            },
            {
                "q": "Epoch dalam training ML berarti:",
                "options": [
                    ("Satu perulangan penuh melalui seluruh training data", True),
                    ("Jumlah neuron pada input layer", False),
                    ("Jumlah fitur", False),
                    ("Proses memuat data", False)
                ]
            }
        ],

        "Visi komputer": [
            {
                "q": "Apa tujuan dari convolution pada CNN?",
                "options": [
                    ("Menangkap fitur visual", True),
                    ("Meningkatkan saturasi gambar", False),
                    ("Mengganti background", False),
                    ("Memperbesar ukuran file", False)
                ]
            },
            {
                "q": "Library Python yang sering dipakai untuk computer vision?",
                "options": [
                    ("OpenCV", True),
                    ("Selenium", False),
                    ("NumPy", False),
                    ("SQLAlchemy", False)
                ]
            },
            {
                "q": "Apa itu edge detection?",
                "options": [
                    ("Menemukan batas objek", True),
                    ("Menambah resolusi gambar", False),
                    ("Menghapus noise audio", False),
                    ("Menggabungkan dua gambar", False)
                ]
            },
            {
                "q": "Model yang populer untuk object detection:",
                "options": [
                    ("YOLO", True),
                    ("SOAP", False),
                    ("SMTP", False),
                    ("SAS", False)
                ]
            },
            {
                "q": "Augmentasi gambar bertujuan untuk:",
                "options": [
                    ("Memperbanyak variasi data", True),
                    ("Mengurangi brightness", False),
                    ("Menggabungkan dataset", False),
                    ("Membuat dataset baru secara manual", False)
                ]
            },
            {
                "q": "Pooling layer umumnya digunakan untuk:",
                "options": [
                    ("Mengurangi dimensi fitur", True),
                    ("Memperbesar gambar", False),
                    ("Mengganti warna piksel", False),
                    ("Menambah resolusi", False)
                ]
            },
            {
                "q": "Fungsi Grayscale pada preprocessing gambar adalah:",
                "options": [
                    ("Mengubah gambar menjadi satu channel", True),
                    ("Menambah kontras", False),
                    ("Membuat gambar lebih berwarna", False),
                    ("Mengurangi blur", False)
                ]
            },
            {
                "q": "Object tracking berbeda dari object detection karena:",
                "options": [
                    ("Tracking mengikuti objek sepanjang waktu", True),
                    ("Tracking menambah objek ke gambar", False),
                    ("Detection memperbesar objek", False),
                    ("Detection menghapus background", False)
                ]
            },
            {
                "q": "Canny digunakan untuk:",
                "options": [
                    ("Edge detection", True),
                    ("Color grading", False),
                    ("Image blending", False),
                    ("Image compression", False)
                ]
            },
            {
                "q": "CNN cocok untuk data visual karena:",
                "options": [
                    ("Mampu mengenali pola spasial", True),
                    ("Lebih cepat dari SQL", False),
                    ("Tidak butuh training", False),
                    ("Selalu akurat", False)
                ]
            }
        ],

        "NLP (Pemrograman Neuro-linguistik)": [
            {
                "q": "Tokenization pada NLP berarti:",
                "options": [
                    ("Memecah teks menjadi unit kecil", True),
                    ("Menggabungkan teks dari banyak dokumen", False),
                    ("Membersihkan HTML tag", False),
                    ("Menambah jumlah karakter", False)
                ]
            },
            {
                "q": "Library NLP yang terkenal:",
                "options": [
                    ("NLTK", True),
                    ("BeautifulSoup", False),
                    ("OpenCV", False),
                    ("Flask", False)
                ]
            },
            {
                "q": "Word Embedding berfungsi untuk:",
                "options": [
                    ("Representasi kata ke bentuk angka", True),
                    ("Mengubah font dokumen", False),
                    ("Mengurutkan kalimat", False),
                    ("Menghapus whitespace", False)
                ]
            },
            {
                "q": "Metode populer untuk sentiment analysis:",
                "options": [
                    ("Naive Bayes", True),
                    ("K-Means", False),
                    ("Apriori", False),
                    ("Dijkstra", False)
                ]
            },
            {
                "q": "Stopwords digunakan untuk:",
                "options": [
                    ("Menghapus kata tidak penting", True),
                    ("Mendeteksi topik utama", False),
                    ("Menambah keyword ke teks", False),
                    ("Mengubah grammar", False)
                ]
            },
            {
                "q": "Stemming bertujuan untuk:",
                "options": [
                    ("Mengembalikan kata ke bentuk dasar", True),
                    ("Menambahkan suffix ke kata", False),
                    ("Menghapus angka", False),
                    ("Menambah panjang kalimat", False)
                ]
            },
            {
                "q": "NER (Named Entity Recognition) digunakan untuk:",
                "options": [
                    ("Mendeteksi entitas seperti nama dan lokasi", True),
                    ("Membuat grafik", False),
                    ("Mendeteksi warna gambar", False),
                    ("Menghapus kata unik", False)
                ]
            },
            {
                "q": "TF-IDF digunakan untuk:",
                "options": [
                    ("Memberi bobot penting pada kata", True),
                    ("Mengurutkan file", False),
                    ("Menghapus tanda baca", False),
                    ("Menambah jumlah token", False)
                ]
            },
            {
                "q": "Lemmatization berbeda dari stemming karena:",
                "options": [
                    ("Menghasilkan kata dasar yang lebih formal", True),
                    ("Lebih cepat dari stemming", False),
                    ("Tidak mengurangi kata", False),
                    ("Menghapus huruf kapital", False)
                ]
            },
            {
                "q": "Sequence-to-sequence model biasa digunakan untuk:",
                "options": [
                    ("Machine translation", True),
                    ("Image segmentation", False),
                    ("Audio mixing", False),
                    ("Clustering", False)
                ]
            }
        ],

        "Menerapkan model AI dalam aplikasi Python": [
            {
                "q": "Format umum untuk menyimpan model AI di Python:",
                "options": [
                    (".h5", True),
                    (".txt", False),
                    (".csv", False),
                    (".png", False)
                ]
            },
            {
                "q": "Framework Python untuk membuat API ML:",
                "options": [
                    ("FastAPI", True),
                    ("Bootstrap", False),
                    ("Celery", False),
                    ("Sass", False)
                ]
            },
            {
                "q": "Inference adalah proses:",
                "options": [
                    ("Menggunakan model untuk prediksi", True),
                    ("Membersihkan training data", False),
                    ("Melatih ulang model", False),
                    ("Menghapus konfigurasi lama", False)
                ]
            },
            {
                "q": "Model AI biasanya dijalankan di backend karena:",
                "options": [
                    ("Butuh resource besar", True),
                    ("Tidak bisa dibuat UI", False),
                    ("Tidak boleh diakses user", False),
                    ("Berbahaya", False)
                ]
            },
            {
                "q": "Library untuk pipeline ML di Python:",
                "options": [
                    ("Scikit-Learn", True),
                    ("Pandas-UI", False),
                    ("CSSParser", False),
                    ("Gunicorn", False)
                ]
            },
            {
                "q": "Model ML biasanya diekspor lalu dimuat ulang menggunakan:",
                "options": [
                    ("joblib atau pickle", True),
                    ("sqlite3", False),
                    ("argparse", False),
                    ("venv", False)
                ]
            },
            {
                "q": "Model deployment biasanya memerlukan:",
                "options": [
                    ("Lingkungan runtime yang stabil", True),
                    ("CSS gradient", False),
                    ("Bootstrap layout", False),
                    ("Java compiler", False)
                ]
            },
            {
                "q": "Scaling pada API inference diperlukan agar:",
                "options": [
                    ("Bisa menangani banyak request", True),
                    ("Model tidak usah dilatih", False),
                    ("Mengurangi ukuran file model", False),
                    ("Menghapus dependency", False)
                ]
            },
            {
                "q": "Peran GPU dalam inference model AI adalah:",
                "options": [
                    ("Mempercepat operasi tensor", True),
                    ("Meningkatkan kualitas UI", False),
                    ("Menyimpan file log", False),
                    ("Mengubah model ke format HTML", False)
                ]
            },
            {
                "q": "Model monitoring penting karena:",
                "options": [
                    ("Memastikan model tetap akurat setelah deployment", True),
                    ("Menghapus error server otomatis", False),
                    ("Membuat API lebih aesthetic", False),
                    ("Menambah jumlah request", False)
                ]
            }
        ]
    }
    
    for topic_name, questions in data.items():
        existing_topic = QuizTopics.query.filter_by(name=topic_name).first()
        
        if existing_topic:
            topic = existing_topic
        else:
            topic = QuizTopics(name=topic_name)
            db.session.add(topic)
            db.session.flush()

        for q in questions:
            existing_q = Questions.query.filter_by(question_text=q["q"]).first()
            if existing_q:
                question = existing_q
            else:
                question = Questions(
                    topic_id=topic.id,
                    question_text=q["q"]
                )
                db.session.add(question)
                db.session.flush()

            for opt_text, is_correct in q["options"]:
                existing_opt = QuestionOptions.query.filter_by(
                    question_id=question.id,
                    option_text=opt_text
                ).first()

                if existing_opt:
                    continue

                option = QuestionOptions(
                    question_id=question.id,
                    option_text=opt_text,
                    is_correct=is_correct
                )
                db.session.add(option)

    db.session.commit()