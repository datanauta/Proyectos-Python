import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=7,
    border=2
)

qr.add_data('https://google.com')
qr.make(fit=True)

# Corrección aquí: back_color, no black_color
img = qr.make_image(fill_color='black', back_color='white')
img.save('google.png')
