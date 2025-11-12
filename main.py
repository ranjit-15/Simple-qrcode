'''

import qrcode

url = input("Enter the URL to generate QR code: ").strip()
file_path = input("Enter the file path to save the QR code image (e.g., qr_code.png): ").strip()

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)
print(f"QR code saved to {file_path}")

'''

import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Get inputs
url = input("Enter the URL or text to generate QR code: ").strip()
file_path = input("Enter file name to save (e.g., qr_code.png): ").strip()

try:
    # Create QRCode object with better control
    qr = qrcode.QRCode(
        version=1,  # 1–40 (controls size). 1 is smallest
        error_correction=ERROR_CORRECT_H,  # better error correction
        box_size=10,  # pixel size of each box
        border=4,  # border size
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Create an image (black QR on white background)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(file_path)
    print(f"✅ QR code successfully saved to {file_path}")

except Exception as e:
    print(f"❌ Something went wrong: {e}")
