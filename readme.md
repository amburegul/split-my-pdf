# PDF Bookmark Splitter

Tool sederhana untuk memecah (split) file PDF menjadi beberapa file PDF berdasarkan bookmark level pertama (top-level bookmark).

Nama file output akan mengikuti nama bookmark yang ditemukan pada dokumen PDF.

## Fitur

* Split PDF berdasarkan bookmark level 1
* Nama file output otomatis mengikuti nama bookmark
* Mendukung Drag & Drop PDF ke EXE
* Mendukung mode Double Click EXE
* Otomatis membuat folder output `hasil_split`
* Membersihkan karakter ilegal pada nama file Windows

---

## Requirement

* Python 3.10 atau lebih baru

Cek versi Python:

```bash
py --version
```

atau

```bash
python --version
```

---

## Instalasi

Clone repository:

```bash
git clone https://github.com/USERNAME/PDFBookmarkSplitter.git
cd PDFBookmarkSplitter
```

Install dependency:

```bash
pip install pypdf
```

atau:

```bash
py -m pip install pypdf
```

Verifikasi:

```bash
pip show pypdf
```

---

## Menjalankan Script

Letakkan file PDF yang akan diproses pada folder yang sama dengan script.

Contoh:

```text
project/
├── PDFBookmarkSplitter.py
└── input.pdf
```

Jalankan:

```bash
py PDFBookmarkSplitter.py
```

atau

```bash
python PDFBookmarkSplitter.py
```

Script akan mencari file:

```text
input.pdf
```

dan menghasilkan:

```text
hasil_split/
├── Bab 1.pdf
├── Bab 2.pdf
├── Bab 3.pdf
└── Lampiran.pdf
```

---

## Build Menjadi EXE

Install PyInstaller:

```bash
py -m pip install pyinstaller
```

Verifikasi:

```bash
py -m PyInstaller --version
```

Build executable:

```bash
py -m PyInstaller --onefile PDFBookmarkSplitter.py
```

Hasil build:

```text
dist/
└── PDFBookmarkSplitter.exe
```

---

## Cara Menggunakan EXE

### Opsi 1 - Double Click

Letakkan:

```text
PDFBookmarkSplitter.exe
input.pdf
```

pada folder yang sama.

Kemudian jalankan:

```text
PDFBookmarkSplitter.exe
```

Program akan otomatis mencari:

```text
input.pdf
```

dan memprosesnya.

Jika file tidak ditemukan, program akan menampilkan pesan:

```text
ERROR: input.pdf tidak ditemukan.

Cara penggunaan:
1. Letakkan input.pdf di folder yang sama dengan EXE
ATAU
2. Drag & drop file PDF ke EXE
```

---

### Opsi 2 - Drag & Drop

Drag file PDF ke executable:

```text
dokumen.pdf
    ↓
PDFBookmarkSplitter.exe
```

Program akan memproses file tersebut secara otomatis.

Output akan dibuat pada folder yang sama dengan file PDF sumber:

```text
dokumen.pdf
hasil_split/
```

---

## Struktur Output

Contoh bookmark:

```text
BAB 1
BAB 2
BAB 3
Lampiran
```

Hasil:

```text
hasil_split/
├── BAB 1.pdf
├── BAB 2.pdf
├── BAB 3.pdf
└── Lampiran.pdf
```

---

## Troubleshooting

### 'pyinstaller' is not recognized

Gunakan:

```bash
py -m PyInstaller --onefile PDFBookmarkSplitter.py
```

bukan:

```bash
pyinstaller --onefile PDFBookmarkSplitter.py
```

---

### ModuleNotFoundError: No module named 'pypdf'

Install dependency:

```bash
py -m pip install pypdf
```

---

### Tidak ditemukan bookmark level 1

Pesan:

```text
Tidak ditemukan bookmark level 1.
```

Penyebab:

* PDF tidak memiliki bookmark
* Bookmark berada pada level yang lebih dalam
* Bookmark rusak atau tidak dapat dibaca

---

## Struktur Repository

```text
PDFBookmarkSplitter/
├── PDFBookmarkSplitter.py
├── README.md
└── .gitignore
```

Contoh `.gitignore`:

```gitignore
__pycache__/
build/
dist/
*.spec
hasil_split/
```

---

## Library yang Digunakan

* pypdf
* PyInstaller

---

## License

MIT License
