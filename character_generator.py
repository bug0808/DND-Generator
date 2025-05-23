import random
from spell_lists import all_spells
from spell_slots import ALL_SPELL_SLOTS

# Can be part of the lightweight character generator or full character generator
# This code generates a character with a set of stats based on the class chosen.
def generate_stats_for_class(class_name):
    stat_profiles = {
        "Wizard": ["INT", "CON", "DEX", "WIS", "CHA", "STR"],
        "Fighter": ["STR", "CON", "DEX", "WIS", "CHA", "INT"],
        "Rogue": ["DEX", "INT", "CON", "WIS", "CHA", "STR"],
        "Cleric": ["WIS", "CON", "STR", "CHA", "DEX", "INT"],
        "Bard": ["CHA", "DEX", "CON", "INT", "WIS", "STR"],
        "Ranger": ["DEX", "WIS", "CON", "STR", "CHA", "INT"],
        "Paladin": ["STR", "CHA", "CON", "WIS", "DEX", "INT"],
        "Monk": ["DEX", "WIS", "CON", "STR", "CHA", "INT"],
        "Druid": ["WIS", "CON", "DEX", "INT", "CHA", "STR"],
        "Warlock": ["CHA", "CON", "DEX", "WIS", "INT", "STR"],
        "Sorcerer": ["CHA", "CON", "DEX", "WIS", "INT", "STR"],
        "Barbarian": ["STR", "CON", "DEX", "WIS", "CHA", "INT"],
        "Artificer": ["INT", "CON", "DEX", "WIS", "CHA", "STR"]
    }

    if class_name not in stat_profiles:
        raise ValueError("Unknown class name")

    ordered_stats = stat_profiles[class_name]
    point_array = [15, 14, 13, 10, 8, 8]

    final_stats = {stat: point_array[i] for i, stat in enumerate(ordered_stats)}

    return final_stats


stat_profiles = {
    "Wizard": ["INT", "CON", "DEX", "WIS", "CHA", "STR"],
    "Fighter": ["STR", "CON", "DEX", "WIS", "CHA", "INT"],
    "Rogue": ["DEX", "INT", "CON", "WIS", "CHA", "STR"],
    "Cleric": ["WIS", "CON", "STR", "CHA", "DEX", "INT"],
    "Bard": ["CHA", "DEX", "CON", "INT", "WIS", "STR"],
    "Ranger": ["DEX", "WIS", "CON", "STR", "CHA", "INT"],
    "Paladin": ["STR", "CHA", "CON", "WIS", "DEX", "INT"],
    "Monk": ["DEX", "WIS", "CON", "STR", "CHA", "INT"],
    "Druid": ["WIS", "CON", "DEX", "INT", "CHA", "STR"],
    "Warlock": ["CHA", "CON", "DEX", "WIS", "INT", "STR"],
    "Sorcerer": ["CHA", "CON", "DEX", "WIS", "INT", "STR"],
    "Barbarian": ["STR", "CON", "DEX", "WIS", "CHA", "INT"],
    "Artificer": ["INT", "CON", "DEX", "WIS", "CHA", "STR"]
}

class_table = {
    range(1, 8): "Barbarian",
    range(8, 15): "Bard",
    range(15, 21): "Cleric",
    range(22, 29): "Druid",
    range(29, 36): "Fighter",
    range(36, 43): "Monk",
    range(43, 50): "Paladin",
    range(50, 57): "Ranger",
    range(57, 64): "Rogue",
    range(64, 71): "Sorcerer",
    range(71, 78): "Warlock",
    range(78, 85): "Wizard",
    range(85, 92): "Artificer",
    range(92, 101): "Dealer's Choice"
}

