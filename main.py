import time
import random


# ==================== GENSHIN IMPACT STYLE ====================
# ELEMENTS & CHARACTER SYSTEM
# =============================================================

# Element Types
ELEMENTS = {
    'pyro': {'name': 'Pyro', 'symbol': '🔥', 'color': 'orange'},
    'hydro': {'name': 'Hydro', 'symbol': '💧', 'color': 'blue'},
    'electro': {'name': 'Electro', 'symbol': '⚡', 'color': 'purple'},
    'cryo': {'name': 'Cryo', 'symbol': '❄️', 'color': 'cyan'},
    'anemo': {'name': 'Anemo', 'symbol': '🌪️', 'color': 'green'},
    'geo': {'name': 'Geo', 'symbol': '🪨', 'color': 'yellow'},
}

# Elemental Reactions
REACTIONS = {
    'pyro_hydro': {'name': 'Vaporize', 'multiplier': 1.5, 'symbol': '💥'},
    'hydro_electro': {'name': 'Electrocharge', 'multiplier': 1.4, 'symbol': '⚡💧'},
    'electro_cryo': {'name': 'Superconduct', 'multiplier': 1.3, 'symbol': '❄️⚡'},
    'pyro_cryo': {'name': 'Melt', 'multiplier': 1.6, 'symbol': '🔥❄️'},
    'pyro_anemo': {'name': 'Swirl', 'multiplier': 1.2, 'symbol': '🌪️🔥'},
    'hydro_anemo': {'name': 'Swirl', 'multiplier': 1.2, 'symbol': '🌪️💧'},
}


# ASCII ART

def ascii_art_menang():
    """Tampilkan ASCII art pedang untuk kemenangan"""
    art = """
    
         |
         |
        /|\\
         |
         |
        / \\
       /   \\
      /     \\
     /_______\\
     |       |
     |       |
    _|_______|_
    
    """
    return art


def ascii_art_kalah():
    """Tampilkan ASCII art tengkorak untuk kekalahan"""
    art = """
    
       .-""""""-.
      /          \\
     |   oo       |
     |            |
     |   __       |
     |  (__)      |
      \\          /
       '._____.-'
        | | |
        | | |
       _| | |_
    
    """
    return art


# GAME CLASSES & SYSTEMS

class Pemain:
    def __init__(self, nama):
        self.nama = nama
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.characters = []  # List of characters owned
        self.active_team = []  # Active team (max 4 characters)
        self.artifacts = []  # Collected artifacts
        self.weapons = []  # Collected weapons
        
    def add_character(self, character):
        """Add character ke collection"""
        self.characters.append(character)
        
    def set_active_team(self, char_indices):
        """Set active team (max 4 characters)"""
        self.active_team = [self.characters[i] for i in char_indices[:4]]
        
    def can_use_element(self, element):
        """Check if any active team member has this element"""
        return any(char.element == element for char in self.active_team)
        
    def display_team(self):
        """Display active team"""
        if not self.active_team:
            return "No active team!"
        team_str = " | ".join([f"{char.name} {ELEMENTS[char.element]['symbol']} Lvl{char.level}" 
                               for char in self.active_team])
        return f"[Team: {team_str}]"


class Character:
    def __init__(self, name, element, rarity=4):
        self.name = name
        self.element = element  # 'pyro', 'hydro', 'electro', 'cryo', 'anemo', 'geo'
        self.rarity = rarity  # 4-star or 5-star
        self.level = 1
        self.exp = 0
        self.hp = 100 + (rarity * 10)
        self.max_hp = self.hp
        self.attack = 15 + (rarity * 5)
        self.energy = 0  # Energy untuk Ultimate
        self.max_energy = 100
        self.equipped_artifact = None
        self.equipped_weapon = None
        
    def normal_attack(self):
        """Normal attack damage"""
        damage = self.attack + random.randint(-3, 5)
        return damage
        
    def elemental_skill(self):
        """Elemental Skill damage"""
        damage = self.attack * 1.5 + random.randint(0, 10)
        return damage
        
    def elemental_burst(self):
        """Elemental Burst (Ultimate) - requires 100 energy"""
        if self.energy < 100:
            return 0
        self.energy = 0
        damage = self.attack * 2.5 + random.randint(10, 20)
        return damage
        
    def gain_energy(self, amount=20):
        """Gain energy"""
        self.energy = min(100, self.energy + amount)
        
    def display_info(self):
        element_info = ELEMENTS[self.element]
        rarity_display = "⭐" * self.rarity
        return f"{element_info['symbol']} {self.name} {rarity_display} | Lvl {self.level} | HP: {self.hp}/{self.max_hp} | Energy: {self.energy}/100"


