# install pip
# install pip qrcode
# install  pip install pillow

import qrcode # importando o QRCode
from PIL import Image  # Importando o Image do PIL

img = qrcode.make('https://github.com/0CMat')
img.save('0CMatCod2.png')

print('QRCode gerado com sucesso!')
