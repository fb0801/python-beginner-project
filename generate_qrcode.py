import qrcode
import tkinter



def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color="black", black_color="white")
    #img.save("qrimg.png")

    name = input("Enter name of file: ")
    
    qcode = img.save(f'{name}.png')

url =input("Enter your link: ")
generate_qrcode(url)