import os
import tkinter
from DocumentManager import DocumentManager

class Gui():
    '''Graphical interface made with Tkinter. The websites introduced by the
    user is saved and written in other files to block the website.'''

    def __init__(self, root):

        ''' Creates the Tkinter Interface '''

        self.document_handler = DocumentManager()
        self.Frame = tkinter.Frame(root)
        self.Frame.pack()
        start_msg = "Enter a web:"
        start_label = tkinter.Label(master=self.Frame, text=start_msg)
        start_label.pack()

        self.start_entry = tkinter.Entry(self.Frame)
        self.start_entry.pack()

        plot_block_button = tkinter.Button(master=self.Frame,
                                           text="  Block  ",
                                           command=lambda:
                                           self.block_website())

        plot_block_button.pack(side=tkinter.LEFT)
        plot_unblock_button = tkinter.Button(self.Frame,
                                             text="Unblock",
                                             command=lambda:
                                             self.unblock_website())
        plot_unblock_button.pack(side=tkinter.LEFT)

        self.Frame2 = tkinter.Frame(root)
        self.Frame2.pack()
        self.Label = tkinter.Label(master=self.Frame2, text=None)
        self.Label.pack(side=tkinter.BOTTOM)

    def unblock_website(self):
        '''It unblocks the website that the user
        has introduced'''

        self._input_entry()

        if self.document_handler.data == "" or "." not in self.document_handler.data:
            print("No has introducido ninguna web")
        else:
            self.document_handler.delete_web_from_document()
            print("La siguiente web será desbloqueada", self.document_handler.data)
            self.Label["text"] = " Has desbloqueado {}".format(self.document_handler.data)

    def block_website(self):
        ''' It blocks the website that the user
        has introduced'''

        self._input_entry()
        if not self.document_handler.data or "." not in self.document_handler.data:
            print("No has introducido ninguna web")
        else:
            self.document_handler.write_web_in_document()
            print("La siguiente web será bloqueada", self.document_handler.data)
            self.Label["text"] = " Has bloqueado {}".format(self.document_handler.data)

    def _input_entry(self):

        original = self.start_entry

        self.document_handler.data = self.start_entry.get()
        self.start_entry = self.start_entry.delete(0, 'end')
        self.start_entry = original