class Musuh:
    def __init__(self, nama, hp, attack, defense, element='geo', exp_drop=30, gold_drop=20):
        self.nama = nama
        self.element = element
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.exp_drop = exp_drop
        self.gold_drop = gold_drop
        
    def display_status(self):
        element_info = ELEMENTS.get(self.element, {'symbol': '?'})
        return f"{element_info['symbol']} {self.nama} | HP: {self.hp}/{self.max_hp}"
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        return actual_damage


def battle_system(team, musuh, vibe=None):
    """Sistem pertarungan gaya Genshin Impact - Team-based dengan elemental reactions"""
    dram(apply_vibe(f"\n⚔️ = BATTLE START = ⚔️", vibe))
    party_str = " | ".join([f"{c.name} {ELEMENTS[c.element]['symbol']}" for c in team])
    dram(apply_vibe(f"Your Party: {party_str}", vibe))
    dram(apply_vibe(f"Enemy: {musuh.nama} {ELEMENTS[musuh.element]['symbol']}", vibe))
    time.sleep(1)
    
    current_char_idx = 0  # Current active character
    turn = 0
    last_element_used = None  # Track last element for reactions
    
    while any(char.hp > 0 for char in team) and musuh.hp > 0:
        turn += 1
        current_char = team[current_char_idx]
        
        dram(apply_vibe(f"\n➤ TURN {turn} ➤ {current_char.name}'s Turn", vibe))
        for i, char in enumerate(team):
            marker = "●" if i == current_char_idx else "○"
            dram(f"  {marker} {char.display_info()}")
        dram(f"  Enemy: {musuh.display_status()}")
        
        # Battle menu
        dram(apply_vibe("\n⚔️ Action Menu:", vibe))
        dram("1. Normal Attack")
        dram("2. Elemental Skill")
        if current_char.energy >= 100:
            dram("3. Elemental Burst (ULTIMATE) ⭐")
        dram(f"{3 if current_char.energy >= 100 else 4}. Switch Character")
        dram(f"{4 if current_char.energy >= 100 else 5}. Defend")
        
        action = get_input("Choose action: ", "1")
        
        damage = 0
        is_elemental = False
        
        # Action handling
        if action == '1':
            damage = current_char.normal_attack()
            dram(apply_vibe(f"{current_char.name} uses Normal Attack! Damage: {damage}", vibe))
            current_char.gain_energy(20)
            is_elemental = False
            
        elif action == '2':
            damage = current_char.elemental_skill()
            dram(apply_vibe(f"{current_char.name} uses Elemental Skill {ELEMENTS[current_char.element]['symbol']}! Damage: {damage}", vibe))
            current_char.gain_energy(30)
            is_elemental = True
            last_element_used = current_char.element
            
        elif action == '3' and current_char.energy >= 100:
            damage = current_char.elemental_burst()
            element_info = ELEMENTS[current_char.element]
            dram(apply_vibe(f"⭐ {current_char.name} uses ELEMENTAL BURST {element_info['symbol']}! CRITICAL DAMAGE: {damage}!", vibe))
            is_elemental = True
            last_element_used = current_char.element
            
        elif action in ['4', '5'] or (action == '3' and current_char.energy < 100):
            if 'witch' in action.lower() or action in ['4', '5']:
                # Switch or defend
                if action not in ['4', '5']:
                    dram(apply_vibe(f"Switched to next character!", vibe))
                else:
                    dram(apply_vibe(f"{current_char.name} is defending!", vibe))
                    current_char.gain_energy(25)
            damage = 0
        else:
            dram("Invalid action!")
            continue
        
        # Apply elemental reaction
        if is_elemental and last_element_used and last_element_used != musuh.element:
            reaction_key = f"{last_element_used}_{musuh.element}"
            reverse_key = f"{musuh.element}_{last_element_used}"
            
            if reaction_key in REACTIONS:
                reaction = REACTIONS[reaction_key]
                bonus_damage = int(damage * (reaction['multiplier'] - 1))
                damage += bonus_damage
                dram(apply_vibe(f"{reaction['symbol']} ELEMENTAL REACTION: {reaction['name']}! +{bonus_damage} bonus damage!", vibe))
            elif reverse_key in REACTIONS:
                reaction = REACTIONS[reverse_key]
                bonus_damage = int(damage * (reaction['multiplier'] - 1))
                damage += bonus_damage
                dram(apply_vibe(f"{reaction['symbol']} ELEMENTAL REACTION: {reaction['name']}! +{bonus_damage} bonus damage!", vibe))
        
        # Deal damage
        if damage > 0:
            actual_damage = musuh.take_damage(damage)
            dram(apply_vibe(f"💥 {musuh.nama} takes {actual_damage} damage!", vibe))
        
        # Check if enemy is defeated
        if musuh.hp <= 0:
            dram(apply_vibe(f"\n🎉 {musuh.nama} has been defeated!", vibe))
            # Reward all team members
            for char in team:
                char.exp += musuh.exp_drop
            return True
        
        # Enemy counterattack
        time.sleep(0.5)
        enemy_damage = musuh.attack + random.randint(-2, 3)
        actual_damage = max(1, enemy_damage - current_char.defense)
        current_char.hp -= actual_damage
        dram(apply_vibe(f"⚔️ {musuh.nama} counterattacks! {current_char.name} takes {actual_damage} damage!", vibe))
        
        # Check if character is defeated
        if current_char.hp <= 0:
            current_char.hp = 0
            dram(apply_vibe(f"💀 {current_char.name} has been defeated!", vibe))
            # Find next alive character
            alive_found = False
            for i in range(len(team)):
                if team[i].hp > 0:
                    current_char_idx = i
                    dram(apply_vibe(f"Switched to {team[i].name}!", vibe))
                    alive_found = True
                    break
            if not alive_found:
                dram(apply_vibe(f"All party members have been defeated!", vibe))
                return False
        
        # Move to next character
        current_char_idx = (current_char_idx + 1) % len(team)
        time.sleep(0.5)
    
    return musuh.hp <= 0


