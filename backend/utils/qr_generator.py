# backend/utils/qr_generator.py
import qrcode

def generate_qr(data: str, path: str = "qrcode.png"):
    img = qrcode.make(data)
    img.save(path)
    return path
