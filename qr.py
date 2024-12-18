import qrcode

# Replace with your project IP
project_ip = "http://127.0.0.1:5000"  # Example local IP with port

# Generate QR codeen
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(project_ip)
qr.make(fit=True)

# Save the QR code image
qr_img = qr.make_image(fill="black", back_color="white")
qr_img.save("project_ip_qr.png")

print("QR code generated and saved as 'project_ip_qr.png'")
