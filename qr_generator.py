#!/usr/bin/env python3

import qrcode

def crear_qr(texto, nombre_archivo):
    qr = qrcode.make(texto)
    qr.save(nombre_archivo+".png")

nombre_archivo = input("Ingrese el nombre del archivo: ")
texto = input("Ingrese la dirección URL para crear su codigo QR: ")
crear_qr(texto, nombre_archivo)
print(f"El código QR ha sido creado y guardado como {nombre_archivo}.png")
print("Codigo QR guaradado en: /home/kali/Documentos/Codigos QR")