subclass_table = {
    "Barbarian": ["Ancestral Guardian", "Battlerager", "Beast", "Berserker","Giant", "Storm Herald", "Totem Warrior", "Wild Magic", "Zealot"],
    "Bard": ["College of Creation", "College of Eloquence","College of Glamour", "College of Lore", "College of Spirits", "College of Swords", "College of Valor", "College of Whispers"],
    "Cleric": ["Arcana Domain", "Death Domain", "Forge Domain", "Grave Domain", "Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Order Domain", "Peace Domain", "Tempest Domain", "Trickery Domain","Twilight Domain", "War Domain"],
    "Druid": ["Circle of Dreams", "Circle of Spores", "Circle of Stars", "Circle of the Moon", "Circle of the Shepherd", "Circle of Wildfire", "Circle of the Land"],
    "Fighter": ["Arcane Archer", "Banneret", "Battle Master", "Cavalier", "Champion", "Echo Knight", "Eldritch Knight", "Rune Knight", "Samurai", "Psi Warrior"],
    "Monk": ["Astral Self", "Drunken Master", "Four Elements", "Kensei", "Long Death", "Mercy", "Open Hand", "Shadow", "Sun Soul", "Ascendant Dragon"],
    "Paladin": ["Oath of Ancients ", "Oath of Crown", "Oath of Devotion", "Oath of Glory", "Oath of Redemption", "Oath of Vengeance", "Oath of Conquest", "Oathbreaker", "Oath of the Watchers"],
    "Ranger": ["Beast Master", "Gloom Stalker", "Horizon Walker", "Hunter", "Monster Slayer", "Swarmkeeper", "Fey Wanderer", "Drakewarden"],
    "Rogue": ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Phantom", "Scout", "Soulknife", "Swashbuckler", "Thief"],
    "Sorcerer":["Abberant Mind", "Clockwork Soul", "Divine Soul", "Draconic Bloodline", "Lunar Sorcery", "Shadow Magic", "Storm Sorcery", "Wild Magic"],
    "Warlock": ["The Archfey", "The Celestial", "The Fathomless", "The Fiend", "The Genie", "The Great Old One", "The Hexblade", "The Undead", "The Undying"],
    "Wizard": ["Abjuration", "Bladesinging", "Chronurgy", "Conjuration", "Divination", "Enchantment", "Evocation", "Graviturgy", "Illusion", "Necromancy", "Order of Scribes", "Transmutation", "War Magic"],
    "Artificer": ["Alchemist", "Armorer", "Artillerist", "Battle Smith"]
}


# Define a Common race table
race_table_common = {
    range(1, 11): "Human",
    range(11, 21): "Elf",
    range(21, 31): "Dwarf",
    range(31, 41): "Halfling",
    range(41, 51): "Half-Orc",
    range(51, 61): "Gnome",
    range(61, 71): "Half-Elf",
    range(71, 81): "Dragonborn",
    range(81, 91): "Tiefling",
    range(91, 100): "Exotic"
}

race_table_exotic = {
    range(1, 11): "Warforged",
    range(11, 21): "Tortle",
    range(21, 31): "Aasimar",
    range(31, 41): "Firbolg",
    range(41, 51): "Genasi",
    range(51, 61): "Goliath",
    range(61, 71): "Kobold",
    range(71, 81): "Tabaxi",
    range(81, 91): "Triton",
    range(91, 100): "Kenku"
}

def roll_subrace(race):
    """Rolls for a subrace if the race has subraces, otherwise returns the race itself."""
    if race in subraces:
        return random.choice(subraces[race])
    return race


