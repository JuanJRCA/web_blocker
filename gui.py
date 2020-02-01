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

        self.frame_message = tkinter.Frame(root)
        self.frame_message.pack()
        self.Label = tkinter.Label(master=self.frame_message, text=None)
        self.Label.pack(side=tkinter.BOTTOM)

    def unblock_website(self):
        '''It unblocks the website that the user
        has introduced'''

        self._input_entry()

        if not self.document_handler._is_correct_web_name():
            self.Label["text"] = "No has añadido ninguna web"

        else:
            if self.document_handler._check_if_data_in_file():
                self.document_handler.delete_web_from_host_to_unblock()
                self.Label["text"] = " Has desbloqueado {}".format(self.document_handler.data)
            else:
                self.Label["text"] = "{} no estaba bloqueado".format(self.document_handler.data)

    def block_website(self):
        ''' It blocks the website that the user
        has introduced'''

        self._input_entry()
        if not self.document_handler._is_correct_web_name():
            self.Label["text"] = "No has añadido ninguna web"
        else:
            if not(self.document_handler._check_if_data_in_file()):
                self.document_handler.add_website_to_hosts_to_block()
                self.Label["text"] = " Has bloqueado {}".format(self.document_handler.data)
            else:
                self.Label["text"] = "{} ya estaba bloqueado".format(self.document_handler.data)

    def _input_entry(self):

        original = self.start_entry

        self.document_handler.data = self.start_entry.get()

        self.start_entry = self.start_entry.delete(0, 'end')
        self.start_entry = original





