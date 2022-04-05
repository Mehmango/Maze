embed
<drac2>
args = &ARGS&
title = ":compass: Checking your options :compass:"
desc = ""
footer = "Maze alias by Mehmango | !maze for help"
image = "https://images.alphacoders.com/691/thumb-1920-691531.jpg"

imageGvar = "7b705930-60f2-488e-873d-6a5841ccea50"
imageDict = load_json(get_gvar(imageGvar))

mazeDict = load_json(get_svar("maze"))
horizontal_corridors = mazeDict.horizontal_corridors
vertical_corridors = mazeDict.vertical_corridors

MAX_X = len(vertical_corridors)
MAX_Y = len(horizontal_corridors[0])

playerCvar = get("mazePlayerCvar")
playerDict = {}
if playerCvar is None:
    playerDict = {
        "mazeId":mazeDict.mazeId,
        "position":(0,0),
        "solved":False
    }
    
else:
    playerDict = load_json(playerCvar)

if playerDict.solved:
    title = ":confetti_ball: You already solved the maze! :confetti_ball:"
    
else:

    if playerDict.mazeId != mazeDict.mazeId:
        playerDict.update(mazeId=mazeDict.mazeId, position=(0,0))
        
    options = ""

    playerPosition = playerDict.position
    playerX = playerPosition[0]
    playerY = playerPosition[1]
    if playerY > 0 and vertical_corridors[playerX][playerY-1] == 1:
        options += "n"
    if playerY < MAX_Y-1 and vertical_corridors[playerX][playerY] == 1:
        options += "s"
    if playerX < MAX_X-1 and horizontal_corridors[playerX][playerY] == 1:
        options += "e"
    if playerX > 0 and horizontal_corridors[playerX-1][playerY] == 1:
        options += "w"
        
    image = imageDict[options]
            
    desc += "\n\nUse `!maze move <direction>` to move your character in the specified direction"
    desc += "\n*(Eg: `!maze move e`)*"

character().set_cvar("mazePlayerCvar", dump_json(playerDict))
return f""" -title "{title}" -desc "{desc}" -footer "{footer}" -image "{image}" """
</drac2>
