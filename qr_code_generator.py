 #  Generate QR code
import qrcode    #liberary code must import
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
data = "I am learning Python."
qr.add_data('data')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr-code.png")  #if code is not run by image,the install "pip install image"extension.
