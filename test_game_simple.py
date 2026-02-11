"""
Test sederhana untuk cek error handling dan nyawa
"""

import subprocess
import sys

print("=" * 60)
print("TEST: Input salah dan nyawa berkurang")
print("=" * 60)

# Input: nama=Test, vibe=5, salah 1x, salah 2x, salah 3x (nyawa habis), main lagi=n
test_input = "TestUser\n5\nsalah\nsalah\nsalah\nn\n"

result = subprocess.run(
    [sys.executable, "/workspaces/mystery-adventure-bot/main.py"],
    input=test_input,
    capture_output=True,
    text=True,
    timeout=20
)

print(f"Exit code: {result.returncode}")
print("\n--- OUTPUT ---")
print(result.stdout)

if result.stderr:
    print("\n--- ERROR ---")
    print(result.stderr)

# Debug info
print("\n--- ANALYSIS ---")
if "Pilihan tidak dikenal" in result.stdout:
    print("✅ Error handling bekerja (pesan 'Pilihan tidak dikenal' muncul)")
else:
    print("❌ Error handling tidak bekerja")

if "Nyawamu habis" in result.stdout:
    print("✅ Sistem nyawa bekerja (crash detection muncul)")
else:
    print("❌ Sistem nyawa tidak bekerja")

if result.returncode == 0:
    print("✅ Program tidak crash")
else:
    print(f"❌ Program crash dengan exit code {result.returncode}")
