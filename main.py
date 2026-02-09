import time


def dram(msg="", end="\n", flush=False):
    print(msg, end=end, flush=flush)
    time.sleep(0.5)


def apply_vibe(msg, vibe):
    v = (vibe or "").lower()
    if v == 'dramatis':
        return f"🔥 {msg} 🔥"
    if v == 'misterius':
        return f"~ {msg} ~"
    if v == 'kocak':
        return msg + " 😂"
    if v == 'santai':
        return msg + " (tenang... )"
    return msg


def lembah_coding(nama, vibe=None):
    dram(apply_vibe(f"\n{nama}, kamu memasuki Lembah Coding.", vibe))
    dram(apply_vibe("Di sini kamu menemukan sebuah laptop magis dan tugas pemecahan teka-teki.", vibe))
    time.sleep(1)
    dram(apply_vibe("Kamu berhasil menyelesaikan tantangan dan menemukan harta berupa pengetahuan baru.", vibe))
    dram(apply_vibe("Selamat, petualangan di Lembah Coding berakhir bahagia.\n", vibe))


def gunung_bug(nama, vibe=None):
    dram(apply_vibe(f"\n{nama}, kamu mendaki Gunung Bug.", vibe))
    dram(apply_vibe("Di puncak, kamu bertemu Bug raksasa yang mengacaukan kode.", vibe))
    time.sleep(1)
    dram(apply_vibe("Dengan ketelitian dan debug, kamu menaklukkan bug dan turun sebagai pahlawan.", vibe))
    dram(apply_vibe("Selamat, petualangan di Gunung Bug selesai.\n", vibe))


def game_utama():
    dram("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")
    # pilih vibe untuk mengubah 'feel' narasi
    dram("\nPilih vibe narasi:")
    dram("1. Dramatis")
    dram("2. Misterius")
    dram("3. Kocak")
    dram("4. Santai")
    dram("5. Netral (default)")
    vibe_in = input("Ketik angka atau nama vibe: ").strip()
    vibe_map = {'1': 'dramatis', '2': 'misterius', '3': 'kocak', '4': 'santai', '5': ''}
    vibe = vibe_map.get(vibe_in, vibe_in)
    nyawa = 100
    while True:
        dram("\nPilih jalurmu:")
        dram("1. Lembah Coding")
        dram("2. Gunung Bug")
        pilihan = input("Ketik 'Lembah Coding' atau 'Gunung Bug': ").strip()
        if pilihan.lower() == 'lembah coding' or pilihan == '1':
            lembah_coding(nama, vibe)
            break
        elif pilihan.lower() == 'gunung bug' or pilihan == '2':
            gunung_bug(nama, vibe)
            break
        else:
            nyawa -= 20
            if nyawa <= 0:
                dram(apply_vibe("Nyawamu habis. Permainan berakhir.", vibe))
                break
            dram(apply_vibe(f"Pilihan tidak dikenal. Nyawa berkurang 20. Sisa nyawa: {nyawa}", vibe))


if __name__ == "__main__":
    game_utama()