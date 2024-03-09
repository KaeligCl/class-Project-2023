from random import *
import string
from tkinter import *

background_color = '#004958'
bouton_color = '#4b5e65'

dict_leter = []
# dictionnaire de lettre vers morse
MORSE_CODE_DICT = {'a': '.-', 'b': '-...',
                   'c': '-.-.', 'd': '-..', 'e': '.',
                   'f': '..-.', 'g': '--.', 'h': '....',
                   'i': '..', 'j': '.---', 'k': '-.-',
                   'l': '.-..', 'm': '--', 'n': '-.',
                   'o': '---', 'p': '.--.', 'q': '--.-',
                   'r': '.-.', 's': '...', 't': '-',
                   'u': '..-', 'v': '...-', 'w': '.--',
                   'x': '-..-', 'y': '-.--', 'z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}

# dictionnaire de morse vers lettre
MORSE_CODE_DICT_inverse = {}
for keys,values in MORSE_CODE_DICT.items():
    MORSE_CODE_DICT_inverse[values] = keys


# traduction des lettres au morse
def fr_trad():
    global fr_trad_entry
    
    # supprime tout ce qu'il a dans dict_leter
    dict_leter.clear()
    # séparer chaque lettre du mot
    split_word = list(fr_trad_entry)
    # transforme toute les majuscule en minuscule
    for i in split_word:
        num_i = 0
        if ord(i) <= 90 and ord(i) >= 65:
            num_i += ord(i) + 32
        else:
            num_i += ord(i)
        dict_leter.append(chr(num_i))
    
    # traduction
    fr_trad_entry = ""
    # verifie chaque lettre du dict avec chaque lettre de dict_leter
    for letter in dict_leter:
        for values, trad in MORSE_CODE_DICT.items():
            # si il y a la meme lettre du dict et la lettre de dict_leter, on ajoute la traduction en morse dans fr_trad_entry
            if letter == values:
                fr_trad_entry += trad + " "
    # affiche la phrase en morse et la phrase en lettre dans le terminal
    print(fr_trad_entry)
    print(dict_leter)


# traduction du morse au lettre
def morse_trad():
    global morse_trad_entry
    global dict_leter
    
    # supprime tout ce qu'il a dans dict_leter
    dict_leter.clear()
    # sépare chaque séquancage de morse (sépare à chaque éspace)
    split_word = morse_trad_entry.split()
    # incrémente split_word à dict_leter
    dict_leter += split_word
    
    # traduction
    morse_trad_entry = ""
    for word in dict_leter:
        # verifie chaque mot du dict avec chaque lettre de dict_leter_inverse
        for values, trad in MORSE_CODE_DICT_inverse.items():
            if word == values:
                morse_trad_entry += trad
    # affiche la phrase en morse et la phrase en lettre dans le terminal
    print(morse_trad_entry)
    print(dict_leter)


def recuperer_entry():
    # initialise les deux variables pour qu'elles puissent etre changée partout
    global fr_trad_entry
    global morse_trad_entry
    # si on a entré un caractère dans le champ n°1
    if entry == True:
        # si il y a quelque chose dans le champ de morse_entry
        if morse_entry.get() != "":
            # tout supprimer dans le champ morse_entry
            morse_entry.delete(0, END)
        # enregistre ce qu'il y a dans le champ fr_entry et l'enregistre dans fr_trad_entry
        fr_trad_entry = fr_entry.get()
        # appel la fonction fr_trad()
        fr_trad()
        # insert dans le morse_entry ce qu'il y a été traduit par le fr_trad
        morse_entry.insert(0, fr_trad_entry)
    # si on a entré un caractère dans le champ n°2
    else:
        # si il y a quelque chose dans le champ de fr_entry
        if fr_entry.get() != "":
            # tout supprimer dans le champ fr_entry
            fr_entry.delete(0, END)
        # enregistre ce qu'il y a dans le champ morse_entry et l'enregistre dans morse_trad_entry
        morse_trad_entry = morse_entry.get()
        # appel la fonction morse_trad()
        morse_trad()
        # insert dans le fr_entry ce qu'il y a été traduit par le morse_trad
        fr_entry.insert(0, morse_trad_entry)

def witch_entry_1(event):
    # si on a entré un caractère dans le champ n°1
    global entry
    if fr_entry.get() != "":
        entry = True
    else:
        entry = False
    
def witch_entry_2(event):
    # si on a entré un caractère dans le champ n°2
    global entry
    if morse_entry.get() != "":
        entry = False
    else:
        entry = True

def reset_entry():
    # efface les deux champs
    morse_entry.delete(0, END)
    fr_entry.delete(0, END)


# creer la fenetre
window = Tk()
# nom de la fenetre
window.title("Morse traduction")
# teille de la fenetre
window.geometry("720x480")
# couleur de fond de la fenetre
window.config(background=background_color)

# creer la frame principale
frame = Frame(window, bg=background_color, padx=10, pady=10)
# creer une sous boite
right_frame = Frame(frame, bg=background_color, padx=10, pady=10)

# creer un titre
label_title = Label(right_frame, text="Morse traduction", font=("Helvetica", 20), bg=background_color, fg='white')
# afficher le label
label_title.pack()

# creer un champs/entrée/input
fr_entry = Entry(right_frame, font=("Helvetica", 20), bg=background_color, fg='white')
# afficher le champs avec des contour
fr_entry.pack(padx=5, pady=5)
# 
fr_entry.bind("<KeyRelease>", witch_entry_1)

# creer un bouton traduire
translate_button = Button(right_frame, text="Traduire", font=(
    "Helvetica", 20), bg=bouton_color, fg='white', command=recuperer_entry)
translate_button.pack(fill=X)

# creer un champs/entrée/input
morse_entry = Entry(right_frame, font=(
    "Helvetica", 20), bg=background_color, fg='white')
morse_entry.pack(padx=5, pady=5)
morse_entry.bind("<KeyRelease>", witch_entry_2)

# creer un bouton reset
reset_button = Button(right_frame, text="Reset", font=(
    "Helvetica", 20), bg=bouton_color, fg='white', command=reset_entry)
reset_button.pack(fill=X)

# on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# afficher la fenetre
window.mainloop()