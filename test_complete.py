"""
Test komprehensif untuk validasi checklist
"""

import subprocess
import sys

def run_test(test_name, test_input, timeout=15):
    """Helper untuk menjalankan test"""
    print(f"\n{'='*60}")
    print(f"[TEST] {test_name}")
    print(f"{'='*60}")
    
    result = subprocess.run(
        [sys.executable, "/workspaces/mystery-adventure-bot/main.py"],
        input=test_input,
        capture_output=True,
        text=True,
        timeout=timeout
    )
    
    return result

# TEST 1: Nama disimpan dan ditampilkan
result = run_test(
    "Nama tersimpan dan dipanggil kembali",
    "Budi\n1\n1\nn\n"
)
print("Output snippet:", result.stdout[:300])
if "Budi" in result.stdout:
    print("✅ PASS: Nama 'Budi' ditampilkan")
else:
    print("❌ FAIL: Nama tidak ditampilkan")
print(f"Exit code: {result.returncode}")

# TEST 2: Input kosong ditangani
result = run_test(
    "Input kosong ditangani (EOFError prevention)",
    "Adi\n5\n\n1\nn\n"
)
print("Output snippet:", result.stdout[:400])
if result.returncode == 0:
    print("✅ PASS: Program tidak crash dengan input kosong")
else:
    print("❌ FAIL: Program crash")
    print("Error:", result.stderr[:200] if result.stderr else "No error")
print(f"Exit code: {result.returncode}")

# TEST 3: Nyawa berkurang dengan benar (habis)
result = run_test(
    "Nyawa berkurang sampai 0 (game over)",
    "Citra\n5\nsalah\nsalah\nsalah\nsalah\nsalah\nn\n",
    timeout=20
)
if "Nyawamu habis" in result.stdout:
    print("✅ PASS: Pesan 'Nyawamu habis' ditampilkan")
else:
    print("❌ FAIL: Pesan nyawa habis tidak ditampilkan")

if "Pilihan tidak dikenal" in result.stdout:
    print("✅ PASS: Sistem pengoreksi pilihan bekerja")
else:
    print("❌ FAIL: Sistem pengoreksi tidak bekerja")

if "Sisa nyawa:" in result.stdout:
    print("✅ PASS: Sistem nyawa ditampilkan")
else:
    print("❌ FAIL: Sistem nyawa tidak ditampilkan")

if result.returncode == 0:
    print("✅ PASS: Program tidak crash")
else:
    print(f"❌ FAIL: Program crash dengan exit code {result.returncode}")

# TEST 4: ASCII art ditampilkan (win)
result = run_test(
    "ASCII art menang ditampilkan",
    "Eka\n1\n1\nn\n"
)
if "_______" in result.stdout or "|  |" in result.stdout:
    print("✅ PASS: ASCII art pedang ditampilkan")
else:
    print("❌ FAIL: ASCII art pedang tidak ditampilkan")
print(f"Exit code: {result.returncode}")

# TEST 5: Main lagi berfungsi
result = run_test(
    "Main lagi berfungsi dengan benar",
    "Eka\n1\n1\ny\nFio\n1\n2\nn\n",
    timeout=20
)
if "Main lagi?" in result.stdout:
    print("✅ PASS: Pertanyaan 'Main lagi?' muncul")
else:
    print("❌ FAIL: Pertanyaan tidak muncul")

if result.stdout.count("MEMULAI PETUALANGAN") >= 2:
    print("✅ PASS: Game dimulai 2 kali (main lagi bekerja)")
else:
    print("❌ FAIL: Game hanya berjalan 1 kali")
print(f"Exit code: {result.returncode}")

print("\n" + "="*60)
print("PENGUJIAN SELESAI")
print("="*60)
