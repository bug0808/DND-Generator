import random
import json
import os
import tkinter as tk
from tkinter import ttk

# Helper to load JSON from the data directory
def load_json(filename):
    with open(os.path.join("data", filename), "r", encoding="utf-8") as f:
        return json.load(f)

all_spells = load_json("all_spells.json")
ALL_SPELL_SLOTS = load_json("spell_slots.json")
proficiencies = load_json("proficiencies.json")
backstories = load_json("backstories.json")
feats = load_json("feats.json")


# This code is part of a character generator for Dungeons & Dragons 5th Edition.

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

def get_npc_spells(char_class, char_level):
    npc_spells = {}
    spell_slots = ALL_SPELL_SLOTS.get(char_class, {}).get(str(char_level), {})
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
        lvl_int = int(lvl)
        if lvl_int == 0:  # Cantrips
            cantrips = [spell for spell, info in all_spells.items()
                        if char_class in info['classes'] and info['level'] == 0]
            if cantrips:
                npc_spells[0] = random.sample(cantrips, min(num_slots, len(cantrips)))
        else:
            spells = [spell for spell, info in all_spells.items()
                      if char_class in info['classes'] and info['level'] == lvl_int]
            if spells:
                npc_spells[lvl_int] = random.sample(spells, min(num_slots, len(spells)))

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

def ability_score_increase_or_feat(stats, char_level, feats_taken=None):
    # Ability Score Increases at 4, 8, 12, 16, 19
    asi_levels = [4, 8, 12, 16, 19]
    if feats_taken is None:
        feats_taken = []
    for lvl in asi_levels:
        if char_level >= lvl:
            # 70% chance for stat increase, 30% for feat (adjust as desired)
            if random.random() < 0.3:
                feat = choose_random_feat(stats)
                if feat and feat["name"] not in feats_taken:
                    feats_taken.append(feat["name"])
                    # Apply stat increase if the feat grants one
                    if "stat_increase_choice" in feat:
                        options = feat["stat_increase_choice"]["options"]
                        stat = random.choice(options)
                        amount = feat["stat_increase_choice"]["amount"]
                        stats[stat] = min(20, stats.get(stat, 0) + amount)
                    # You could add more logic here to apply other feat effects
                    continue  # Skip normal stat increase if feat is taken
            # Stat increase (as before)
            stats_below_20 = sorted([(k, v) for k, v in stats.items() if v < 20], key=lambda x: -x[1])
            if len(stats_below_20) == 0:
                break  # All stats at 20
            elif len(stats_below_20) == 1:
                stats[stats_below_20[0][0]] = min(20, stats_below_20[0][1] + 2)
            else:
                stats[stats_below_20[0][0]] = min(20, stats_below_20[0][1] + 1)
                stats[stats_below_20[1][0]] = min(20, stats_below_20[1][1] + 1)
    return feats_taken

def get_class_skill_proficiencies(char_class):
    """Return a list of skill proficiencies for the given class, randomly chosen as per class rules."""
    class_prof = proficiencies["Classes"].get(char_class, {})
    skills_info = class_prof.get("skills", {})
    num = skills_info.get("choose", 0)
    options = skills_info.get("from", [])
    if num and options:
        return random.sample(options, min(num, len(options)))
    return []

def get_background_skill_proficiencies(background):
    """Return a list of skill proficiencies for the given background."""
    skills = []
    for skill, info in proficiencies["Skills"].items():
        if "Backgrounds" in info and background in info["Backgrounds"]:
            skills.append(skill)
    return skills

def choose_random_feat(stats):
    """Choose a random feat that meets prerequisites (very basic check)."""
    # Only check stat prerequisites for now
    available_feats = []
    for feat in feats:
        prereqs = feat.get("prerequisite", [])
        meets_prereq = True
        for prereq in prereqs:
            # Check for stat prerequisites like "Strength 13 or higher"
            if "13 or higher" in prereq:
                for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
                    if stat in prereq and stats.get(stat, 0) < 13:
                        meets_prereq = False
            # Add more checks as needed for other types of prerequisites
        if meets_prereq:
            available_feats.append(feat)
    if available_feats:
        return random.choice(available_feats)
    return None

