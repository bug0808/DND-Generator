# spell_lists.py

# all_spells = {
#     "Acid Splash": {
#         "level": 0,
#         "school": "Conjuration",
#         "classes": ["Wizard", "Sorcerer", "Artificer"],
#         "components": ["V", "S"],
#         "casting_time": "1 Action",
#         "range": "60 Feet",
#         "duration": "Instantaneous"
#     },
#     "Blade Ward": {
#         "level": 0,
#         "school": "Abjuration",
#         "classes": ["Wizard", "Sorcerer"],
#         "components": ["V", "S"],
#         "casting_time": "1 Action",
#         "range": "Self",
#         "duration": "1 round"
#     },
#     "Fire Bolt": {
#         "level": 0,
#         "school": "Evocation",
#         "classes": ["Wizard", "Sorcerer", "Artificer"],
#         "components": ["V", "S"],
#         "casting_time": "1 Action",
#         "range": "120 feet",
#         "duration": "Instantaneous"
#     },
#     "Magic Missile": {
#         "level": 1,
#         "school": "Evocation",
#         "classes": ["Wizard", "Sorcerer"],
#         "components": ["V", "S"],
#         "casting_time": "1 Action",
#         "range": "120 feet",
#         "duration": "Instantaneous"
#     },
#     "Cure Wounds": {
#         "level": 1,
#         "school": "Evocation",
#         "classes": ["Cleric", "Druid", "Bard", "Paladin", "Ranger", "Artificer"],
#         "components": ["V", "S"],
#         "casting_time": "1 Action",
#         "range": "Touch",
#         "duration": "Instantaneous"
#     },
#     # ...continue for all spells...
# }

