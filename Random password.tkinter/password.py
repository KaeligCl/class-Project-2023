from random import*
from tkinter import*

def generate_password():
    generate_password_button.pack_forget()
    password_entry.pack_forget()
    label_title.pack_forget()

#creer la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.config(background='#4065A4')

#creer la frame principale
frame = Frame(window, bg='#4065A4')

#creer une sous boite
right_frame = Frame(frame, bg='#4065A4')

#creer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

#creer un champs/entrée/input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

#creer un bouton
generate_password_button = Button(right_frame, text="Entrer", font=("Helvetica", 20), bg='#4065A4', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

#on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)

#afficher la frame
frame.pack(expand=YES)

width = 300
height = 300
image = PhotoImage(file="R.png").zoom(5).subsample(10)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)

#creation d'une barre de menu
menu_bar = Menu(window)

#configurer notrre fenetre pour ajouter cette menu bar
window.config(menu=menu_bar)

# afficher la fenetre
window.mainloop()