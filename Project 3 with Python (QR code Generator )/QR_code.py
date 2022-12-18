import qrcode as qr
img = qr.make("https://www.facebook.com/profile.php?id=100009406630517")
img.save("facebook.png")
