from tkinter import *

def test():
    print("test réussi")

fenetre=Tk()
fenetre.title('Renommage de fichiers')
fenetre.geometry("900x400+400+400")

repertoireString = StringVar()
prefixeString = StringVar()
postfixeString = StringVar()
extensionString = StringVar()
apartirDeString = StringVar()
nomFichierString = StringVar()



lbRepertoire= Label(fenetre, text="nom du répertoire").place(x=410, y=80)
tbRepertoire= Entry(fenetre, textvariable=repertoireString).place(x=400, y=100)

lbPrefixe= Label(fenetre, text="préfixe").place(x=135, y=180)
tbPrefixe= Entry(fenetre, textvariable=prefixeString).place(x=125, y=200)

lbPostfixe= Label(fenetre, text="postfixe").place(x=535, y=180)
tbPostfixe= Entry(fenetre, textvariable=postfixeString).place(x=525, y=200)

lbExtension= Label(fenetre, text="extension concernée").place(x=710, y=180)
tbExtension= Entry(fenetre, textvariable=extensionString).place(x=700, y=200)

lbApartirDe= Label(fenetre, text="à partir de").place(x=30, y=330)
tbApartirDe= Entry(fenetre, textvariable=apartirDeString).place(x=20, y=350)

lbNomFichier= Label(fenetre, text="nom du fichier").place(x=335, y=180)
tbNomFichier= Entry(fenetre, textvariable=nomFichierString).place(x=350, y=220)

value=False
bouton1 = Radiobutton(fenetre, text="Nom original", variable=value, value=False).place(x=335, y=200)
bouton2 = Radiobutton(fenetre, text="", variable=value, value=True).place(x=335, y=220)
tbNomModifier = tbNomFichier= Entry(fenetre, textvariable=nomFichierString).place(x=336, y=220)

lbAmorce= Label(fenetre, text="amorce").place(x=35, y=180)
amorce= Listbox(fenetre)
amorce.pack()
for item in ["aucun","lettre","chiffre"]:
    amorce.insert(END, item)


renommer= Button(fenetre, text='Renommer', command=lambda: test())

#lbRepertoire.pack()
#tbRepertoire.pack()
#lbPrefixe.pack()
#tbPrefixe.pack()
#lbPostfixe.pack()
#tbPostfixe.pack()
#lbExtension.pack()
#tbExtension.pack()
#lbApartirDe.pack()
#tbApartirDe.pack()
#lbNomFichier.pack()
#tbNomFichier.pack()
#bouton1.pack()
#bouton2.pack()
#renommer.pack()
fenetre.mainloop()
