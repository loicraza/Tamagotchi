from cProfile import label
from cgitb import text
from logging import root
import sys
from textwrap import fill
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
""" from PIL import Image, ImageTk  """  # pour recentrer l'image

import lib.actions as actions
import lib.outils as outils

# la fenêtre
ma_fenetre = Tk()
ma_fenetre.geometry('700x550')
ma_fenetre.title('Tamagotchi')

# permet de définir les styles qui seront utilisés dans la Progressbar
style = Style()
style.theme_use('alt')
style.configure("green.Horizontal.TProgressbar",
                foreground='green',  background='green')
style.configure("orange.Horizontal.TProgressbar",
                foreground='orange', background='orange')
style.configure("red.Horizontal.TProgressbar",
                foreground='red',    background='red')

# images
images ={
    "manger": PhotoImage(file=sys.path[0] +'/images/Tamagotchi_mange.png'),
    "boire": PhotoImage(file=sys.path[0] +'/images/Tamagotchi_boit.png'),
    "dormir": PhotoImage(file=sys.path[0] +'/images/Tamagotchi_dort.png'),
    "jouer": PhotoImage(file=sys.path[0] +'/images/Tamagotchi_joue.png')
}




################# CONNEXION ########################
#premier cadre de l'acueil
frm_connexion = Frame(ma_fenetre, width=40, height=40, bd=5, bg="pink")  


can1 = Canvas(frm_connexion, width=150, height=150, bg='white')
photo = PhotoImage(file=sys.path[0] + "/images/photo_tama.png")

item = can1.create_image(150, 150, image=photo)

mon_label = Label(frm_connexion, text='Quel est le nom de votre Tamagotchi ? :')

sv_nom = StringVar()

#le champ pour saisir le nom de son tamagochi
mon_champ = Entry(frm_connexion, textvariable=sv_nom)  
bouton_valider = Button(frm_connexion, text="Valider", command= lambda : outils.changer(frm_connexion, mon_cadre1))

frm_connexion.pack()
can1.grid()
mon_label.grid()
mon_champ.grid()
bouton_valider.grid()

################ ACCUEIL ###################
mon_cadre1 = Frame(ma_fenetre, bd=2)
can_tamagotchi = Canvas(ma_fenetre, width=700, height=300, bg='white')
btn_etat = Button(mon_cadre1, text="Voir l'état", command=lambda : outils.montrer(frm_etat))

can_tamagotchi.create_image(150, 150, image=photo)

# faim
iv_manger = IntVar()
iv_manger.set(5)
btn_manger = Button(mon_cadre1, text="Manger",
                    command=lambda: actions.manger(bar_faim, iv_poids, iv_manger, can_tamagotchi, images))
lbl_manger = Label(mon_cadre1, textvariable=str(iv_manger))
bar_faim = Progressbar(mon_cadre1, orient=HORIZONTAL, length=100,
                       mode="determinate", value=60, style="orange.Horizontal.TProgressbar")

# boire
iv_boire = IntVar()
iv_boire.set(5)
btn_boire = Button(mon_cadre1, text="Boire", command=lambda: actions.boire(bar_boire, iv_boire, can_tamagotchi, images))
lbl_boire = Label(mon_cadre1, textvariable=str(iv_boire))
bar_boire = Progressbar(mon_cadre1, orient=HORIZONTAL, length=100,
                        mode="determinate", value=60, style="orange.Horizontal.TProgressbar")


# dormir
iv_dormir = IntVar()
iv_dormir.set(5)
btn_dormir = Button(mon_cadre1, text="Dormir",
                    command=lambda: actions.dormir(bar_dormir, iv_dormir, can_tamagotchi, images))
lbl_dormir = Label(mon_cadre1, textvariable=str(iv_dormir))
bar_dormir = Progressbar(mon_cadre1, orient=HORIZONTAL, length=100,
                         mode="determinate", value=60, style="orange.Horizontal.TProgressbar")

# jouer
iv_jouer = IntVar()
iv_jouer.set(5)
lbl_jouer = Label(mon_cadre1, textvariable=str(iv_jouer))
btn_jouer = Button(mon_cadre1, text="Jouer", command=lambda: actions.jouer(bar_jouer, iv_jouer, iv_poids, can_tamagotchi, images))
bar_jouer = Progressbar(mon_cadre1, orient=HORIZONTAL, length=100,
                        mode="determinate", value=60, style="orange.Horizontal.TProgressbar")




########## ETATS #############
# poids
frm_etat = Frame(ma_fenetre, bd=2)
iv_poids = IntVar()
iv_poids.set(50)
lbl_libelle_poids = Label(frm_etat, text="Poids : ")
lbl_poids = Label(frm_etat, textvariable=str(iv_poids))


# age à définir...
iv_age = IntVar()
iv_age.set(0)
lbl_libelle_age = Label(frm_etat, text="Age : ")
lbl_age = Label(frm_etat, textvariable=str(iv_age))

# nom
sv_nom.set(sv_nom.get())
lbl_libelle_nom = Label(frm_etat, textvariable=sv_nom)

btn_fermer = Button(frm_etat, text="Fermer", command=lambda: outils.cacher(frm_etat))

outils.vieillir(ma_fenetre, iv_age, lbl_age, 1, 10000)
actions.decrementer(ma_fenetre, bar_faim, iv_manger, 1, 10000, iv_manger, iv_boire, iv_poids, btn_manger, btn_boire, btn_jouer, btn_dormir)
actions.decrementer(ma_fenetre, bar_boire, iv_boire, 1, 10000, iv_manger, iv_boire, iv_poids, btn_manger, btn_boire, btn_jouer, btn_dormir)
actions.decrementer(ma_fenetre, bar_dormir, iv_dormir, 1, 10000, iv_manger, iv_boire, iv_poids, btn_manger, btn_boire, btn_jouer, btn_dormir)
actions.decrementer(ma_fenetre, bar_jouer, iv_jouer, 1, 10000, iv_manger, iv_boire, iv_poids, btn_manger, btn_boire, btn_jouer, btn_dormir)


# grid (dans la fênetre)/pack(dans les cadres)
can_tamagotchi.pack()
mon_cadre1.pack(pady=20)

btn_manger.grid(row=1, column=1, padx=10, pady=5)
bar_faim.grid(row=2, column=1, padx=10, pady=10)
lbl_manger.grid(row=3, column=1, padx=10)

btn_boire.grid(row=1, column=2, padx=10, pady=5)
bar_boire.grid(row=2, column=2, padx=10, pady=10)
lbl_boire.grid(row=3, column=2, padx=10)

btn_dormir.grid(row=1, column=3, padx=10, pady=5)
bar_dormir.grid(row=2, column=3, padx=10, pady=10)
lbl_dormir.grid(row=3, column=3, padx=10)

btn_jouer.grid(row=1, column=4, padx=10, pady=5)
bar_jouer.grid(row=2, column=4, padx=10, pady=10)
lbl_jouer.grid(row=3, column=4, padx=10)


btn_etat.grid(row=1, column=5, columnspan=2)
lbl_libelle_nom.grid(row=2, column=1, columnspan=2)
lbl_libelle_age.grid(row=3, column=1, padx=10)
lbl_age.grid(row=3, column=2)

lbl_libelle_poids.grid(row=4, column=1, padx=10)
lbl_poids.grid(row=4, column=2, padx=10)

btn_fermer.grid(row=5, column=1, columnspan=2)

ma_fenetre.mainloop()
