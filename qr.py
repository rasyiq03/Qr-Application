import qrcode
import tkinter as tk

# Data yang akan dimasukkan ke dalam QR Code
data = "https://www.w3schools.com/html/html_colors.asp"

root = tk.Tk()
root.title("Coba")

root.geometry("500x500")
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
img.save("qrcode.png")

# Menampilkan QR Code
img.show()

