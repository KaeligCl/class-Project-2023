import time
import threading
from random import *
from tkinter import *
from decimal import *


def generate_cookie():
    global cookie
    cookie += cookie_damage
    cookie_conteur.config(text=cookie)


def shop_cookie():
    global generate_cookie_home_button
    global generate_upgrade1_button
    global upgrade1_info
    global current_cookie
    global generate_upgrade2_button
    global upgrade2_info
    # tout caché
    generate_cookie_button.pack_forget()
    generate_shop_button.pack_forget()
    cookie_conteur.pack_forget()
    generate_achivement_button.pack_forget()

    # créer le label de cookie actuel
    current_cookie = Label(text="cookie actuel:"+str(cookie)+"",
                           font=("Helvetica", 40), bg='#928429', fg='white')
    current_cookie.place(x=100, y=50)

    # créer le bouton returne
    generate_cookie_home_button = Button(text="home", font=(
        "Helvetica", 20), bg='#928429', fg='white', command=home_cookie)
    generate_cookie_home_button.place(x=300, y=600)

    # créer l'amélioration des dégats
    generate_upgrade1_button = Button(frame, text="More damage", font=(
        "Helvetica", 20), bg='#928429', fg='white', command=upgrade1_cookie)
    generate_upgrade1_button.place(x=0, y=150)
    # info du cout de dégats
    upgrade1_info = Label(frame, text="cout actuel:"+str(upgrade1_price) +
                          "", font=("Helvetica", 10), bg='#928429', fg='white')
    upgrade1_info.place(x=0, y=225)

    # créer un bot qui créer automatiquement des cookie
    generate_upgrade2_button = Button(frame, text="Auto-cookie", font=(
        "Helvetica", 20), bg='#928429', fg='white', command=upgrade2_cookie)
    generate_upgrade2_button.place(x=300, y=150)
    # info du cout du robot
    upgrade2_info = Label(frame, text="cout actuel:"+str(upgrade2_price) +
                          "", font=("Helvetica", 10), bg='#928429', fg='white')
    upgrade2_info.place(x=300, y=225)


def home_cookie():
    current_cookie.place_forget()
    generate_cookie_home_button.place_forget()
    generate_upgrade1_button.place_forget()
    upgrade1_info.place_forget()
    generate_upgrade2_button.place_forget()
    upgrade2_info.place_forget()

    generate_cookie_button.pack()
    cookie_conteur.pack()
    generate_shop_button.pack()
    generate_achivement_button.pack()
    cookie_conteur.config(text=cookie)


def clignotement():
    # creer un clignotement si il n'y pas assez de cookie
    global text_color
    global number_of_clignotement
    if text_color:
        current_cookie.config(fg="#B63434")
    else:
        current_cookie.config(fg="white")

    text_color = not text_color
    number_of_clignotement = number_of_clignotement + 1
    if number_of_clignotement == 8:
        number_of_clignotement = 0
        return
    frame.after(75, clignotement)


def upgrade1_cookie():
    # amélioration du nombre de cookie produit
    global cookie
    global upgrade1_price
    global cookie_damage
    global cookie_conteur
    if cookie >= upgrade1_price:
        cookie_damage = cookie_damage*2
        cookie = cookie-upgrade1_price
        upgrade1_price = upgrade1_price*4
        current_cookie.config(text="cookie actuel:"+str(cookie)+"")
        upgrade1_info.config(text="cout actuel:"+str(upgrade1_price)+"")
    else:
        clignotement()


def upgrade2_cookie():
    # cration d'une cliqueur automatique de cookie
    global cookie
    global upgrade2_price
    global cookie_conteur
    global bot_add_cookie
    if cookie >= upgrade2_price:
        cookie = cookie-upgrade2_price
        upgrade2_price = upgrade2_price*2
        bot_add_cookie = bot_add_cookie*2
        current_cookie.config(text="cookie actuel:"+str(cookie)+"")
        upgrade2_info.config(text="cout actuel:"+str(upgrade2_price)+"")
        threading.Thread(target=bot_cookie).start()
    else:
        clignotement()


def bot_cookie():
    global cookie
    global cookie_damage
    while 1 == 1:
        cookie += int(cookie_damage/4)
        cookie_conteur.config(text=cookie)
        current_cookie.config(text="cookie actuel:"+str(cookie)+"")
        time.sleep(0.100)


def achivement():
    global generate_cookie_home_button_achivement
    global achivement_begener
    global label_achivement
    # tout caché
    generate_cookie_button.pack_forget()
    generate_shop_button.pack_forget()
    cookie_conteur.pack_forget()
    generate_achivement_button.pack_forget()
    # creer le bouton return
    generate_cookie_home_button_achivement = Button(text="home", font=(
        "Helvetica", 20), bg='#928429', fg='white', command=home_cookie_achivement)
    generate_cookie_home_button_achivement.place(x=300, y=600)
    # creer le label achivement
    label_achivement = Label(text="Achivement", font=(
        "Helvetica", 40), bg='#928429', fg='white')
    label_achivement.place(x=200, y=50)


def home_cookie_achivement():
    generate_cookie_home_button_achivement.place_forget()
    label_achivement.place_forget()

    generate_cookie_button.pack()
    cookie_conteur.pack()
    generate_shop_button.pack()
    generate_achivement_button.pack()


# initialisation
text_color = True
number_of_clignotement = 0
cookie_damage = 1
upgrade1_price = 10
upgrade2_price = 100
bot_add_cookie = 10
cookie = 0

# creer la fenetre
window = Tk()
window.title("Cookie cliker")
window.geometry("720x720")
window.minsize(720, 720)
window.maxsize(720, 720)
window.iconbitmap("cookie - Copie.ico")
window.config(background='#928429')

# creer la frame principale
frame = Frame(window, bg='#928429')

# création d'image
width = 500
height = 500
image = PhotoImage(file="cookie.png").zoom(10).subsample(10)

# creer un bouton cookie
generate_cookie_button = Button(frame, image=image, text="Cookie", font=(
    "Helvetica", 20), bg='#928429', fg='white', command=generate_cookie)
generate_cookie_button.pack(fill=X)

# on place la sous boite sous de la frame principal
frame.grid(row=1, column=0, sticky=S)

# creer un conteur
cookie_conteur = Label(frame, text=cookie, font=(
    "Helvetica", 20), bg='#928429', fg='white')
cookie_conteur.pack()

# creer un bouton shop
generate_shop_button = Button(frame, text="shop", font=(
    "Helvetica", 20), bg='#928429', fg='white', command=shop_cookie)
generate_shop_button.pack()

# creer un bouton achivement
generate_achivement_button = Button(frame, text="achivement", font=(
    "Helvetica", 20), bg='#928429', fg='white', command=achivement)
generate_achivement_button.pack()

# afficher la frame
frame.pack(expand=YES)

# afficher la fenetre
window.mainloop()
