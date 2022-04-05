embed
<drac2>
args = &ARGS&
title = ":eyes: Peeking at the maze :eyes:"
desc = ""
footer = "Maze alias by Mehmango | !maze for help"
image = ""

mazeDict = load_json(get_svar("maze"))
horizontal_corridors = mazeDict.horizontal_corridors
vertical_corridors = mazeDict.vertical_corridors

MAX_X = len(vertical_corridors)
MAX_Y = len(horizontal_corridors[0])

desc += "```"

for y in range(MAX_Y):
    for x in range(MAX_X):
        desc += "██"
        if x < MAX_X-1:
            if horizontal_corridors[x][y] == 1:
                desc += "■■"
            else:
                desc += "  "
    desc += "\n"
    if y < MAX_Y-1:
        for x in range(MAX_X):
            if vertical_corridors[x][y] == 1:
                desc += "▐▌  " if x < MAX_X-1 else "▐▌"
            else:
                desc += "    " if x < MAX_X-1 else "  "
    desc += "\n"

desc += "```"
        
return f""" -title "{title}" -desc "{desc}" -footer "{footer}" -image "{image}" """
</drac2>
