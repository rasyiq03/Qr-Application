import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# membuat tampilan
root = tk.Tk()
root.title("Coba")
root.geometry("500x500")

def generate_qr(data, namafile):
    # Buat objek QR Code
    qr = qrcode.QRCode(
        version=1,  # Ukuran QR Code (1 sampai 40, semakin besar semakin kompleks)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Level koreksi error (L, M, Q, H)
        box_size=10,  # Ukuran tiap kotak dalam QR
        border=4,  # Ketebalan border (minimal 4)
    )
    # Tambahkan data ke QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Buat gambar QR Code
    img = qr.make_image(fill="black", back_color="white")

    # Simpan gambar QR Code
    img.save(f"{namafile}.png")
    # Menampilkan QR Code
    # img.show()



def isValid():
    text1 = str(entry1.get())
    text= str(entry.get())
 
    if (text == "") or ( text1 == ""):
        messagebox.showinfo("message box","Harap isi Masukan Url dan Nama File")
    else:
        generate_qr(entry.get(), entry1.get())
        image = Image.open(f"{entry1.get()}.png")  
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        labelg = tk.Label(root, image=photo)
        labelg.place(x= 150, y= 200 )
        messagebox.showinfo("message box","Url Berhasil dibuat")


label = tk.Label(root, text="Masukan Url!")
label.place(x= 220 , y=10 )

entry = tk.Entry(root)
entry.place(x= 200 , y=35 )

label1 = tk.Label(root, text="Masukan Nama file")
label1.place(x= 210 , y= 65 )

entry1 = tk.Entry(root)
entry1.place(x= 200 , y= 90 )

button = tk.Button(root, text="Buat QR Code", command=isValid)
button.place(x= 220 , y= 125 )


root.mainloop()