def get_class_tool_proficiencies(char_class):
    """Return a list of tool proficiencies for the given class, randomly chosen as per class rules."""
    class_prof = proficiencies["Classes"].get(char_class, {})
    tools_info = class_prof.get("tools", {})
    profs = []
    # Add fixed tools
    profs.extend(tools_info.get("fixed", []))
    # Handle "choose" from a list of tags/groups or a single group
    choose = tools_info.get("choose", 0)
    from_ = tools_info.get("from", [])
    if choose and from_:
        # If from_ is a string, treat as a single group/tag
        if isinstance(from_, str):
            from_ = [from_]
        # Gather all tool names that match any tag/group in from_
        tool_options = []
        for tool_name, tool_info in proficiencies["Tools"].items():
            if "Tags" in tool_info and any(tag in tool_info["Tags"] for tag in from_):
                tool_options.append(tool_name)
        if tool_options:
            profs.extend(random.sample(tool_options, min(choose, len(tool_options))))
    return profs

def get_background_tool_proficiencies(background):
    """Return a list of tool proficiencies for the given background, handling group/tag choices."""
    tools = []
    bg_obj = proficiencies["Backgrounds"].get(background, {})
    tool_choices = bg_obj.get("tool_choices", 0)
    tool_groups = bg_obj.get("tools", [])

    # If tool_choices is set and there are group entries, pick only that many
    if tool_choices and tool_groups:
        # Gather all possible tool options from the listed groups/tags
        possible_tools = []
        for entry in tool_groups:
            # If entry is a group/tag, gather all tools with that tag
            group_tools = [tool for tool, info in proficiencies["Tools"].items()
                           if "Tags" in info and entry in info["Tags"]]
            if group_tools:
                possible_tools.extend(group_tools)
            else:
                # If entry is a specific tool, just add it
                possible_tools.append(entry)
        # Avoid duplicates and already-chosen tools
        possible_tools = list(set(possible_tools))
        if len(possible_tools) <= tool_choices:
            tools.extend(possible_tools)
        else:
            tools.extend(random.sample(possible_tools, tool_choices))
    else:
        # If no choices, just add all listed tools (for backgrounds with fixed tools)
        for entry in tool_groups:
            # If entry is a group/tag, add one random tool from that group
            group_tools = [tool for tool, info in proficiencies["Tools"].items()
                           if "Tags" in info and entry in info["Tags"]]
            if group_tools:
                tools.append(random.choice(group_tools))
            else:
                tools.append(entry)
    return tools

def get_background_languages(background):
    bg = proficiencies["Backgrounds"].get(background, {})
    chosen_languages = []
    all_languages = proficiencies.get("Languages", {})

    # Fixed languages (if any, and not tags or "One/Two of your choice")
    for lang in bg.get("languages", []):
        if lang in ["Common", "Exotic"]:
            continue
        if lang == "One of your choice":
            # Pick one language not already chosen
            pool = [l for l in all_languages if l not in chosen_languages]
            if pool:
                choice = random.choice(pool)
                if choice not in chosen_languages:
                    chosen_languages.append(choice)
            continue
        if lang == "Two of your choice":
            # Pick two languages not already chosen
            pool = [l for l in all_languages if l not in chosen_languages]
            picks = []
            if len(pool) >= 2:
                picks = random.sample(pool, 2)
            else:
                picks = pool
            for pick in picks:
                if pick not in chosen_languages:
                    chosen_languages.append(pick)
            continue
        if lang not in chosen_languages:
            chosen_languages.append(lang)

    # Handle language choices by tag
    num_choices = bg.get("languages_choices", 0)
    tags = [tag for tag in bg.get("languages", []) if tag in ["Common", "Exotic"]]
    if num_choices and tags:
        language_pool = [
            lang for lang, info in all_languages.items()
            if "Tags" in info and any(tag in info["Tags"] for tag in tags)
        ]
        language_pool = [l for l in language_pool if l not in chosen_languages]
        if len(language_pool) >= num_choices:
            chosen_languages += random.sample(language_pool, num_choices)
        else:
            chosen_languages += language_pool

    # Remove any duplicates just in case
    return list(dict.fromkeys(chosen_languages))

