import os


def renomear():
    i = 0
    path = "C:/Users/mattc/Pictures/Camera Roll/"
    for filename in os.listdir(path):
        nome_alterar = "foto" + str(i) + ".jpg"
        diretorio_nomeado = path + filename
        nome_alterado = path + nome_alterar
        os.rename(diretorio_nomeado, nome_alterado)
        i += 1


if __name__ == '__main__':
    renomear()