def get_starter_characters():
    """Dapatkan starter characters untuk role model"""
    characters = [
        Character("Amber", "pyro", rarity=4),
        Character("Barbara", "hydro", rarity=4),
        Character("Lisa", "electro", rarity=4),
        Character("Kaeya", "cryo", rarity=4),
        Character("Traveler", "anemo", rarity=5),
    ]
    return characters


def init_player_characters(player):
    """Initialize player dengan starter characters"""
    starters = get_starter_characters()
    for char in starters:
        player.add_character(char)
    # Set first team
    player.set_active_team([0, 1, 2, 3])  # First 4 characters


def display_character_selection(player):
    """Display dan pilih karakter untuk team"""
    dram("\n════════════════════════════════════")
    dram("🎭 CHARACTER SELECTION")
    dram("════════════════════════════════════")
    
    for i, char in enumerate(player.characters):
        element_info = ELEMENTS[char.element]
        rarity = "⭐" * char.rarity
        dram(f"{i+1}. {element_info['symbol']} {char.name} {rarity} - Lvl {char.level}")
    
    dram("\nSelect up to 4 characters for your team:")
    dram("(Enter numbers separated by comma, e.g., 1,2,3,4)")
    
    selection = get_input("Your selection: ", "1,2,3,4")
    try:
        indices = [int(x.strip()) - 1 for x in selection.split(',')]
        indices = [i for i in indices if 0 <= i < len(player.characters)][:4]
        player.set_active_team(indices)
        team_str = " | ".join([f"{c.name} {ELEMENTS[c.element]['symbol']}" for c in player.active_team])
        dram(apply_vibe(f"\nTeam set: {team_str}", None))
    except:
        dram("Invalid selection, using default team")
        player.set_active_team([0, 1, 2, 3])


def get_input(prompt, default=""):
    """Handle input dengan error handling untuk empty/EOF"""
    try:
        return input(prompt).strip()
    except EOFError:
        return default
    except KeyboardInterrupt:
        print("\n\nPermainan dibatalkan.")
        exit(0)


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


