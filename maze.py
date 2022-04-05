embed
<drac2>
args = &ARGS&

title = ":face_with_spiral_eyes: A little lost? :face_with_spiral_eyes:"

desc = "❧ `!maze` ⟶ Displays a list of all commands :scroll:"
desc += "\n\n❧ `!maze move <direction>` ⟶ Moves your character in the specified direction if possible :person_with_probing_cane:\n\nPossible directions: n, s, e, w \n*(Eg: `!maze move n`)*"
desc += "\n\n❧ `!maze current` ⟶ Displays your current movement options :compass:"
desc += "\n\n❧ `!maze admin` ⟶ Displays a list of commands for server admins :levitate:"

footer = "Maze alias by Mehmango | !maze for help"

image = "https://images.alphacoders.com/691/thumb-1920-691531.jpg"

return f""" -title "{title}" -desc "{desc}" -footer "{footer}" -image "{image}" """
</drac2>
