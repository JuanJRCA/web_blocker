directionBloquearUrls = r"path fichero txt con las páginas a bloquear"
def bloquear_paginas(*args):
    with open(directionBloquearUrls, "r+") as file:
        content = file.read()

        for x in args:
            if x in content:
                pass
            else:
                file.write(x+"\n")



