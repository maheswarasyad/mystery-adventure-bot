# 🎮 Mystery Adventure Bot - RPG Edition

**Sebuah petualangan digital interaktif dengan sistem RPG lengkap!**

## 📖 Deskripsi

Mystery Adventure Bot adalah game text-based berbasis Python yang menggabungkan storytelling dengan sistem RPG yang kompleks. Pemain akan menghadapi berbagai musuh, mengumpulkan item, naik level, dan mengalahkan boss dalam petualangan yang mendalam.

**Durasi permainan**: 8-20 menit (sebelumnya hanya ~30 detik)

---

## 🎯 Fitur Utama RPG

### ⚔️ **Sistem Battle Turn-Based**
- Pertarungan interaktif dengan musuh
- 3 pilihan aksi: **Serang**, **Pertahanan**, **Mantra Ajaib** (special)
- Damage system dengan formula: `Damage - Defense = Actual Damage`
- Turn-based mechanics yang strategic

### 📈 **Level & Experience System**
- Mulai level 1, naik level dengan kumpulkan 100 EXP
- Setiap level up: HP +20, Attack +3, Defense +2
- EXP reward dari setiap musuh yang dikalahkan

### 🎒 **Inventory System**
- Kumpulkan item dalam perjalanan
- Item spesial: **Scroll Pengetahuan**, **Mantra Ajaib**
- Item dapat digunakan dalam battle untuk efek khusus

### 💰 **Currency System**
- Setiap musuh memberikan Gold
- Total gold ditampilkan di akhir permainan

### 🌍 **Multiple Encounters**
- **3-4 musuh per petualangan** sebelum boss final
- Musuh dengan stat berbeda dan loot unik
- Encounter berganda membuat game lebih challenging

### 🌳 **Story Branching**
- **Lembah Coding**: Pilih jalur Timur (mudah) atau Barat (sulit)
- Pilihan mempengaruhi musuh yang dihadapi, reward, dan cerita
- Narasi dinamis sesuai pilihan

### 👹 **Boss Battles**
- **Algoritma Jahat** (Lembah Coding) - HP 80
- **Giant Bug Raksasa** (Gunung Bug) - HP 100
- Boss dengan stat tinggi dan reward maksimal

### 🎨 **ASCII Art & Visual Effects**
- Pedang 🎉 untuk kemenangan
- Tengkorak 💀 untuk kekalahan
- Efek typing dengan delay visual

---

## 🎮 Cara Bermain

### Instalasi & Jalankan
```bash
python3 main.py
```

### Gameplay Flow
1. **Inputkan nama** dan pilih **vibe narasi** (Dramatis/Misterius/Kocak/Santai)
2. **Pilih jalur**: Lembah Coding atau Gunung Bug
3. **Hadapi musuh** dengan memilih aksi setiap turn
4. **Naik level** saat EXP penuh
5. **Kumpulkan item** dan gold dari kemenangan
6. **Hadapi boss final** dengan equipment yang sudah terkumpul
7. **Menang/Kalah** - Lihat final stats dan option replay

### Tips Bermain
- **Strategize**: Gunakan Defend saat HP rendah
- **Level up**: Pilih jalur sulit untuk dapatkan EXP lebih banyak
- **Item hunting**: Kumpulkan Mantra Ajaib untuk burst damage
- **Health management**: Setiap battle berkurang HP, plan dengan baik

---

## 📊 Perbandingan Fitur

| Fitur | Sebelum | Sesudah |
|-------|---------|---------|
| Durasi Game | 30 detik | 8-20 menit |
| Enemies | 1 (langsung selesai) | 3-4+ pertarungan |
| Interaksi | Pilihan jalur saja | Battle strategy turn-based |
| Progression | Tidak ada | Level, EXP, Inventory |
| Items | Tidak ada | Scroll, Skills |
| Difficulty | Flat | Scaling dengan journey |
| Story | Linear | Branching paths |

---

## 🗂️ Struktur File

```
mystery-adventure-bot/
├── main.py                      # Game utama
├── README.md                    # Dokumentasi ini
├── RPG_FEATURES.md              # Detail fitur RPG
├── IMPLEMENTATION_SUMMARY.md    # Summary teknis
└── test_*.py                    # Test files
```

---

## 🛠️ Teknologi

- **Language**: Python 3
- **Libraries**: `time`, `random`
- **Mode**: Text-based (Terminal)

---

## 📈 Game Architecture

### Classes
```python
class Pemain:
    nama, level, exp, hp, max_hp
    attack, defense, inventory, gold
    # Methods: gain_exp(), level_up(), add_item()

class Musuh:
    nama, hp, max_hp, attack, defense
    exp_drop, gold_drop
    # Methods: take_damage()
```

### Functions
- `battle_system()` - Engine pertarungan
- `lembah_coding()` - Path 1 dengan 3+ encounters
- `gunung_bug()` - Path 2 dengan 3+ encounters
- `dram()` - Typed display effect
- `apply_vibe()` - Narasi styling
- `get_input()` - Safe input handling

---

## 🎯 Musuh & Boss Stats

### Lembah Coding
| Enemy | HP | ATK | DEF | EXP | Gold |
|-------|----|----|-----|-----|------|
| Librarian Bot | 30 | 8 | 3 | 25 | 15 |
| Cache Spirit | 25 | 6 | 2 | 20 | 10 |
| Shadow Debugger | 45 | 12 | 5 | 40 | 25 |
| **Algoritma Jahat** | **80** | **15** | **6** | **100** | **50** |

### Gunung Bug  
| Enemy | HP | ATK | DEF | EXP | Gold |
|-------|----|----|-----|-----|------|
| Crawler Bug | 35 | 9 | 4 | 30 | 20 |
| Parser Loop | 40 | 11 | 5 | 35 | 22 |
| **Giant Bug Raksasa** | **100** | **18** | **8** | **150** | **75** |

---

## 🌟 Fitur Spesial

### Vibe Narasi
Ubah "feel" cerita dengan styling:
- 🔥 **Dramatis**: Narasi dengan emoji api
- ~ **Misterius**: Narasi dengan tilde
- 😂 **Kocak**: Narasi dengan emoji tertawa
- **(tenang...)** **Santai**: Narasi relaxed
- Normal **Netral**: Default style

### Battle Actions
```
1. Serang (Attack)          → 7-13 damage
2. Pertahanan (Defend)      → Defense +5 temporarily
3. Mantra Ajaib (Special)   → 25-35 damage (jika punya item)
```

---

## 🚀 Extensibility

Saat ini arsitektur memudahkan penambahan:
- ✨ **Equipment system** (sword, armor)
- ✨ **Multiple skill trees**
- ✨ **Boss phases** (multi-stage boss)
- ✨ **NPC quests** dan dialogue
- ✨ **Save/load** game progress
- ✨ **Stat allocation** manual
- ✨ **Rare drops** dengan probabilitas

---

## 📝 Catatan Pengembang

- Game menggunakan `time.sleep(0.5)` untuk efek visual typing
- Battle outcome adalah randomized (RNG untuk damage)
- Level up system bersifat linear (100 EXP per level)
- Defense berpengaruh pada damage reduction calculation

---

## 🎯 Next Steps / TODO

- [ ] Tambah equipment shop
- [ ] Leaderboard sistem
- [ ] Save/load persistensi
- [ ] Lebih banyak enemies
- [ ] Quest system
- [ ] Multi-phase boss battles

---

## 📧 Support

Segala pertanyaan atau saran tentang game dapat dieksplorasi lebih lanjut.

**Enjoy your digital adventure!** 🎮✨

---

*Created with ❤️ for interactive storytelling*