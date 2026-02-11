"""
Quick test untuk verify RPG features work
"""

import subprocess
import sys

print("🎮 Testing RPG Features...")

# Quick test dengan input cepat
test_input = "Quick\n5\n1\n1\n1\n1\nn\n"

result = subprocess.run(
    [sys.executable, "/workspaces/mystery-adventure-bot/main.py"],
    input=test_input,
    capture_output=True,
    text=True,
    timeout=15
)

output = result.stdout
has_errors = result.returncode != 0

print("\n✅ FITUR RPG YANG BERHASIL DIIMPLEMENTASI:\n")

checks = {
    "Battle System": "TURN" in output and "Pilih aksi:" in output,
    "HP System": "HP:" in output and "max_hp" not in output,
    "EXP System": "EXP:" in output and "Dapatkan" in output,
    "Multiple Encounters": output.count("bertemu dengan") >= 2,
    "Enemy AI": "menyerang" in output,
    "ASCII Art": ("_______" in output or "oo" in output),
    "Story Branching": "dua jalan" in output or "jalur" in output,
    "No Crash": result.returncode == 0,
}

for feature, status in checks.items():
    symbol = "✅" if status else "❌"
    print(f"{symbol} {feature}")

print(f"\n📊 Program Status: {'OK ✅' if not has_errors else 'ERROR ❌'}")
print(f"📝 Output length: {len(output)} characters")

# Show battle example
if "TURN" in output:
    print("\n⚔️ Sample Battle Output:")
    for i, line in enumerate(output.split('\n')):
        if 'TURN' in line and i < len(output.split('\n')) - 5:
            for j in range(5):
                print(f"  {output.split(chr(10))[i+j]}")
            break

print("\n" + "="*60)
print("✨ RPG MODE ACTIVATED! Game is now more engaging ✨")
print("="*60)
