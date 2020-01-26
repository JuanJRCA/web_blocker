import tkinter
import os


class Gui():
    '''Sencilla interfaz gráfica. Se inicializa con una pantalla de tkinter.'''
    def __init__(self, root):
        self.redirection = "127.0.0.1"
        self.path = str(os.path.abspath("blocked_urls.txt"))
        self.hosts = r"/etc/hosts"
        self.data = []

        startLabel = tkinter.Label(root, text="Introduce la web que deseas bloquear: ")
        startLabel.pack()
        self.startEntry = tkinter.Entry(root)
        self.startEntry.pack()
        self.original = self.startEntry

        plotButton = tkinter.Button(root, text="Confirmar", command=self.input_data)
        plotButton.pack()

    def escribir_documento_txt(self):
        ''' Escribe en el documento txt y en hosts la web introducida.'''
        with open(self.path, "r+") as documentoWebs:
            webs = documentoWebs.read()
            for x in self.data:
                if x in webs:
                    pass
                else:
                    documentoWebs.write(x+"\n")
            documentoWebs.close()

        with open(self.hosts, "r+") as hosts:
            websBlocked = hosts.read()
            for x in self.data:
                if x in websBlocked:
                    pass
                else:
                    hosts.write((self.redirection + "    " + str(x) + "\n"))
            hosts.close()

    def input_data(self):
        ''' Recoge la información introducida por el usuario una vez pinchado el button'''
        if self.startEntry.get() == "":
            print("No has introducido ninguna web")
            pass
        else:

            self.data.append(self.startEntry.get())
            self.escribir_documento_txt()
            print("La siguiente web ha sido bloqueada : {}".format(self.data[-1]))
        self.startEntry = self.startEntry.delete(0, 'end')
        self.startEntry = self.original


