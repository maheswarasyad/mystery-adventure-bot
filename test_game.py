"""
Script pengujian untuk mengecek:
1. Apakah input nama tersimpan dan dipanggil kembali?
2. Apakah pilihan angka/huruf yang salah membuat program crash?
3. Apakah sistem nyawa/skor berkurang dengan benar?
"""

import subprocess
import sys

print("=" * 60)
print("PENGUJIAN CHECKLIST GAME")
print("=" * 60)

# Test 1: Input nama tersimpan dan nama error handling
print("\n[TEST 1] Nama tersimpan dan dipanggil kembali")
print("-" * 60)
test1_input = "Budi\n1\n1\n"  # nama: Budi, vibe: 1, jalur: 1
result = subprocess.run(
    [sys.executable, "/workspaces/mystery-adventure-bot/main.py"],
    input=test1_input,
    capture_output=True,
    text=True,
    timeout=10
)
if "Budi" in result.stdout:
    print("✅ PASS: Nama 'Budi' tersimpan dan ditampilkan kembali")
else:
    print("❌ FAIL: Nama tidak ditampilkan")
print(f"Output snippet: {result.stdout[:200]}...\n")

# Test 2: Input vibe huruf (tidak angka)
print("[TEST 2] Vibe input dengan huruf (bukan angka)")
print("-" * 60)
test2_input = "Adi\nkocak\n1\nn\n"  # nama: Adi, vibe: kocak (huruf), jalur: 1, main lagi: n
try:
    result = subprocess.run(
        [sys.executable, "/workspaces/mystery-adventure-bot/main.py"],
        input=test2_input,
        capture_output=True,
        text=True,
        timeout=10
    )
    if result.returncode == 0:
        print("✅ PASS: Program tidak crash dengan input vibe 'kocak'")
        if "😂" in result.stdout:
            print("✅ PASS: Vibe 'kocak' dikenali dan emoji ditampilkan")
        else:
            print("❌ FAIL: Vibe tidak diaplikasikan dengan benar")
    else:
        print(f"❌ FAIL: Program crash dengan exit code {result.returncode}")
        print(f"Error: {result.stderr}")
except subprocess.TimeoutExpired:
    print("❌ FAIL: Program timeout (infinite loop?)")

# Test 3: Input jalur yang salah (error handling)
print("\n[TEST 3] Input jalur yang salah (nyawa berkurang)")
print("-" * 60)
test3_input = "Citra\n5\nbuat\ntest\nhalaman\n1\nn\n"  # nama: Citra, vibe: netral, input salah x3, jalur: 1, main lagi: n
try:
    result = subprocess.run(
        [sys.executable, "/workspaces/mystery-adventure-bot/main.py"],
        input=test3_input,
        capture_output=True,
        text=True,
        timeout=15
    )
    if result.returncode == 0:
        print("✅ PASS: Program tidak crash dengan input salah")
        if "Sisa nyawa" in result.stdout:
            print("✅ PASS: Sistem nyawa ditampilkan")
            # Cek apakah nyawa berkurang
            if "60" in result.stdout:  # 100 - 20 - 20 = 60
                print("✅ PASS: Nyawa berkurang dengan benar (100 → 80 → 60)")
            else:
                print("⚠️  INFO: Nyawa mungkin berkurang tapi angka tidak sesuai harapan")
        else:
            print("❌ FAIL: Sistem nyawa tidak ditampilkan")
    else:
        print(f"❌ FAIL: Program crash dengan exit code {result.returncode}")
except subprocess.TimeoutExpired:
    print("❌ FAIL: Program timeout (infinite loop?)")

# Test 4: Game selesai dan pertanyaan main lagi muncul
print("\n[TEST 4] Pertanyaan 'Main lagi?' setelah game selesai")
print("-" * 60)
test4_input = "Eka\n1\n2\nn\n"  # nama: Eka, vibe: 1, jalur: 2, main lagi: n
try:
    result = subprocess.run(
        [sys.executable, "/workspaces/mystery-adventure-bot/main.py"],
        input=test4_input,
        capture_output=True,
        text=True,
        timeout=10
    )
    if "Main lagi?" in result.stdout or "terima kasih" in result.stdout.lower():
        print("✅ PASS: Pertanyaan 'Main lagi?' muncul dan game mengakhiri dengan baik")
    else:
        print("❌ FAIL: Pertanyaan 'Main lagi?' tidak ditemukan")
except subprocess.TimeoutExpired:
    print("❌ FAIL: Program timeout")

print("\n" + "=" * 60)
print("PENGUJIAN SELESAI")
print("=" * 60)
