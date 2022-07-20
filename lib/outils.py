from tkinter import RIGHT, messagebox

def setstatusImage(canvas,images,status):
    """ Changer d'image """
    canvas.delete("all")
    canvas.create_image(150,150,image=images[status])

def changer(show_frame, hide_frame):
    """ Changer de frame """
    hide_frame.grid_remove()
    show_frame.grid()

def montrer(frame):
    frame.pack(side=RIGHT)

def cacher(frame):
    frame.pack_forget()

def vieillir(fenetre, iv, label, valeur, delai):
    ''' Fait vieillir le tamagotchi '''
    iv.set(iv.get() + valeur)
    if iv.get() == 5:
        messagebox.showinfo("Evolution", "Votre tamagochi est maintenant adulte")
    elif iv.get() == 15:
        messagebox.showinfo("Evolution", "Votre tamagochi est maintenant vieux")
    elif iv.get() > 20:
        messagebox.showerror("Game Over", "Votre tamagochi est mort de vieillesse")
        fenetre.destroy()
    fenetre.after(delai, lambda: vieillir(fenetre, iv, label, valeur, delai))
