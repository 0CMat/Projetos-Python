# install pip
# install pip qrcode
# install  pip install pillow

import qrcode  # importando o QRCode
from PIL import Image  # Importando o Image do PIL

chosen_logo = 'logo.png'  # Logomarca desejada

# Setando a imagem desejada
logo = Image.open('QRCode\ocmat JPG.png')

basewidth = 100  # Setando o local da logo

# Ajuste da imagem
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# Inserção da URL ou TEXTO
content = 'https://github.com/0CMat'

# Inserindo conteudo ao QRCode
QRcode.add_data(content)

# Gerando o QRCode
QRcode.make()

# Setando uma váriavel para a cor do QRCode
QRcolor = 'White'

# Adcionando cor ao QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="Black").convert('RGB')

# Setando tamanho do QRCode
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# Como deve ser salvo o QRCode
QRimg.save('0Cmat_QR.png')

print('QRCode Gerado!')

img = qrcode.make('https://github.com/0CMat')
img.save('QRCode/0CMatCode.png')
