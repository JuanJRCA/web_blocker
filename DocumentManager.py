import os

class DocumentManager(object):
    ''' Writes and deletes data from two documents.
    1. To know what websites I have currently blocked.
    2. To block the websites.'''

    def __init__(self):
        ''' Initialize the paths of the documents and
        the blocked redirection.'''

        self.data = None
        self.redirection = "127.0.0.1"
        absolute_path = os.path.abspath("blocked_urls.txt")
        self.path_save_blocked_websites = str(absolute_path)
        self.hosts = r"/etc/hosts"

    def add_website_to_hosts_to_block(self):
        '''Writes data in the documents.'''

        with open(self.path_save_blocked_websites, "r+") as file:
            self._write_data_in_file(file)


    def delete_web_from_host_to_unblock(self):

        ''' Deletes data from both documents'''
        with open(self.path_save_blocked_websites, "r+") as file:
                self._delete_data_from_file(file)



    def _write_data_in_file(self, pageRead):

        file_read = pageRead.readlines()
        if not (self._check_if_data_in_file()):

            pageRead.write(self.redirection + "    " +
                           str(self.data) + "\n")



    def _delete_data_from_file(self, pageRead):

        file_read = pageRead.readlines()
        pageRead.seek(0)
        if self._check_if_data_in_file():

            data_to_write = [data for data in file_read
                             if self.data not in data]

            for data in data_to_write:
                pageRead.write(str(data))
            pageRead.truncate()

    def _check_if_data_in_file(self):
        with open(self.path_save_blocked_websites, "r+") as file:
            file_open = file.readlines()

            data_in_file = [self.data for information_file in file_open
                            if self.data in information_file]


            if len(data_in_file) != 0:
                return True
            else:
                return False




