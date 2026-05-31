import qrcode as qr
import os
import customtkinter as CTK
from customtkinter import *

while True:
    print("THE QRCODE IS GOING TO BE SAVED TO THE PATH YOU ARE RUNNING THIS SCRIPT IN")
    print("""                                                                   
 ,-----.   ,------. ,--.   ,--.  ,---.  ,--. ,--.,------.,------.  
'  .-.  '  |  .--. '|   `.'   | /  O  \ |  .'   /|  .---'|  .--. ' 
|  | |  |  |  '--'.'|  |'.'|  ||  .-.  ||  .   ' |  `--, |  '--'.' 
'  '-'  '-.|  |\  \ |  |   |  ||  | |  ||  |\   \|  `---.|  |\  \  
 `-----'--'`--' '--'`--'   `--'`--' `--'`--' '--'`------'`--' '--' 
                                                                   """)
    link = input("Enter your link here: ").strip()
    ui = input("Enter the name for the file: ")
    if link.startswith("http://") or link.startswith("https://"):
        break
    else:
        print("Please enter a valid link (must start with http:// or https://)")


qr = qr.QRCode(
    version=1,
    error_correction=qr.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

name=f"{ui}.png"
img.save(name)
print(f"Image saved as {name}")
