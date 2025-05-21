# spell_lists.py

# Dictionary of spells for each class with spell levels
spell_lists = {
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
        0: ["Guidance", "Sacred Flame", "Thaumaturgy"],
        1: ["Cure Wounds", "Bless", "Shield of Faith"],
        2: ["Spiritual Weapon", "Lesser Restoration", "Hold Person"],
        3: ["Spirit Guardians", "Revivify", "Dispel Magic"],
        4: ["Death Ward", "Guardian of Faith", "Divination"],
        5: ["Flame Strike", "Greater Restoration", "Mass Cure Wounds"]
    },
    "Druid": {
        0: ["Druidcraft", "Guidance", "Produce Flame"],
        1: ["Entangle", "Goodberry", "Faerie Fire"],
        2: ["Moonbeam", "Flaming Sphere", "Lesser Restoration"],
        3: ["Call Lightning", "Plant Growth", "Wind Wall"],
        4: ["Conjure Woodland Beings", "Ice Storm", "Polymorph"],
        5: ["Commune with Nature", "Tree Stride", "Mass Cure Wounds"]
    },
    "Sorcerer": {
        0: ["Prestidigitation", "Ray of Frost", "Fire Bolt"],
        1: ["Magic Missile", "Shield", "Chromatic Orb"],
        2: ["Mirror Image", "Scorching Ray", "Hold Person"],
        3: ["Fireball", "Counterspell", "Fly"],
        4: ["Greater Invisibility", "Ice Storm", "Polymorph"],
        5: ["Teleportation Circle", "Wall of Force", "Cone of Cold"]
    },
    "Bard": {
        0: ["Vicious Mockery", "Prestidigitation", "Mage Hand"],
        1: ["Healing Word", "Dissonant Whispers", "Charm Person"],
        2: ["Suggestion", "Lesser Restoration", "Hold Person"],
        3: ["Hypnotic Pattern", "Dispel Magic", "Major Image"],
        4: ["Greater Invisibility", "Polymorph", "Dimension Door"],
        5: ["Raise Dead", "Mass Cure Wounds", "Hold Monster"]
    },
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
}