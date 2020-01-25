

hosts =  r"/etc/hosts"
redirection = "127.0.0.1"
paginas_bloquear = r"txt con los ficheros a bloquear"

with open(paginas_bloquear, "r+") as file:
    content = file.read()

    listaPaginas=content.split("\n")[:-1]

    file.close()


with open(hosts, "r+") as file:
    openhost = file.read()

    for web in listaPaginas:
        if web in openhost:
            pass
        else:
            file.write(redirection + "    " + str(web) + "\n")


