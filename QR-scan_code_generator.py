import pyqrcode
import time
from pyzbar.pyzbar import decode
from PIL import Image

while 1:
    print("What do you want :\n1.Generate QRCode(Press 1) \n2.Scan QR Code(Press 2)")
    sa = int(input("Enter your choice: "))

    if sa == 1:
        sen = input("Enter text or URL address: ")
        qr = pyqrcode.create(sen)
        file = input("Give a title to your QR Code: ")
        qr.png(f"{file}.png", scale=8)
        time.sleep(3)
        print("Successfully generated...")

    elif sa == 2:
        say = input("Which file do you want to Scan: ")
        a = decode(Image.open(f'{say}.png'))
        print("Scannig...")
        time.sleep(3)

        print(f'\n Text Scanned: {a[0][0]}')

    else:
        print('Invalid choice! Please type 1 or 2.')

    command = input('Do you want to continue: [Yes/No]').lower()

    if command == "yes":
        continue
    else:
        exit()

