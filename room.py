#Name-
#description-

class Room:

    def __init__(self,name: str, image_filepath: str) -> None:
        """
        A Room in the Rooom Adventure game.

        name: str - a name for the room
            ex: 'ROOM' OR 'LIVING ROOM'
        image_filepath: str - the relative filepath to the image
            ex: 'images\\room1.gif' on windows
`           Fr: os.path.join("images", "room1.gif")
        """

        self.name = name
        self.image = image_filepath
        self.exits: dict[str, 'Room'] = {} #key is the direction, value is the room
        self.items: dict[str, str] = {} #key is the label, value os the description
        self.grabbables = []


    def add_exist(self, location: str, room: 'Room | None') -> None:
        """
        Adds an exist to the room

        location: str - a direction such as'north', 'south', 'east', 'west',etc
        room: Room | None - a room object or None. In the case of losing/death sequence, use None.
        """
        self.exits[location]= room

    def add_item(self, label: str, description: str) -> None:
        self.items[label]= description

    def add_grabbable(self, item: str) -> None:
        self.grabbables.append(item)

    def delete_grabbable(self,item:str) -> None:
        self.grabbables.remove(item)

    def __str__(self) -> str:

        result = f"Yoy are in {self.name}\n"
        #handle the items
        result += "You see: "
        for item in self.items.keys():
            result += item + " "
        result += "\n"

        #handle the exists
        result += "Exits: "
        for exit_ in self.exits.keys():
            result += exit_ + " "
        result += "\n"

        return result




        return result
