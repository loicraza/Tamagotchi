# FONCTIONS
from logging import root
import time
from tkinter import DISABLED, messagebox

import lib.outils as outils


def desactiverBoutons(p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir):
    """ grise les boutons  """
    p_btn_manger['state'] == DISABLED
    p_btn_boire['state'] == DISABLED
    p_btn_jouer['state'] == DISABLED
    p_btn_dormir['state'] == DISABLED


def mortFaim(fenetre, p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir):
    desactiverBoutons(p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir)
    messagebox.showerror("Game Over", "Votre tamagochi est mort de faim")
    fenetre.destroy()


def mortSoif(fenetre, p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir):
    desactiverBoutons(p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir)
    messagebox.showerror("Game Over", "Votre tamagochi est mort de soif")
    fenetre.destroy()


def mortPoids(fenetre, p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir):
    desactiverBoutons(p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir)
    fenetre.destroy()


def incrementerSommeil(progressBar, p_iv_dormir):
    p_iv_dormir.set(10)
    progressBar['value'] = 100
    progressBar['style'] = "green.Horizontal.TProgressbar"


def incrementer(progressBar, iv):
    ''' incremente la bar d'etat '''
    if iv.get() < 10:
        iv.set(iv.get() + 1)

    if progressBar['value'] < 100:
        progressBar['value'] += 10

    if progressBar['value'] > 30:                                       # 40<x<80
        progressBar['style'] = "orange.Horizontal.TProgressbar"
    if progressBar['value'] > 60:
        progressBar['style'] = "green.Horizontal.TProgressbar"


def decrementerPoids(fenetre, p_iv_poids, valeur, delai):
    """ Fait décremtenter le poids """
    p_iv_poids.set(p_iv_poids.get()-valeur)
    fenetre.after(delai, lambda: decrementerPoids(
        fenetre, p_iv_poids, valeur, delai))


def decrementer(fenetre, progressBar, iv, valeur, delai, p_iv_manger, p_iv_boire, p_iv_poids, p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir):
    """ permet de decrementer la faim, la soif, le sommeil, le divertissement et le poids """
    if p_iv_manger.get() == 0:
        mortFaim(fenetre, p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir)
    elif p_iv_boire.get() == 0:
        mortSoif(fenetre, p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir)
    elif p_iv_poids.get() > 100:
        messagebox.showerror(
            "Game Over", "Votre tamagochi est mort de surpoids")
        mortPoids(fenetre, p_btn_manger, p_btn_boire,
                  p_btn_jouer, p_btn_dormir)
    elif p_iv_poids.get() < 20:
        messagebox.showerror(
            "Game Over", "Votre tamagochi est mort de sous poids")
        mortPoids(fenetre, p_btn_manger, p_btn_boire,
                  p_btn_jouer, p_btn_dormir)

    if iv.get() > 0:
        iv.set(iv.get()-valeur)

    """ if p_iv_manger.get() < 4:
        decrementerPoids(fenetre, p_iv_poids, 1, 1000) """
        
        
    if progressBar['value'] > 0:
        progressBar['value'] -= 10

    if progressBar['value'] < 70:
        progressBar['style'] = "orange.Horizontal.TProgressbar"
    if progressBar['value'] < 40:
        progressBar['style'] = "red.Horizontal.TProgressbar"

    fenetre.after(delai, lambda: decrementer(
        fenetre, progressBar, iv, valeur, delai, p_iv_manger, p_iv_boire, p_iv_poids, p_btn_manger, p_btn_boire, p_btn_jouer, p_btn_dormir))

def manger(progressBar, p_iv_poids, p_iv_manger, canvas, images):
    ''' fait manger le tamagotchi '''
    outils.setstatusImage(canvas, images, "manger")
    incrementer(progressBar, p_iv_manger)
    p_iv_poids.set(p_iv_poids.get() + 1)
    # un pop up pour lui dire qu'il n'a plus faim
    if p_iv_manger.get() == 10:
        messagebox.showinfo(
            "message", "Votre tamagochi n'a plus faim")


def boire(progressBar, p_iv_boire, canvas, images):
    ''' fait boire le tamagotchi '''
    outils.setstatusImage(canvas, images, "boire")
    incrementer(progressBar, p_iv_boire)
    if p_iv_boire.get() == 10:
        messagebox.showinfo(
            "message", "Votre tamagochi n'a plus soif")

def dormir(progressBar, p_iv_dormir,canvas, images):
    ''' fait dormir le tamagotchi '''
    outils.setstatusImage(canvas, images, "dormir")
    incrementerSommeil(progressBar, p_iv_dormir)
    if p_iv_dormir.get() == 10:
        messagebox.showinfo(
            "message", "Votre tamagochi est en pleine forme !")


def jouer(progressBar, p_iv_jouer, p_iv_poids, canvas, images):
    ''' fait jouer le tamagotchi '''
    outils.setstatusImage(canvas, images, "jouer")
    incrementer(progressBar, p_iv_jouer)
    if p_iv_poids.get() > 50: 
        p_iv_poids.set(p_iv_poids.get() - 1)

    # fenetre.after(5000, lambda:)
    # fenetre.after(5000, lambda:decrementer(fenetre, progressBar, iv_manger, 1, 1000))
    # fenetre.after_cancel(w)