# Subrace options for races with subraces
subraces = {
    "Elf": ["High Elf", "Wood Elf", "Dark Elf (Drow)"],
    "Dwarf": ["Hill Dwarf", "Mountain Dwarf", "Duergar"],
    "Half-Elf": ["High Elf Heritage", "Wood Elf Heritage", "Dark Elf (Drow) Heritage"],
    "Tiefling": ["Bloodline of Asmodeus", "Bloodline of Mephistopheles", "Bloodline of Zariel", "Bloodline of Dispater", "Bloodline of Levistus", "Bloodline of Fierna", "Bloodline of Glasya", "Bloodline of Mammon", "Bloodline of Baalzebul"],
    "Dragonborn": ["Black Dragonborn", "Blue Dragonborn", "Brass Dragonborn", "Bronze Dragonborn", "Copper Dragonborn", "Gold Dragonborn", "Green Dragonborn", "Red Dragonborn", "Silver Dragonborn", "White Dragonborn"],
    "Halfling": ["Lightfoot Halfling", "Stout Halfling"],
    "Gnome": ["Forest Gnome", "Rock Gnome", "Deep Gnome"],
    "Genasi": ["Air Genasi", "Earth Genasi", "Fire Genasi", "Water Genasi"]
}


 
#TODO: fix bonuses 
# Racial bonuses including subraces
racial_bonuses = {
    # Humans have no subraces
    "Human": {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1},

    # Elves
    "High Elf": {"DEX": 2, "INT": 1},
    "Wood Elf": {"DEX": 2, "WIS": 1},
    "Dark Elf (Drow)": {"DEX": 2, "CHA": 1},

    # Dwarves
    "Hill Dwarf": {"CON": 2, "WIS": 1},
    "Mountain Dwarf": {"STR": 2, "CON": 2},
    "Duergar": {"STR": 1, "CON": 2},

    # Halflings
    "Lightfoot Halfling": {"DEX": 2, "CHA": 1},
    "Stout Halfling": {"DEX": 2, "CON": 1},

    # Gnomes
    "Forest Gnome": {"DEX": 1, "INT": 2},
    "Rock Gnome": {"INT": 2, "CON": 1},
    "Deep Gnome": {"DEX": 1, "INT": 2}, 

    # Half-Elf (heritages)
    "High Elf Heritage": {"CHA": 2, "INT": 1, "DEX": 1},
    "Wood Elf Heritage": {"CHA": 2, "WIS": 1, "DEX": 1},
    "Dark Elf (Drow) Heritage": {"CHA": 2, "DEX": 1, "CON": 1},  

    # Dragonborn
    "Black Dragonborn": {"STR": 2, "CHA": 1},
    "Blue Dragonborn": {"STR": 2, "CHA": 1},
    "Brass Dragonborn": {"STR": 2, "CHA": 1},
    "Bronze Dragonborn": {"STR": 2, "CHA": 1},
    "Copper Dragonborn": {"STR": 2, "CHA": 1},
    "Gold Dragonborn": {"STR": 2, "CHA": 1},
    "Green Dragonborn": {"STR": 2, "CHA": 1},
    "Red Dragonborn": {"STR": 2, "CHA": 1},
    "Silver Dragonborn": {"STR": 2, "CHA": 1},
    "White Dragonborn": {"STR": 2, "CHA": 1},

    # Genasi
    "Air Genasi": {"DEX": 1, "CON": 2},
    "Earth Genasi": {"STR": 1, "CON": 2},
    "Fire Genasi": {"CON": 2, "INT": 1},
    "Water Genasi": {"CON": 2, "WIS": 1},

    # Tiefling
    "Bloodline of Asmodeus": { "INT": 1, "CHA": 2},
    "Bloodline of Mephistopheles": {"CHA": 2, "INT": 1},
    "Bloodline of Zariel": {"STR": 1, "CHA": 2},
    "Bloodline of Dispater": {"DEX": 1, "CHA": 2,},
    "Bloodline of Levistus": {"CON": 1, "CHA": 2},
    "Bloodline of Fierna": {"WIS": 1, "CHA": 2},
    "Bloodline of Glasya": {"DEX": 1, "CHA": 2},
    "Bloodline of Mammon": {"INT": 1, "CHA": 2},
    "Bloodline of Baalzebul": {"INT": 1, "CHA": 2 },


    # Other races (no subraces)
    "Half-Orc": {"STR": 2, "CON": 1},
    "Warforged": {"CON": 2, "STR": 1}, #Assuming it gets STR Bonus
    "Tortle": {"CON": 2, "WIS": 1}, # increase one score by 2 and increase a different score by 1, or increase three different scores by 1
    "Aasimar": {"CHA": 2, "WIS": 1}, # increase one score by 2 and increase a different score by 1, or increase three different scores by 1
    "Firbolg": {"WIS": 2, "STR": 1}, # increase one score by 2 and increase a different score by 1, or increase three different scores by 1
    "Genasi": {"CON": 2, "DEX": 1}, # increase one score by 2 and increase a different score by 1, or increase three different scores by 1
    "Goliath": {"STR": 2, "CON": 1}, # increase one score by 2 and increase a different score by 1, or increase three different scores by 1
    "Kobold": {"DEX": 2, "CHA": 1}, # increase one score by 2 and increase a different score by 1, or increase three different scores by 1
    "Tabaxi": {"DEX": 2, "CHA": 1}, # Volos Guide to Monsters
    "Triton": {"STR": 1, "CON": 1, "WIS": 1}, # Volos Guide to Monsters
    "Kenku": {"DEX": 2, "WIS": 1}, # Volos Guide to Monsters
    # For base races (if subrace not chosen)
    "Elf": {"DEX": 2},
    "Dwarf": {"CON": 2},
    "Halfling": {"DEX": 2},
    "Gnome": {"INT": 2},
    "Half-Elf": {"CHA": 2, "DEX": 1, "CON": 1},
    "Dragonborn": {"STR": 2, "CHA": 1},
    "Genasi": {"CON": 2},
}

