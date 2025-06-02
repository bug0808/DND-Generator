# DND-Generator
A Python-based Dungeons & Dragons 5th Edition NPC generator.
Generates random characters with stats, class, subclass, race, background, skills, tools, languages, spells, and backstory using customizable JSON data.

## Features
Random NPC generation with D&D 5e rules
Supports all core classes, subclasses, races, and backgrounds
Handles skill and tool proficiencies (with overlap logic)
Assigns languages based on race and background (using tags like "Common" and "Exotic")
Generates spells for spellcasting classes
Pulls backstories and backgrounds from JSON for variety
Easily extensible: add new races, classes, backgrounds, or spells by editing JSON files

## Customization
Add new races, classes, backgrounds, or spells by editing the relevant JSON files.
Change proficiency rules (e.g., add new tool groups or language tags) in proficiencies.json.
Expand backstories in backstories.json for more variety.

## TODO
Save/load/edit/delete generated NPCs
Generate full character sheets
Add feats, items, and equipment
Add factions, guilds, and adventure hooks
More advanced backstory and subclass features
License
MIT License