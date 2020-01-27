import os
import tkinter
class Gui():

    '''Graphical interface made with Tkinter. The websites introduced by the
    user is saved and written in other files to block the website.'''

    def __init__(self, root):

        ''' Initialize the path of the hosts, the redirection value, and the
        path where the websites blocked will be saved. Tkinter is launched. '''

        self.redirection = "127.0.0.1"
        absolute_path = os.path.abspath("blocked_urls.txt")
        self.path_save_blocked_websites = str(absolute_path)
        self.hosts = r"/etc/hosts"
        self.data = None

        start_msg = "Introduce la web que deseas bloquear:"
        start_label = tkinter.Label(root, text=start_msg)
        start_label.pack()

        self.start_entry = tkinter.Entry(root)
        self.start_entry.pack()

        plot_button = tkinter.Button(root,
                                     text="Confirmar",
                                     command=self.input_data)
        plot_button.pack()

    def _block_save_selected_websites(self):

        ''' Block the websites writing in hosts file. Also saves the website in the
        txt document.'''

        with open(self.path_save_blocked_websites, "r+") as txt_with_saved_blocked_websites:
            self._write_in_document(txt_with_saved_blocked_websites)

        with open(self.hosts, "r+") as path_to_block_websites:
            self._write_in_document(path_to_block_websites)


    def input_data(self):

        ''' Recolects the data that the user wrote on the graphical interface. '''

        info_in_entry = self.start_entry.get()
        original = self.start_entry

        if info_in_entry == "":
            print("No has introducido ninguna web")

        else:

            self.data = info_in_entry
            print("La siguiente web será bloqueada" , self.data)
            self._block_save_selected_websites()
            self.start_entry = self.start_entry.delete(0, 'end')
            self.start_entry = original

    def _write_in_document(self,pageRead):
            file_read = pageRead.read()

            if self.data in file_read:
                pass

            else:
                pageRead.write(self.redirection + "    " +
                               str(self.data) + "\n")

        self.startEntry = self.startEntry.delete(0, 'end')
        self.startEntry = self.original