def lembah_coding(player, vibe=None):
    """Lembah Coding - Region 1 with elemental puzzle system"""
    dram(apply_vibe(f"\n{'='*50}", vibe))
    dram(apply_vibe("🌄 LEMBAH CODING - Digital Valley", vibe))
    dram(apply_vibe(f"{'='*50}", vibe))
    
    dram(apply_vibe(f"\n{player.nama}, Anda memasuki Lembah Coding yang dipenuhi bug digital.", vibe))
    dram(apply_vibe(f"Your active team: {player.display_team()}", vibe))
    time.sleep(1)
    
    # Encounter 1 - Elemental Requirement
    dram(apply_vibe("\n[Domain: Code Guardian's Challenge]", vibe))
    if not player.can_use_element('geo'):
        dram(apply_vibe("⚠️ This domain requires GEO element to enter!\nRecruit Geo users or you'll take penalty damage.", vibe))
    
    librarian = Musuh("Code Guardian", hp=40, attack=12, defense=4, element='geo', exp_drop=50, gold_drop=25)
    if not battle_system(player.active_team, librarian, vibe):
        dram(ascii_art_kalah())
        return False
    
    player.gold += librarian.gold_drop
    dram(apply_vibe("✨ Artifact obtained: Flower of Life +20 HP", vibe))
    
    time.sleep(1)
    
    # Branch - Elemental Puzzle Choice
    dram(apply_vibe("\n[Puzzle: Which path requires YOUR element?]", vibe))
    dram("1. Pyro Challenge (🔥) - Use fire elements")
    dram("2. Hydro Challenge (💧) - Use water elements")
    dram("3. Electro Challenge (⚡) - Use electricity elements")
    
    puzzle_choice = get_input("Choose your element path: ", "1")
    
    element_map = {'1': 'pyro', '2': 'hydro', '3': 'electro'}
    chosen_element = element_map.get(puzzle_choice, 'pyro')
    
    if player.can_use_element(chosen_element):
        dram(apply_vibe(f"✅ Your team has {ELEMENTS[chosen_element]['symbol']} users! Entering domain...", vibe))
        
        # Enemy varies by element choice
        enemies_by_element = {
            'pyro': Musuh("Inferno Construct", hp=45, attack=14, defense=5, element='hydro', exp_drop=60, gold_drop=30),
            'hydro': Musuh("Frost Abyss", hp=45, attack=14, defense=5, element='cryo', exp_drop=60, gold_drop=30),
            'electro': Musuh("Thunder Sentinel", hp=45, attack=14, defense=5, element='electro', exp_drop=60, gold_drop=30),
        }
        enemy = enemies_by_element[chosen_element]
        
    else:
        dram(apply_vibe(f"❌ No {ELEMENTS[chosen_element]['symbol']} users! Taking damage + easier enemy...", vibe))
        for char in player.active_team:
            char.hp = max(1, char.hp - 10)
        enemy = Musuh("Weakened Bug", hp=25, attack=8, defense=2, element='geo', exp_drop=30, gold_drop=15)
    
    if not battle_system(player.active_team, enemy, vibe):
        dram(ascii_art_kalah())
        return False
    
    player.gold += enemy.gold_drop
    time.sleep(1)
    
    # Final Boss
    dram(apply_vibe("\n" + "="*50, vibe))
    dram(apply_vibe("👹 BOSS: Algoritma Jahat - The Glitch Lord", vibe))
    dram(apply_vibe("="*50, vibe))
    
    boss = Musuh("Algoritma Jahat", hp=120, attack=18, defense=8, element='geo', exp_drop=200, gold_drop=100)
    
    if battle_system(player.active_team, boss, vibe):
        dram(ascii_art_menang())
        dram(apply_vibe(f"\n🎉 Congrats! You defeated {boss.nama}!", vibe))
        dram(apply_vibe(f"Rewards: {boss.exp_drop} EXP, {boss.gold_drop} Gold", vibe))
        player.gold += boss.gold_drop
        return True
    else:
        dram(ascii_art_kalah())
        return False


