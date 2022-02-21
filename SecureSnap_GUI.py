from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import time
import main
# append your program functions here
# data="abcd"
# enr_data_entry=''


def encrypt():
    encrypt_root = Tk()
    encrypt_root.title("ENRYPTION")
    encrypt_root.minsize(800, 450)
    encrypt_root.maxsize(800, 450)

    l = Label(encrypt_root, text="Secure Snap-ENCRYPTION", relief=SUNKEN, foreground="yellow",
              background="blue", padx=10, pady=5, borderwidth=50)
    l.pack(fill=X)
    l = Label(encrypt_root, text="[*] Maximum bytes to encode: 93750", relief=SUNKEN, foreground="yellow",
              background="blue", padx=10, pady=5, borderwidth=5)
    l.place(x=290,y=150)
    l = Label(encrypt_root, text="Enter Your Data : ")
    l.place(x=210, y=200)
    global data
    data = StringVar()
    global enr_data_entry
    enr_data_entry = Entry(encrypt_root, textvariable=data)
    enr_data_entry.place(x=360, y=200)
    data = enr_data_entry.get()
    dcr = Button(encrypt_root, text="SELECT_IMAGE", fg='black',
                 command=select_image_encryption, height=2, width=10)
    dcr.place(x=350, y=250)
    # window destroying button

    def destroy_window():

        encrypt_root.destroy()

    select_image_button = Button(encrypt_root, text="SUBMIT", fg='black',
                                 command=destroy_window, height=2, width=10)
    select_image_button.place(x=300, y=400)
    cancel_button= Button(encrypt_root, text="cancel", fg='black',
                                command=destroy_window, height=2, width=10)
    cancel_button.place(x=450, y=400)
    encrypt_root.mainloop()


def select_image_encryption():
    data = enr_data_entry.get()
    main.en(data)
    encr_message_root = Tk()
    encr_message_root.title("message")
    l = Label(encr_message_root, text="Your data is encrypted in the image", relief=SUNKEN, foreground="yellow",
            background="black", padx=10, pady=5, borderwidth=50)
    l.pack()
    # destroying after message window

    def destroy_after_window():
        encr_message_root.destroy()
    # destroy_after_window ends here
    ok_button = Button(encr_message_root, text="OK",
                        command=destroy_after_window)
    ok_button.pack()
    
    encr_message_root.mainloop()


def decrypt():
    encrypt_root = Tk()
    encrypt_root.title("DECRYPTION")
    encrypt_root.minsize(800, 600)
    l = Label(encrypt_root, text="Secure Snap-DECRYPTION", relief=SUNKEN, foreground="yellow",
              background="blue", padx=10, pady=5, borderwidth=50)
    l.pack(fill=X)

    def select_image_DECRYPTION():
        d = main.dc()
        l = Label(encrypt_root, text=f"thanks your data is {d}", relief=SUNKEN, foreground="yellow",
                background="black", padx=10, pady=5, borderwidth=10)
        l.place(x=260, y=350)
    # print("thanks your data is encrypted in your image")
        
        def destroy_window():
            encrypt_root.destroy()
        select_image_button = Button(encrypt_root, text="EXIT", fg='black',
                                    command=destroy_window, height=2, width=10)
        select_image_button.place(x=350, y=400)
    # the destroy function ends here
        
    dcr = Button(encrypt_root, text="SELECT_IMAGE", fg='black',
                command=select_image_DECRYPTION, height=2, width=10)
    dcr.place(x=350, y=250)
    def destroy_window_cancel():
            encrypt_root.destroy()
    cancel_button = Button(encrypt_root, text="CACNCEL", fg='black',
                                    command=destroy_window_cancel, height=2, width=10)
    cancel_button.pack(side="bottom")
        
    encrypt_root.mainloop()


root = Tk()
root.title("Secure Snap")
root.minsize(800, 450)
root.maxsize(800, 450)
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
# background image code
image1 = Image.open("securesnap.png")
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test)
label1.image = test
label1.place(x=0, y=0)


# photo = PhotoImage(file="securesnap.png")
# background_photo_label=Label(image=photo)
# background_photo_label.pack()
l = Label(text="Secure Snap", foreground="black", font=fontStyle)
l.place(x=350, y=30)

# canvas_width = 200
# canvas_height = 200
# can_widget = Canvas(root, width=canvas_width, height=canvas_height)
# can_widget.pack()
enr = Button(text='ENCRYPT', fg='blue', background='black',
             command=encrypt, height=2, width=7)
enr.place(x=360, y=200)
# can_widget.create_rectangle(3, 5, 700, 300,fill="")
dcr = Button(text='DECRYPT', fg='blue',
             command=decrypt, height=2, width=7)
dcr.place(x=360, y=250)
root.mainloop()
