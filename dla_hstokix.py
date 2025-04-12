from customtkinter import*
from PIL import Image
from socket import *
import threading 
client = socket(AF_INET,SOCK_STREAM)

client.connect(("0.tcp.eu.ngrok.io", 14202))





Window = CTk()

Window.geometry("400x500")

Window.title("Общяга")

Window.configure(fg_color = "blue")

load_image = Image.open("send.jpg")
ready_image = CTkImage(light_image=load_image,size=(20,20))

frum =CTkFrame(Window, width= 250, height=270)
frum.pack_propagate(False)
frum.pack(pady=20)
frum2=CTkFrame(Window, width= 200, height=190)
frum2.pack_propagate(False)


def click():
    enutry = entry.get()
    entry.delete(0,END)

    Text_but.configure(state="normal")
    Text_but.insert(END, enutry + "\n")
    Text_but.configure(state="disabled")

    client.send(f"Victor+Kapneplod" + enutry.encode())
    


def prinimanie_sms():
    while True:
        try:
            a = client.recv(1024).decode()
            Text_but.configure(state="normal")
            Text_but.insert(END, a + "\n")
            Text_but.configure(state="disabled")
        except:
            pass
threading.Thread(target= prinimanie_sms).start()




but = CTkButton(frum2, text="Отправить",image = ready_image,command=click,compound="left", width= 90,height=38)
but.pack()
frum2.pack(pady=20)

entry = CTkEntry(frum2,placeholder_text="Ведите собшение" ,width=70,height=50)
entry.pack(pady=20, padx= 10)
Text_but = CTkTextbox(frum)
Text_but.configure(state="disabled")

Text_but.pack()



Window.mainloop()