# Dictionary of spells for each class with spell levels
spell_lists = {
    #Done
    "Wizard": {
        0: ["Acid Splash", "Blade Ward", "Booming Blade", "Chill Touch", "Control Flames", "Create Bonfire", "Dancing Lights", "Encode Thoughts", "Fire Bolt", "Friends", "Frostbite", "Green-Flame Blade", "Gust", "Infestation", "Light", "Lightning Lure", "Mage Hand", "Mending", "Message", "Mind Sliver", "Minor Illusion", "Mold Earth", "Poison Spray", "Prestidigitation","Ray of Frost", "Sapping Sting", "Shape Water", "Shocking Grasp", "Sword Burst", "Thunderclap", "Toll the Dead","True Strike"],
        1: ["Absorb Elements", "Alarm", "Burning Hands", "Catapult", "Cause Fear", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Distort Value", "Earth Tremor", "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Frost Fingers", "Gift of Alacrity", "Grease", "Ice Knife", "Identify", "Illusory Script", "Jim's Magic Missile", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Magnify Gravity", "Protection from Evil and Good", "Ray of Sickness", "Shield", "Silent Image", "Silvery Barbs", "Sleep", "Snare", "Tasha's Caustic Brew", "Tasha's Hideous Laughter", "Tenser's Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt"],
        2: ["Aganazzar's Scorcher", "Air Bubble", "Alter Self", "Arcane Lock", "Augury", "Blindness/Deafness", "Blur", "Borrowed Knowledge", "Cloud of Daggers", "Continual Flame", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Dragon's Breath", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/Reduce", "Flaming Sphere", "Flock of Familiars", "Fortune's Favor", "Gentle Repose", "Gift of Gab", "Gust of Wind", "Hold Person", "Immovable Object", "Invisibility", "Jim's Glowing Coin", "Kinetic Jaunt", "Knock", "Levitate", "Locate Object", "Magic Mouth", "Magic Weapon", "Maximillian's Earthen Grasp", "Melf's Acid Arrow", "Mind Spike", "Mirror Image", "Misty Step", "Nathair's Mischief", "Nystul's Magic Aura", "Phantasmal Force", "Pyrotechnics", "Ray of Enfeeblement", "Rime's Binding Ice", "Rope Trick", "Scorching Ray", "See Invisibility", "Shadow Blade", "Shatter", "Skywrite", "Snilloc's Snowball Swarm", "Spider Climb", "Spray Of Cards", "Suggestion", "Tasha's Mind Whip", "Vortex Warp", "Warding Wind", "Warp Sense", "Web", "Wither and Bloom", "Wristpocket"],
        3: ["Animate Dead", "Antagonize", "Ashardalon's Stride", "Bestow Curse", "Blink", "Catnap", "Clairvoyance", "Counterspell", "Dispel Magic", "Enemies Abound", "Erupting Earth", "Fast Friends", "Fear", "Feign Death", "Fireball", "Flame Arrows", "Fly", "Galder's Tower", "Gaseous Form", "Glyph of Warding", "Haste", "Hypnotic Pattern", "Incite Greed", "Intellect Fortress", "Leomund's Tiny Hut", "Life Transference", "Lightning Bolt", "Magic Circle", "Major Image", "Melf's Minute Meteors", "Nondetection", "Phantom Steed", "Protection from Energy", "Pulse Wave", "Remove Curse", "Sending", "Sleet Storm", "Slow", "Speak with Dead", "Spirit Shroud", "Stinking Cloud", "Summon Fey", "Summon Lesser Demons", "Summon Shadowspawn", "Summon Undead", "Thunder Step", "Tidal Wave", "Tiny Servant", "Tongues", "Vampiric Touch", "Wall of Sand", "Wall of Water", "Water Breathing"],
        4: ["Arcane Eye", "Banishment", "Blight", "Charm Monster", "Confusion", "Conjure Minor Elementals", "Control Water", "Dimension Door", "Divination", "Elemental Bane", "Evard's Black Tentacles", "Fabricate", "Fire Shield", "Galder's Speedy Courier", "Gate Seal", "Gravity Sinkhole", "Greater Invisibility", "Hallucinatory Terrain", "Ice Storm",  "Leomund's Secret Chest", "Locate Creature", "Mordenkainen's Faithful Hound", "Mordenkainen's Private Sanctum", "Otiluke's Resilient Sphere", "Phantasmal Killer", "Polymorph", "Raulothim's Psychic Lance", "Sickening Radiance", "Spirit Of Death", "Stone Shape", "Stoneskin", "Storm Sphere", "Summon Aberration", "Summon Construct", "Summon Elemental", "Summon Greater Demon", "Vitriolic Sphere", "Wall of Fire", "Watery Sphere"],
        5: ["Animate Objects", "Bigby's Hand", "Cloudkill", "Cone of Cold", "Conjure Elemental", "Contact Other Plane", "Control Winds", "Create Spelljamming Helm", "Creation", "Danse Macabre", "Dawn", "Dominate Person", "Dream", "Enervation", "Far Step", "Geas", "Hold Monster", "Immolation", "Infernal Calling", "Legend Lore", "Mislead", "Modify Memory", "Negative Energy Flood", "Passwall", "Planar Binding", "Rary's Telepathic Bond", "Scrying", "Seeming", "Skill Empowerment", "Steel Wind Strike", "Summon Draconic Spirit", "Synaptic Static", "Telekinesis", "Teleportation Circle", "Temporal Shunt", "Transmute Rock", "Wall of Force", "Wall of Light", "Wall of Stone"],
        6: ["Arcane Gate","Chain Lightning","Circle of Death","Contingency","Create Homunculus","Create Undead","Disintegrate","Drawmij's Instant Summons","Eyebite","Fizban's Platinum Shield","Flesh to Stone","Globe of Invulnerability","Gravity Fissure","Guards and Wards","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Magic Jar","Mass Suggestion","Mental Prison","Move Earth","Otiluke's Freezing Sphere","Otto's Irresistible Dance","Programmed Illusion","Scatter","Soul Cage","Summon Fiend","Sunbeam","Tasha's Otherworldly Guise","Tenser's Transformation","True Seeing","Wall of Ice"],
        7: ["Create Magen","Crown of Stars","Delayed Blast Fireball","Draconic Transformation","Dream of the Blue Veil","Etherealness","Finger of Death","Forcecage","Mirage Arcane","Mordenkainen's Magnificent Mansion","Mordenkainen's Sword","Plane Shift","Power Word: Pain","Prismatic Spray","Project Image","Reverse Gravity","Sequester","Simulacrum","Symbol","Teleport","Tether Essence","Whirlwind"],
        8: ["Abi-Dalzim's Horrid Wilting", "Antimagic Field", "Antipathy/Sympathy", "Clone", "Control Weather", "Dark Star", "Demiplane", "Dominate Monster", "Feeblemind", "Illusory Dragon", "Incendiary Cloud", "Maddening Darkness", "Maze", "Mighty Fortress", "Mind Blank", "Power Word: Stun", "Reality Break", "Sunburst", "Telepathy"],
        9: ["Astral Projection", "Blade of Disaster", "Foresight", "Gate", "Imprisonment", "Invulnerability", "Mass Polymorph", "Meteor Swarm", "Power Word: Kill", "Prismatic Wall", "Psychic Scream", "Ravenous Void", "Shapechange", "Time Ravage", "Time Stop", "True Polymorph", "Weird", "Wish"]
    },
    "Cleric": {
    0: ["Guidance","Light","Mending","Resistance","Sacred Flame","Spare the Dying","Thaumaturgy","Toll the Dead","Word of Radiance"],
    1: ["Bane","Bless","Ceremony",
        "Command","Create or Destroy Water","Cure Wounds","Detect Evil and Good","Detect Magic","Detect Poison and Disease","Guiding Bolt",
        "Healing Word","Inflict Wounds","Protection from Evil and Good","Purify Food and Drink","Sanctuary","Shield of Faith"],
    2: ["Aid","Augury","Blindness/Deafness", "Calm Emotions", "Continual Flame","Enhance Ability","Find Traps", "Gentle Repose","Hold Person",
        "Lesser Restoration","Locate Object","Prayer of Healing","Protection from Poison","Silence","Spiritual Weapon","Warding Bond","Zone of Truth"],
    3: ["Animate Dead","Aura of Vitality","Beacon of Hope", "Bestow Curse","Clairvoyance","Create Food and Water","Daylight","Dispel Magic","Feign Death",
        "Glyph of Warding","Life Transference","Magic Circle","Mass Healing Word","Meld into Stone","Motivational Speech",
        "Protection from Energy","Remove Curse","Revivify","Sending","Speak with Dead","Spirit Guardians","Tongues","Water Walk"],
    4: ["Aura of Life","Aura of Purity","Banishment","Control Water","Death Ward",
        "Divination","Freedom of Movement","Guardian of Faith","Locate Creature","Stone Shape"],
    5: ["Commune","Contagion","Dawn","Dispel Evil and Good","Flame Strike","Geas","Greater Restoration","Hallow",
        "Holy Weapon","Insect Plague","Legend Lore","Mass Cure Wounds","Planar Binding","Raise Dead","Scrying"],
    6: ["Blade Barrier", "Create Undead", "Find the Path", "Forbiddance","Harm",
        "Heal","Heroes' Feast","Planar Ally","Sunbeam","True Seeing","Word of Recall"],
    7: ["Conjure Celestial","Divine Word","Etherealness","Fire Storm", "Plane Shift", "Regenerate", "Resurrection", "Symbol", "Temple of the Gods"],
    8: ["Antimagic Field","Control Weather","Earthquake","Holy Aura","Sunburst"],
    9: ["Astral Projection","Gate","Mass Heal","Power Word: Heal","True Resurrection"]
    },
    "Druid": {
        0: ["Control Flames", "Create Bonfire", "Druidcraft", "Frostbite", "Guidance", "Gust",
            "Infestation", "Magic Stone", "Mending", "Mold Earth", "Poison Spray", "Primal Savagery",
            "Produce Flame", "Resistance", "Shape Water", "Shillelagh", "Thorn Whip", "Thunderclap"],
        1: ["Absorb Elements", "Animal Friendship", "Beast Bond", "Charm Person", "Create or Destroy Water",
            "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Earth Tremor", "Entangle",
            "Faerie Fire", "Fog Cloud", "Goodberry", "Healing Word", "Ice Knife", "Jump", "Longstrider",
            "Protection from Evil and Good", "Purify Food and Drink", "Snare", "Speak with Animals",
            "Thunderwave"],
        2: ["Air Bubble", "Animal Messenger", "Augury", "Barkskin", "Beast Sense", "Continual Flame",
            "Darkvision", "Dust Devil", "Earthbind", "Enhance Ability", "Enlarge/Reduce", "Find Traps",
            "Flame Blade", "Flaming Sphere", "Gust of Wind", "Healing Spirit", "Heat Metal", "Hold Person",
            "Lesser Restoration", "Locate Animals or Plants", "Locate Object", "Moonbeam", "Pass Without Trace",
            "Protection from Poison", "Skywrite", "Spike Growth", "Summon Beast", "Warding Wind",
            "Wither and Bloom"],
        3: ["Aura of Vitality", "Call Lightning", "Conjure Animals", "Daylight", "Dispel Magic",
            "Elemental Weapon", "Erupting Earth", "Feign Death", "Flame Arrows", "Meld into Stone",
            "Plant Growth", "Protection from Energy", "Revivify", "Sleet Storm", "Speak with Plants",
            "Summon Fey", "Tidal Wave", "Wall of Water", "Water Breathing", "Water Walk", "Wind Wall"],
        4: ["Blight", "Charm Monster", "Confusion", "Conjure Minor Elementals", "Conjure Woodland Beings",
            "Control Water", "Divination", "Dominate Beast", "Elemental Bane", "Fire Shield",
            "Freedom of Movement", "Giant Insect", "Grasping Vine", "Guardian of Nature",
            "Hallucinatory Terrain", "Ice Storm", "Locate Creature", "Polymorph", "Stone Shape",
            "Stoneskin", "Summon Elemental", "Wall of Fire", "Watery Sphere"],
        5: ["Antilife Shell", "Awaken", "Commune with Nature", "Cone of Cold", "Conjure Elemental",
            "Contagion", "Control Winds", "Geas", "Greater Restoration", "Insect Plague", "Maelstrom",
            "Mass Cure Wounds", "Planar Binding", "Reincarnate", "Scrying", "Summon Draconic Spirit",
            "Transmute Rock", "Tree Stride", "Wall of Stone", "Wrath Of Nature"],
        6: ["Bones of the Earth", "Conjure Fey", "Druid Grove", "Find the Path", "Flesh to Stone",
            "Heal", "Heroes' Feast", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone",
            "Investiture of Wind", "Move Earth", "Primordial Ward", "Sunbeam", "Transport via Plants",
            "Wall of Thorns", "Wind Walk"],
        7: ["Draconic Transformation","Fire Storm", "Mirage Arcane", "Plane Shift", "Regenerate", "Reverse Gravity"],
        8: ["Animal Shapes", "Antipathy/Sympathy", "Control Weather", "Earthquake", "Feeblemind","Incendiary Cloud","Sunburst", "Tsunami"],
        9: ["Foresight", "Shapechange", "Storm of Vengeance", "True Resurrection"]
    },
    "Sorcerer": {
        0: ["Acid Splash","Blade Ward","Booming Blade","Chill Touch","Control Flames",
            "Create Bonfire","Dancing Lights","Fire Bolt","Friends","Frostbite","Green-Flame Blade","Gust","Infestation",
            "Light","Lightning Lure","Mage Hand","Mending","Message","Mind Sliver","Minor Illusion",
            "Mold Earth","Poison Spray","Prestidigitation","Ray of Frost","Shape Water","Shocking Grasp","Sword Burst","Thunderclap","True Strike"],
        1: ["Absorb Elements","Burning Hands","Catapult","Chaos Bolt","Charm Person","Chromatic Orb","Color Spray",
            "Comprehend Languages","Detect Magic","Disguise Self","Distort Value","Earth Tremor","Expeditious Retreat",
            "False Life","Feather Fall","Fog Cloud","Grease","Ice Knife","Jump","Mage Armor","Magic Missile","Ray of Sickness",
            "Shield","Silent Image","Silvery Barbs","Sleep","Tasha's Caustic Brew","Thunderwave","Thunderwave","Witch Bolt"],
       2: ["Aganazzar's Scorcher","Air Bubble","Alter Self","Blindness/Deafness","Blur","Cloud of Daggers","Crown of Madness","Darkness",
            "Darkvision","Detect Thoughts","Dragon's Breath","Dust Devil","Earthbind","Enhance Ability","Enlarge/Reduce","Flame Blade",
            "Flaming Sphere","Gust of Wind","Hold Person","Invisibility","Kinetic Jaunt","Knock","Levitate","Magic Weapon","Maximillian's Earthen Grasp",
            "Mind Spike","Mirror Image","Misty Step","Nathair's Mischief","Phantasmal Force","Pyrotechnics","Rime's Binding Ice","Scorching Ray",
            "See Invisibility","Shadow Blade","Shatter","Snilloc's Snowball Swarm","Spider Climb","Spray Of Cards","Suggestion",
            "Tasha's Mind Whip","Vortex Warp","Warding Wind","Warp Sense","Web", "Wither and Bloom"],
        3: [ "Antagonize","Ashardalon's Stride", "Blink",  "Catnap","Clairvoyance","Counterspell", "Daylight", "Dispel Magic", "Enemies Abound","Erupting Earth","Fear","Fireball","Flame Arrows","Fly","Gaseous Form","Haste","Hypnotic Pattern", "Incite Greed",
            "Intellect Fortress", "Lightning Bolt","Major Image","Melf's Minute Meteors","Protection from Energy","Sleet Storm","Slow","Stinking Cloud","Thunder Step","Tidal Wave","Tongues","Vampiric Touch","Wall of Water","Water Breathing","Water Walk"],
        4: ["Banishment","Blight","Charm Monster","Confusion","Dimension Door","Dominate Beast",
            "Fire Shield", "Gate Seal", "Greater Invisibility","Ice Storm","Polymorph","Raulothim's Psychic Lance","Sickening Radiance",
            "Spirit of Death", "Stoneskin", "Storm Sphere", "Vitriolic Sphere", "Wall of Fire", "Watery Sphere"],
        5: ["Animate Objects", "Bigby's Hand", "Cloudkill", "Cone of Cold", "Control Winds", "Creation",
            "Dominate Person", "Enervation", "Far Step", "Geas", "Hold Monster", "Immolation", "Insect Plague",
            "Seeming","Skill Empowerment", "Summon Draconic Spirit", "Synaptic Static", "Telekinesis", "Teleportation Circle" "Wall of Light","Wall of Stone"],
        6: ["Arcane Gate","Chain Lightning", "Circle of Death", "Disintegrate", "Eyebite", "Fizban's Platinum Shield",
            "Flesh to Stone", "Globe of Invulnerability", "Investiture of Flame", "Investiture of Ice",
            "Investiture of Stone", "Investiture of Wind", "Mass Suggestion", "Mental Prison", "Move Earth",
            "Otiluke's Freezing Sphere", "Scatter", "Sunbeam", "Tasha's Otherworldly Guise", "True Seeing"],
        7:["Crown of Stars", "Delayed Blast Fireball", "Draconic Transformation", "Dream of the Blue Veil","Etherealness",
           "Finger of Death", "Firestorm", "Plane Shift", "Power Word: Pain", "Prismatic Spray", "Reverse Gravity", "Teleport"],
        8: ["Abi-Dalzim's Horrid Wilting", "Demiplane", "Dominate Monster", "Earthquale", "Incendiary Cloud", "Power Word: Stun",
            "Sunburst"],
        9: ["Blade of Disaster", "Gate", "Mass Polymorph", "Meteor Swarm", "Power Word: Kill", "Psychic Scream",
            "Time Stop", "Wish"]
    },
    "Bard": {
        0: ["Vicious Mockery", "Prestidigitation", "Mage Hand"],
        1: ["Healing Word", "Dissonant Whispers", "Charm Person"],
        2: ["Suggestion", "Lesser Restoration", "Hold Person"],
        3: ["Hypnotic Pattern", "Dispel Magic", "Major Image"],
        4: ["Greater Invisibility", "Polymorph", "Dimension Door"],
        5: ["Raise Dead", "Mass Cure Wounds", "Hold Monster"]
    },
    "Ranger": {

    },

    "Warlock": {

    },
    #Done
    "Paladin": {
        0: [],
        1: [ "Bless", "Ceremony", "Command", "Compelled Duel", "Cure Wounds",
            "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease",
            "Divine Favor", "Heroism", "Protection from Evil and Good",
            "Purify Food and Drink", "Searing Smite", "Shield of Faith",
            "Thunderous Smite", "Wrathful Smite"],
        2: ["Aid", "Branding Smite", "Find Steed", "Gentle Repose", "Lesser Restoration",
            "Locate Object", "Magic Weapon", "Prayer of Healing", "Protection from Poison",
            "Warding Bond", "Zone of Truth"],
        3: ["Aura of Vitality", "Blinding Smite", "Create Food and Water","Crusader's Mantle", 
            "Daylight","Dispel Magic","Elemental Weapon","Magic Circle",
            "Remove Curse","Revivify","Spirit Shroud"],
        4: ["Aura of Life","Aura of Purity","Banishment",
            "Death Ward","Find Greater Steed","Locate Creature",
            "Staggering Smite"],
        5: ["Banishing Smite","Circle of Power","Destructive Wave",
            "Dispel Evil and Good","Geas","Holy Weapon",
            "Raise Dead","Summon Celestial"]
    },
    #Done
    "Artificer": {
        0: ["Acid Splash", "Booming Blade", "Create Bonfire", "Dancing Lights", "Fire Bolt", "Frostbite", "Green-Flame Blade", "Guidance", "Light", "Lightning Lure", "Mage Hand", "Magic Stone", "Mending", "Message", "Poison Spray", "Prestidigitation", "Ray of Frost", "Resistance", "Shocking Grasp", "Spare the Dying", "Sword Burst", "Thorn Whip", "Thunderclap"],
        1: ["Absorb Elements", "Alarm", "Catapult", "Cure Wounds", "Detect Magic", "Disguise Self", "Expeditious Retreat", "Faerie Fire", "False Life", "Feather Fall", "Grease",  "Identify", "Jump", "Longstrider", "Purify Food and Drink", "Sanctuary", "Snare", "Tasha's Caustic Brew"],
        2: ["Aid","Air Bubble","Alter Self","Arcane Lock", "Blur", "Continual Flame", "Darkvison", "Enhance Ability","Enlarge/Reduce","Heat Metal","Invisibility","Kinetic Jaunt","Lesser Restoration", "Levitate","Magic Mouth","Magic Weapon","Protection from Poison","Pyrotechnics","Rope Trick", "See Invisibility","Spider Climb","Vortex Warp","Web"],
        3: ["Ashardalon's Stride","Blink","Catnap", "Create Food and Water", "Dispel Magic","Elemental Weapon","Flame Arrows","Fly", "Glyph of Warding", "Haste","Intellect Fortress","Protection from Energy","Revivify","Tiny Servant", "Water Breathing", "Water Walk"],
        4: ["Arcane Eye","Elemental Bane","Fabricate","Freedom of Movement","Leomund's Secret Chest","Mordenkainen's Faithful Hound","Mordenkainen's Private Sanctum","Otiluke's Resilient Sphere","Stone Shape", "Stoneskin", "Summon Construct"],
        5: ["Animate Objects","Bigby's Hand", "Create Spelljamming Helm", "Creation","Greater Restoration", "Skill Empowerment", "Transmute Rock", "Wall of Stone"],
    },
}

from spell_lists import spell_lists
import pprint
all_spells = {}

for class_name, levels in spell_lists.items():
    for level, spells in levels.items():
        for spell in spells:
            # Remove duplicates and merge class lists
            if spell not in all_spells:
                all_spells[spell] = {
                    "level": level,
                    "classes": [class_name]
                }
            else:
                if class_name not in all_spells[spell]["classes"]:
                    all_spells[spell]["classes"].append(class_name)

# Optional: sort classes for each spell
for spell in all_spells:
    all_spells[spell]["classes"].sort()

# Print or write to file
import pprint
pprint.pprint(all_spells)
# Save all_spells to a text file
with open("all_spells.txt", "w", encoding="utf-8") as f:
    f.write(pprint.pformat(all_spells))