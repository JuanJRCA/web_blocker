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

    def write_web_in_document(self):
        '''Writes data in the documents.'''

        with open(self.path_save_blocked_websites, "r+") as file:
            blocked_websites = file.read()

            if self.data in blocked_websites:
                pass
            else:
                file.write(self.redirection + "    " +
                           str(self.data) + "\n")

    def delete_web_from_document(self):

        ''' Deletes data from both documents'''
        with open(self.path_save_blocked_websites, "r+") as file:
            blocked_websites = file.readlines()
            file.seek(0)

            webs_to_write = [web for web in blocked_websites if self.data not in web]
            for web in webs_to_write:
                file.write(str(web))
            file.truncate()