def get_race_languages(race, subrace=None):
    all_languages = proficiencies.get("Languages", {})
    race_languages = []
    race_names = {race}
    if subrace and subrace != race:
        race_names.add(subrace)
    # Collect languages granted by race or subrace
    for lang, info in all_languages.items():
        if "Races" in info and any(r in info["Races"] for r in race_names):
            race_languages.append(lang)
    # Handle "One of your choice" and "Two of your choice" if present in race_languages
    # Remove them and pick accordingly from available languages
    picks_needed = 0
    if "One of your choice" in race_languages:
        race_languages.remove("One of your choice")
        picks_needed += 1
    if "Two of your choice" in race_languages:
        race_languages.remove("Two of your choice")
        picks_needed += 2
    # Pick from all languages not already chosen
    available = [l for l in all_languages if l not in race_languages]
    if picks_needed > 0 and available:
        if len(available) >= picks_needed:
            race_languages += random.sample(available, picks_needed)
        else:
            race_languages += available
    # Remove duplicates just in case
    return list(dict.fromkeys(race_languages))

def generate_npc():
    class_roll = random.randint(1, 100)
    print(f"Class Roll: {class_roll}")
    race_roll = random.randint(1, 100)
    backstory_roll = str(random.randint(1, len(backstories)))

    char_class = get_from_table(class_roll, class_table)
    print(f"Class: {char_class}")
    race = get_from_table(race_roll, race_table_common)
    print(race)
    if race == "Exotic":
        race = get_from_table(random.randint(1, 100), race_table_exotic)
        print(race)
    subrace = roll_subrace(race)
    # print(subrace)
    
    # Get backstory and background from JSON
    backstory = backstories[backstory_roll]["backstory"]
    background = backstories[backstory_roll]["background"]


    if char_class == "Dealer's Choice":
        char_class = random.choice(list(stat_profiles.keys()))

    stats = generate_stats_with_race(char_class, race, subrace)
    char_level = random.randint(1, 20)
    feats_taken = []

    match char_class:
        case "Wizard":
            if char_level > 2:
                subclass = random.choice(subclass_table["Wizard"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Sorcerer":
            if char_level > 2:
                subclass = random.choice(subclass_table["Sorcerer"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Warlock":
            subclass = random.choice(subclass_table["Warlock"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Cleric":
            subclass = random.choice(subclass_table["Cleric"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Druid":
            if char_level > 2:
                subclass = random.choice(subclass_table["Druid"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Paladin":
            if char_level > 3:
                subclass = random.choice(subclass_table["Paladin"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Ranger":
            if char_level > 3:
                subclass = random.choice(subclass_table["Ranger"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Fighter":
            if char_level > 3:
                subclass = random.choice(subclass_table["Fighter"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Monk":
            if char_level > 3:
                subclass = random.choice(subclass_table["Monk"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Barbarian":
            if char_level > 3:
                subclass = random.choice(subclass_table["Barbarian"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Rogue":
            if char_level > 3:
                subclass = random.choice(subclass_table["Rogue"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Bard":
            if char_level > 3:
                subclass = random.choice(subclass_table["Bard"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case "Artificer":
            if char_level > 3:
                subclass = random.choice(subclass_table["Artificer"])
            feats_taken = ability_score_increase_or_feat(stats, char_level)
        case _:
            pass  # Placeholder for class-specific features


    # --- Skill proficiency logic with overlap handling ---
    class_skills = get_class_skill_proficiencies(char_class)
    background_skills = get_background_skill_proficiencies(background)
    all_skills = set(class_skills + background_skills)

    # Ensure the character gets the full number of class skill proficiencies
    class_prof = proficiencies["Classes"].get(char_class, {})
    skills_info = class_prof.get("skills", {})
    num_class_skills = skills_info.get("choose", 0)
    class_skill_options = set(skills_info.get("from", []))

    # Remove any skills already granted by background from the class options
    available_for_class = list(class_skill_options - set(background_skills))
    # Add more class skills if overlap reduced the number
    while len(all_skills) < num_class_skills + len(background_skills) and available_for_class:
        new_skill = random.choice(available_for_class)
        all_skills.add(new_skill)
        available_for_class.remove(new_skill)

    # --- Tool proficiency logic ---
    tool_profs = set(get_class_tool_proficiencies(char_class) + get_background_tool_proficiencies(background))
    
    # --- Language proficiency logic ---
    all_languages = get_background_languages(background) + get_race_languages(race, subrace)
    all_languages = list(dict.fromkeys(all_languages))
    all_languages.sort()

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
        "Skill Proficiencies": list(all_skills),
        "Tool Proficiencies": list(tool_profs),
        "Feats": feats_taken if feats_taken else None,
        "Spells": get_npc_spells(char_class, char_level) if char_class in ALL_SPELL_SLOTS else None,
        "Languages": all_languages,
    }

def show_npc_ui(npc):
    root = tk.Tk()
    root.title("Generated D&D NPC")

    # Make the window resizable and add a scrollbar
    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)
    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Display each field in the NPC
    row = 0
    for key, value in npc.items():
        label = ttk.Label(scrollable_frame, text=f"{key}:", font=("Arial", 10, "bold"))
        label.grid(row=row, column=0, sticky="nw", padx=5, pady=2)
        # Display stats in D&D order: STR, DEX, CON, INT, WIS, CHA
        if key == "Stats" and isinstance(value, dict):
            stat_order = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
            stats_text = "\n".join(f"{stat}: {value.get(stat, '-')}" for stat in stat_order)
            value_label = ttk.Label(scrollable_frame, text=stats_text, wraplength=500, justify="left")
        # Show feats as a readable list with descriptions if available
        elif key == "Feats" and value:
            feats_display = ""
            for feat_name in value:
                # Try to find the feat in the feats list for description
                feat_obj = next((f for f in feats if f["name"] == feat_name), None)
                if feat_obj:
                    feats_display += f"{feat_obj['name']}: {feat_obj.get('description', '')}\n"
                else:
                    feats_display += f"{feat_name}\n"
            value_label = ttk.Label(scrollable_frame, text=feats_display.strip(), wraplength=500, justify="left")
        elif isinstance(value, dict) or isinstance(value, list):
            text = json.dumps(value, indent=2, ensure_ascii=False)
            value_label = ttk.Label(scrollable_frame, text=text, wraplength=500, justify="left")
        else:
            text = str(value)
            value_label = ttk.Label(scrollable_frame, text=text, wraplength=500, justify="left")
        value_label.grid(row=row, column=1, sticky="nw", padx=5, pady=2)
        row += 1

    root.mainloop()

# Generate example NPC
n = generate_npc()
show_npc_ui(n)
print(n)
#TODO: Add a way to save the generated NPC to a file
#TODO: Add a way to load the generated NPC from a file
#TODO: Add a way to edit the generated NPC
#TODO: Add a way to delete the generated NPC
#TODO: Add a way to view the generated NPC
#TODO: Maybe add a chatgpt wrapper to allow for more complex backstories
#TODO: Items and equipment
#TODO: Subclasses that add spells to character
#TODO: Add a way to generate a full character sheet
#TODO: Factions and Guilds
#TODO: Names list (nathan is making a names list)
#TODO: FULL ADVENTURE GENERATOR