from tkinter import Tk
from game import Game

window = Tk()
window.title("Room Adventure... Reloaded")
game = Game(window)
game.play()
window.mainloop()