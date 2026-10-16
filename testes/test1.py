#import cv2
#import qrcode 
#
#codigo = "0123"
#
#imagem = qrcode.make(codigo)
#imagem.save("testes/2.png")
#
#leitor = cv2.QRCodeDetector()
#
#imagem = cv2.imread("testes/2.png")
#
#codigo, pontos,_ = leitor.detectAndDecode(imagem)
#
#print(codigo)
#
#a = open(f"testes/{codigo}.txt")
#
#for n in a:
#    print(n)

import pdfplumber

with pdfplumber.open("testes/documento_ficticio.pdf") as pdf:
    pagina = pdf.pages[0]
    texto = pagina.extract_text()

print(texto)