def gunung_bug(player, vibe=None):
    """Gunung Bug - Region 2 with different element mechanics"""
    dram(apply_vibe(f"\n{'='*50}", vibe))
    dram(apply_vibe("⛰️ GUNUNG BUG - Peak of Bugs", vibe))
    dram(apply_vibe(f"{'='*50}", vibe))
    
    dram(apply_vibe(f"\n{player.nama}, Anda mulai mendaki Gunung Bug.", vibe))
    dram(apply_vibe(f"Your active team: {player.display_team()}", vibe))
    time.sleep(1)
    
    # Encounter 1
    dram(apply_vibe("\n[Encounter: Bug Swarm]", vibe))
    bug_swarm = Musuh("Giant Bug Swarm", hp=50, attack=13, defense=3, element='pyro', exp_drop=55, gold_drop=28)
    if not battle_system(player.active_team, bug_swarm, vibe):
        dram(ascii_art_kalah())
        return False
    
    player.gold += bug_swarm.gold_drop
    
    time.sleep(1)
    
    # Encounter 2 - Cryo specific challenge
    dram(apply_vibe("\n[Encounter: Frozen Peak]", vibe))
    if player.can_use_element('cryo'):
        dram(apply_vibe("❄️ Perfect! Your Cryo team can unfreeze barriers!", vibe))
        frozen_enemy = Musuh("Frost Guardian", hp=50, attack=15, defense=6, element='pyro', exp_drop=65, gold_drop=35)
    else:
        dram(apply_vibe("⚠️ No Cryo users. This will be harder...", vibe))
        for char in player.active_team:
            char.hp = max(1, char.hp - 15)
        frozen_enemy = Musuh("Frost Guardian", hp=40, attack=12, defense=4, element='pyro', exp_drop=40, gold_drop=20)
    
    if not battle_system(player.active_team, frozen_enemy, vibe):
        dram(ascii_art_kalah())
        return False
    
    player.gold += frozen_enemy.gold_drop
    
    time.sleep(1)
    
    # Final Boss - Harder than Lembah
    dram(apply_vibe("\n" + "="*50, vibe))
    dram(apply_vibe("👹 BOSS: Giant Bug Godking - Sovereign of Bugs", vibe))
    dram(apply_vibe("="*50, vibe))
    
    boss = Musuh("Giant Bug Godking", hp=160, attack=20, defense=10, element='electro', exp_drop=250, gold_drop=150)
    
    if battle_system(player.active_team, boss, vibe):
        dram(ascii_art_menang())
        dram(apply_vibe(f"\n🎉 EPIC VICTORY! You defeated {boss.nama}!", vibe))
        dram(apply_vibe(f"Rewards: {boss.exp_drop} EXP, {boss.gold_drop} Gold", vibe))
        player.gold += boss.gold_drop
        return True
    else:
        dram(ascii_art_kalah())
        return False


def game_utama():
    """Main Game Loop - Genshin Impact Style"""
    dram(apply_vibe("╔════════════════════════════════════╗", None))
    dram(apply_vibe("║  🎮 GENSHIN ADVENTURE SIMULATOR 🎮 ║", None))
    dram(apply_vibe("╚════════════════════════════════════╝", None))
    
    nama = get_input("📝 Enter your Traveler name: ", "Traveler")
    if not nama:
        nama = "Traveler"
    
    # Vibe selection
    dram("\n🎭 Select Narration Style:")
    dram("1. Dramatis (🔥 Intense & Epic)")
    dram("2. Misterius (~ Dark & Mysterious)")
    dram("3. Kocak (😂 Funny & Humorous)")
    dram("4. Santai (🤐 Chill & Relaxed)")
    dram("5. Netral (⚪ Standard)")
    
    vibe_in = get_input("Choose vibe: ", "5")
    vibe_map = {'1': 'dramatis', '2': 'misterius', '3': 'kocak', '4': 'santai', '5': ''}
    vibe = vibe_map.get(vibe_in, '')
    
    # Initialize player
    player = Pemain(nama)
    init_player_characters(player)
    
    dram(apply_vibe(f"\n✨ Welcome, {nama}! Your adventure begins!", vibe))
    dram(apply_vibe("You have been granted control of these adventurers:", vibe))
    for i, char in enumerate(player.characters):
        element_info = ELEMENTS[char.element]
        rarity = "⭐" * char.rarity
        dram(f"  {i+1}. {element_info['symbol']} {char.name} {rarity}")
    
    # Character Selection
    display_character_selection(player)
    time.sleep(1)
    
    # Story - Choose domain
    while True:
        dram(apply_vibe("\n" + "="*50, vibe))
        dram(apply_vibe("🗺️ SELECT REGION", vibe))
        dram(apply_vibe("="*50, vibe))
        dram("1. Lembah Coding (Valley) - Medium Difficulty")
        dram("2. Gunung Bug (Mountain) - Higher Difficulty")
        dram("3. Change Team")
        
        pilihan = get_input("Choose your region (1/2/3): ", "1")
        
        if pilihan == '3':
            display_character_selection(player)
            continue
        elif pilihan == '1':
            lembah_coding(player, vibe)
            break
        elif pilihan == '2':
            gunung_bug(player, vibe)
            break
        else:
            dram(apply_vibe("Invalid choice!", vibe))


if __name__ == "__main__":
    while True:
        game_utama()
        lagi = get_input("\nMain lagi? (y/n): ", "n").lower()
        if lagi != 'y' and lagi != 'yes':
            dram("Terima kasih telah bermain! Sampai jumpa.\n")
            break