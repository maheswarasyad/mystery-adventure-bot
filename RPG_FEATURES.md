# 🎮 Mystery Adventure Bot - RPG Features

## Fitur RPG yang Ditambahkan

Game ini sekarang memiliki **sistem RPG yang kompleks** agar cerita tidak langsung selesai. Berikut adalah fitur-fiturnya:

### 1. **Sistem Battle Turn-Based** ⚔️
- Pertarungan interaktif dengan musuh
- Pemain dapat memilih aksi setiap turn:
  - **Serang (Attack)**: Serangan normal dengan damage acak
  - **Pertahanan (Defend)**: Menaikkan defense, mengurangi damage yang diterima
  - **Mantra Ajaib (Special)**: Skill khusus dengan damage tinggi (jika memiliki item)
- Sistem damage dengan formula: `Damage - Defence Musuh = Actual Damage`
- Turn-based mechanics alternating antara pemain dan musuh

### 2. **Sistem Level & Experience** 📈
- Pemain mulai di **Level 1**
- Setiap kemenangan musuh memberikan **Experience Points (EXP)**
- Ketika EXP mencapai 100:
  - **Level Up!** 🎉
  - HP maksimal meningkat +20
  - Attack meningkat +3
  - Defense meningkat +2
  - EXP direset ke 0

### 3. **Inventory System** 🎒
- Pemain dapat mengumpulkan item dalam petualangan:
  - **Scroll Pengetahuan**: Item knowledge dari Librarian Bot
  - **Mantra Ajaib**: Skill special untuk serangan powerful
- Item dapat digunakan dalam battle untuk aksi spesial

### 4. **Sistem Gold** 💰
- Setiap musuh yang dikalahkan memberikan Gold
- Gold disimpan dan ditampilkan di akhir permainan
- Untuk upgrade equipment di masa depan (ekstensi)

### 5. **Multiple Encounters** 🌍
Setiap area memiliki **multiple enemy encounters** sebelum boss:

#### **Lembah Coding:**
1. **Librarian Bot** (HP: 30) - Penjaga perpustakaan
2. **Cache Spirit** (HP: 25) - Makhluk energi *atau* **Shadow Debugger** (HP: 45) - Pilihan jalur
   - Timur: Cache Spirit (mudah)
   - Barat: Shadow Debugger (sulit, reward lebih besar)
3. **Boss Final: Algoritma Jahat** (HP: 80) - Raja semua bug di Lembah

#### **Gunung Bug:**
1. **Crawler Bug** (HP: 35) - Bug agresif di lereng
2. **Parser Loop** (HP: 40) - Terjebak dalam loop
3. **Boss Final: Giant Bug Raksasa** (HP: 100) - Raja bug puncak gunung

### 6. **Dynamic Story Branching** 🌳
- Pilihan jalur (Timur/Barat) di Lembah Coding mempengaruhi musuh dan kesulitan
- Cerita adaptif dengan narasi yang berubah sesuai pilihan
- Multiple endings berdasarkan hasil battle

### 7. **Status Display** 📊
Setiap turn menampilkan:
```
Pemain: [Nama | Lvl X | HP: Y/Z | EXP: A/100]
Musuh:  Monster Name | HP: B/C
```

### 8. **ASCII Art untuk Moments Penting** 🎨
- **Pedang** (Kemenangan) ditampilkan saat berhasil mengalahkan boss
- **Tengkorak** (Kekalahan) ditampilkan saat pemain kalah melawan musuh

---

## Perbedaan Sebelum & Sesudah

| Aspek | Sebelum | Sesudah |
|-------|---------|---------|
| Durasi Game | 30 detik | 5-15 menit |
| Encounters | 1 (langsung selesai) | 3-4+ pertarungan |
| Interaksi | Pilihan area saja | Battle turns + strategy |
| Progression | Tidak ada | Level, EXP, Inventory |
| Storyline | Linear | Branching paths |
| Difficulty | Flat | Scaling dengan journey |

---

## Cara Bermain

1. **Inputkan nama** dan pilih **vibe narasi** (Dramatis/Misterius/Kocak/Santai)
2. **Pilih jalur**: Lembah Coding atau Gunung Bug
3. **Hadapi musuh pertama**: Pilih action (Attack/Defend/Special)
4. **Dapatkan EXP dan Gold**, naik level jika EXP penuh
5. **Lanjut ke musuh berikutnya** dengan HP yang sudah berkurang
6. **Hadapi Boss Final** dengan semua skill dan item yang sudah terkumpul
7. **Menang** = Dapatkan ASCII art pedang + final stats
8. **Kalah** = ASCII art tengkorak + end game (game over)

---

## Tips Bermain

- **Defend strategy**: Gunakan pertahanan saat HP rendah
- **Mantra Ajaib**: Gunakan skill khusus untuk burst damage pada boss
- **Pilih jalur sulit**: Shadow Debugger memberikan EXP lebih banyak untuk level up
- **Health management**: Setiap pertarungan membuat HP berkurang, rencanakan dengan baik

---

Selamat bermain dan nikmati petualangan digital yang lebih mendalam! 🎮✨