#TODO: Edit to fit the common backstory table
#TODO: Add more backstories
#TODO CHANGE BACKSTORIES TO BE INDIVIDUAL TABLES TIED TO A BACKGROUND NOT THE OTHER WAY AROUND
# Define a sample backstory table
backstory_table = {
    1: ("Escaped a noble family scandal; hiding under a false identity", "Charlatan"),
    2: ("Grew up in a traveling circus as an acrobat and storyteller", "Entertainer"),
    3: ("Was a squire to a fallen paladin; now seeks redemption", "Acolyte or Knight of the Order"),
    4: ("Deserted the army after a tragic massacre", "Soldier"),
    5: ("Spent a decade as a librarian in a ruined temple of knowledge", "Sage"),
    6: ("Ex-convict turned bounty hunter", "Criminal or Urban Bounty Hunter"),
    7: ("Born with a celestial birthmark believed to be an omen", "Acolyte or Haunted One"),
    8: ("Ex-cultist turned truth-seeker", "Hermit or Acolyte"),
    9: ("Ran a shady potion shop; wants to go “legit”", "Guild Artisan or Charlatan"),
    10: ("Was shipwrecked as a child and raised by coastal druids", "Hermit or Far Traveler"),
    # entries 11–50 similar pattern 
}

#SPELLS




def get_npc_spells(char_class, char_level):
    npc_spells = {}
    spell_slots = ALL_SPELL_SLOTS.get(char_class, {}).get(char_level, {})
    # print(spell_slots)
    # Warlock uses a different slot structure
    if char_class == "Warlock":
        slot_info = spell_slots
        max_spell_level = slot_info.get("slot_level", 0)
        slots = slot_info.get("slots", 0)
        # Find all spells up to max_spell_level
        available_spells = [spell for spell, info in all_spells.items()
                            if char_class in info['classes'] and 1 <= info['level'] <= max_spell_level]
        # Pick up to 'slots' spells
        selected_spells = random.sample(available_spells, min(slots, len(available_spells)))
        return {max_spell_level: selected_spells}

    # For other classes
    for lvl, num_slots in spell_slots.items():
        if lvl == 0:  # Cantrips
            # Find all cantrips for this class
            cantrips = [spell for spell, info in all_spells.items()
                        if char_class in info['classes'] and info['level'] == 0]
            npc_spells[0] = random.sample(cantrips, min(num_slots, len(cantrips)))
        else:
            # Find all spells of this level for this class
            spells = [spell for spell, info in all_spells.items()
                      if char_class in info['classes'] and info['level'] == lvl]
            npc_spells[lvl] = random.sample(spells, min(num_slots, len(spells)))

    return npc_spells


def get_from_table(roll, table):
    for key_range, value in table.items():
        if roll in key_range:
            return value
    return None


def generate_stats_with_race(class_name, race_name, subrace):
    if class_name not in stat_profiles:
        print(class_name)
        raise ValueError("Unknown class name")
    if subrace not in racial_bonuses:
        print(subrace)
        raise ValueError("Unknown subrace") 

    # if race_name not in racial_bonuses:
    #     print(race_name)
    #     raise ValueError("Unknown race name")

    ordered_stats = stat_profiles[class_name]
    # Generate a randomized point array by simulating rolling 4d6 drop lowest for each stat
    def roll_stat():
        rolls = [random.randint(1, 6) for _ in range(4)]
        # print(sum(sorted(rolls)[1:]))
        return sum(sorted(rolls)[1:])  # Drop the lowest

    point_array = sorted([roll_stat() for _ in range(6)], reverse=True)
    # Base stats from rolls
    base_stats = {stat: point_array[i] for i, stat in enumerate(ordered_stats)}

    # Apply racial bonuses
    for stat, bonus in racial_bonuses[subrace].items():
        base_stats[stat] += bonus

    return base_stats

