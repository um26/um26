import json
import random
from datetime import date

# Load the GIFs from gifs.json
with open("gifs.json", "r") as file:
    gifs = json.load(file)["gifs"]

# Determine today's GIF using the current date
today = date.today()
index = today.toordinal() % len(gifs)
selected_gif = gifs[index]

# Update the README file
with open("README.md", "r") as file:
    readme = file.readlines()

# Replace the GIF URL in the README
updated_readme = []
for line in readme:
    if "![Coding Gif]" in line:
        updated_readme.append(f"![Coding Gif]({selected_gif})\n")
    else:
        updated_readme.append(line)

# Write the changes back to README.md
with open("README.md", "w") as file:
    file.writelines(updated_readme)
