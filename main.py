class Player:
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.inventory = []

  def display_status(self):
    print(f"Player: {self.name}")
    print(f"Health: {self.health}")

  def display_inventory(self):
    print(f"Inventory : {self.inventory")

  def take_item(self, item):
    self.inventory.append(item)
    


class Game:
  def __init__(self):
    pass
  
  @staticmethod
  def get_input(prompt):
    return input(prompt)

#game on off
game_on_off = True

#get player's name
player_name = input("please input your name : ")

#make instansce class
player = Player(player_name)
game =Game()

#beggining story
print(
'''
You wake up in a cold, dimly lit dungeon with no memory of how you got there. The damp stone walls echo with eerie whispers, and a sense of foreboding fills the air. As you try to piece together what happened, you realize that escaping this mysterious place is your only hope.
'''
)
print("You try to gather your thoughts, but your mind feels hazy, as if a veil has been cast upon your memories. As you stand up, the metallic clank of chains around your wrists and ankles reverberates through the dungeon. It seems you're not alone in this forsaken place.")
while True:
  