def ability_score_increase(stats, char_level):
    # Ability Score Increases at 4, 8, 12, 16, 19
    asi_levels = [4, 8, 12, 16, 19]
    for lvl in asi_levels:
        if char_level >= lvl:
            # Find two stats below 20, prioritize highest stats first
            stats_below_20 = sorted([(k, v) for k, v in stats.items() if v < 20], key=lambda x: -x[1])
            if len(stats_below_20) == 0:
                break  # All stats at 20
            elif len(stats_below_20) == 1:
                stats[stats_below_20[0][0]] = min(20, stats_below_20[0][1] + 2)
            else:
                stats[stats_below_20[0][0]] = min(20, stats_below_20[0][1] + 1)
                stats[stats_below_20[1][0]] = min(20, stats_below_20[1][1] + 1)


def generate_npc():
    class_roll = random.randint(1, 100)
    print(f"Class Roll: {class_roll}")
    race_roll = random.randint(1, 100)
    backstory_roll = random.randint(1, 10)

    char_class = get_from_table(class_roll, class_table)
    print(f"Class: {char_class}")
    race = get_from_table(race_roll, race_table_common)
    print(race)
    if race == "Exotic":
        race = get_from_table(random.randint(1, 100), race_table_exotic)
        print(race)
    subrace = roll_subrace(race)
    # print(subrace)
    backstory, background = backstory_table[backstory_roll]

    if char_class == "Dealer's Choice":
        char_class = random.choice(list(stat_profiles.keys()))

    stats = generate_stats_with_race(char_class, race, subrace)
    char_level = random.randint(1, 20)

    match char_class:
        case "Wizard":
            if char_level > 2:
                subclass = random.choice(subclass_table["Wizard"])
            ability_score_increase(stats, char_level)
        case "Sorcerer":
            if char_level > 2:
                subclass = random.choice(subclass_table["Sorcerer"])
            ability_score_increase(stats, char_level)
        case "Warlock":
            subclass = random.choice(subclass_table["Warlock"])
            ability_score_increase(stats, char_level)
        case "Cleric":
            subclass = random.choice(subclass_table["Cleric"])
            ability_score_increase(stats, char_level)
        case "Druid":
            if char_level > 2:
                subclass = random.choice(subclass_table["Druid"])
            ability_score_increase(stats, char_level)
        case "Paladin":
            if char_level > 3:
                subclass = random.choice(subclass_table["Paladin"])
            ability_score_increase(stats, char_level)
        case "Ranger":
            if char_level > 3:
                subclass = random.choice(subclass_table["Ranger"])
            ability_score_increase(stats, char_level)
        case "Fighter":
            if char_level > 3:
                subclass = random.choice(subclass_table["Fighter"])
            ability_score_increase(stats, char_level)
        case "Monk":
            if char_level > 3:
                subclass = random.choice(subclass_table["Monk"])
            ability_score_increase(stats, char_level)
        case "Barbarian":
            if char_level > 3:
                subclass = random.choice(subclass_table["Barbarian"])
            ability_score_increase(stats, char_level)
        case "Rogue":
            if char_level > 3:
                subclass = random.choice(subclass_table["Rogue"])
            ability_score_increase(stats, char_level)
        case "Bard":
            if char_level > 3:
                subclass = random.choice(subclass_table["Bard"])
            ability_score_increase(stats, char_level)
        case "Artificer":
            if char_level > 3:
                subclass = random.choice(subclass_table["Artificer"])
            ability_score_increase(stats, char_level)
        case _:
            pass  # Placeholder for class-specific features

    return {
        "Name": f"NPC_{random.randint(1, 1000)}",  # Placeholder for name generation
        "Level": char_level,
        "Class": char_class,
        "Subclass": subclass if 'subclass' in locals() else None,
        "Race": race,
        "Subrace": subrace,
        "Stats": stats,
        "Backstory": backstory,
        "Background": background,
        "Spells": get_npc_spells(char_class, char_level) if char_class in ALL_SPELL_SLOTS else None,
    }

# Generate example NPC
n = generate_npc()
print(n)
#TODO: Add a way to save the generated NPC to a file
#TODO: Add a way to load the generated NPC from a file
#TODO: Add a way to edit the generated NPC
#TODO: Add a way to delete the generated NPC
#TODO: Add a way to view the generated NPC
#TODO: Change the way stats are displayed to follow D&D Conventions
#TODO: Add backstory stats and proficiencies
#TODO: Maybe add a chatgpt wrapper to allow for more complex backstories
#TODO: Items and equipment
#TODO: SUbclasses that add spells to character
#TODO: FEATS
#TODO: Add a way to generate a full character sheet
#TODO: Factions and Guilds
#TODO: FULL ADVENTURE GENERATOR