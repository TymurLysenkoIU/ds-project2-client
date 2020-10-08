import requests
import logging, sys
import json

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

class Client:

    URL = 'http://localhost:8000/NameServer'

    headers_get = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    headers_post = {'Accept': 'text/plain',
               'enctype': 'multipart/form-data',
               'Content-Encoding': 'utf-8'}

    current_dir = '/'

    def __init__(self):
        logging.info('  Initialization of a client')
        return

    def send_request(self, args: list):
        data = {i: args[i] for i in range(len(args))}
        answer = requests.get(url=self.URL,
                              params=data,
                              headers=self.headers_get)
        logging.info("Return :", answer.text)
        return answer

    def conc_dir(self, path1, path2):
        answer = path1
        if path2[0] == '/':
            answer = path2
            if path2[len(path2) - 1] != '/':
                answer += '/'
        elif path2 == '.':
            answer = path1
        elif path2 == '..':
            if path1.count('/') > 1:
                answer = path1[:
                    path1[:-1].rfind('/') + 1]
        else:
            answer = path1 + path2
            if path2[len(path2) - 1] != '/':
                answer += '/'
        return answer

    def initialize(self, args):
        # 'init', host, username, password
        logging.info('  Initialization of storage')
        logging.info('      arguments: ' + str(args))

        if len(args) != 1:
            logging.error(" Incorrect number of arguments")
            return
        answer = self.send_request(args)
        logging.info("Return :", answer.text)

    def create_file(self, args):
        # 'create', path, filename
        logging.info('  Creating file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        answer = self.send_request(args)
        logging.info(answer)
        pass

    def read_file(self, args):
        # 'read', path, filename, local_filename
        logging.info('  Reading file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 4:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        answer = self.send_request(args[:-1])
        #logging.info(answer.text)
        with open(args[-1], 'wb') as file:
            file.write(answer.content)


    def write_file(self, args):
        # 'write', path, filename, path_to_file
        logging.info('  Writing file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 4:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])

        file = {'file' : open(args[3], 'rb')}
        print(file)
        data = {i: args[i] for i in range(len(args))}
        print(data)
        answer = requests.post(url=self.URL+'/',
                              params = data,
                              files = file,
                              headers=self.headers_post
                            )
        logging.info(answer.text)

    def delete_file(self, args):
        # 'delete', path, filename
        logging.info('  Deleting file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        answer = self.send_request(args)
        logging.info(answer.text)

    def info_file(self, args):
        # 'info', path, filename
        logging.info('  Reading info about file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        answer = self.send_request(args)
        logging.info(answer.text)


    def copy_file(self, args):
        # 'copy', path, filename, new_path, new_filename
        logging.info('  Copying file')
        logging.info('      arguments: ' + str(args))

        if len(args) != 5:
            logging.error(" Incorrect number of arguments")
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        args[3] = self.conc_dir(self.current_dir, args[3])
        answer = self.send_request(args)
        logging.info(answer.txt)

    def move_file(self, args):
        # 'copy', path, filename, new_path, new_filename
        logging.info('  Moving file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 5:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        args[3] = self.conc_dir(self.current_dir, args[3])
        answer = self.send_request(args)
        logging.info("Return :", answer.text)

    def open_directory(self, args):
        # 'opendir', path
        logging.info('  Opening directory')
        logging.info('      arguments: ' + str(args))
        if len(args) != 2:
            logging.error(" Incorrect number of arguments")
            return

        self.current_dir = self.conc_dir(
            self.current_dir, args[1])

        logging.info('  Your current directory is '
                     + self.current_dir)

    def read_directory(self, args):
        # 'readdir', path
        logging.info('  Reading directory')
        logging.info('      arguments: ' + str(args))
        if len(args) != 2:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        answer = self.send_request(args)
        print(answer.text)

    def make_directory(self, args):
        # 'makedir', path, dirname
        logging.info('  Making directory')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        answer = self.send_request(args)
        logging.info("Return :", answer.text)

    def delete_directory(self, args):
        # 'deletedir', path
        logging.info('  Deleting directory')
        logging.info('      arguments: ' + str(args))
        if len(args) != 2:
            logging.error(" Incorrect number of arguments")
            return
        args[1] = self.conc_dir(self.current_dir, args[1])
        answer = self.send_request(args)
        logging.info("Return :", answer.text)
        pass

    operations = {
        'init': initialize,
        'create': create_file,
        'read': read_file,
        'write': write_file,
        'delete': delete_file,
        'info': info_file,
        'copy': copy_file,
        'move': move_file,
        'opendir': open_directory,
        'readdir': read_directory,
        'makedir': make_directory,
        'deletedir': delete_directory
    }

    def parse_operation(self, op):
        try:
            func = self.operations[op]
            return func
        except:
            logging.info('Incorrect operation '+op)
            return "No such operation "+op

    def command_line_mode(self):
        # read command line arguments
        # Check arguments count
        args = sys.argv
        op = args[1].lower()

        maybe_func = self.parse_operation(op)
        if type(maybe_func) == str:
            exit()
        maybe_func(self, args[1:])


    def interactive_mode(self):
        args = input()
        while (args.lower() != 'exit'
               and args.lower() != 'exit()'):
            args = args.split()
            op = args[0].lower()

            maybe_func = self.parse_operation(op)
            if type(maybe_func) == str:
                exit()
            maybe_func(self, args)

            args = input()
            while (len(args) == 0):
                args = input()


if __name__ == '__main__':
    # Spot which mode user wants to run the program
    # (command - line or interactive)

    client = Client()

    if len(sys.argv) == 1:
        client.interactive_mode()
    else:
        client.command_line_mode()
