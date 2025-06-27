import os,shutil

#inizia la funzione chiedendo che file vuoi spostare
def insert():
    print("Inserire il file da spostare")
    fileName = input()
#directory dove prendera i file e crera le cartelle 
    directory_principale = "C:/Users/SLK/Desktop/FileOrganizer/files"
    os.walk(directory_principale)
    
    cartella_audio = os.path.join(directory_principale, "Aud")
    cartella_documenti = os.path.join(directory_principale, "Docum")
    cartella_immagini = os.path.join(directory_principale, "Imm")
#creazioni delle cartelle se non esistono
    os.makedirs(cartella_audio, exist_ok=True)
    os.makedirs(cartella_documenti, exist_ok=True)
    os.makedirs(cartella_immagini, exist_ok=True)

    find = False
#qui verra scelto il file da spostare in base all estesione 
    for file in os.listdir(directory_principale):

        if file == fileName:
            percorso_file = os.path.join(directory_principale, file)
             
            if file.endswith((".png", ".jpg", ".jpeg")):
                shutil.move(percorso_file,cartella_immagini)
            
            elif file.endswith((".odt", ".txt")):
                shutil.move(percorso_file, cartella_documenti)
               
            elif file.endswith(".mp3"):
                shutil.move(percorso_file,cartella_audio)

            find = True 

    if (find): 
        print ("Il file e stato spostato")
    else:
        print("Il file non e stato trovato")
#funzione dove il cliente puo scegliere se spostare in file o uscie 
def start_program():
    print("Benvenuto utente")
    while True:
        print("Premi 1 per spostare file")
        print("Premi 0 per uscire")
        cmd = input()
        if cmd == "1":
            insert()
        elif cmd =="0":
            break
        else:
            print("Comando non trovato")
            
start_program()


   