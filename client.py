import httpie
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class Client:

    def __init__(self):
        logging.info('  Initialization of a client')
        return

    def initialize(self, args):
        # 'init', host, username, password
        logging.info('  Initialization of storage')
        logging.info('      arguments: ' + str(args))

        if len(args) != 4:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def create_file(self, args):
        # 'create', path, filename
        logging.info('  Creating file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def read_file(self, args):
        # 'read', path, filename
        logging.info('  Reading file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def write_file(self, args):

        logging.info('  Writing file')
        logging.info('      arguments: ' + str(args))


    def delete_file(self, args):
        # 'delete', path, filename
        logging.info('  Deleting file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def info_file(self, args):
        # 'info', path, filename
        logging.info('  Reading info about file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        pass


    def copy_file(self, args):
        # 'copy', path, filename, new_path, new_filename
        logging.info('  Copying file')
        logging.info('      arguments: ' + str(args))

        if len(args) != 5:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def move_file(self, args):
        # 'copy', path, filename, new_path, new_filename
        logging.info('  Moving file')
        logging.info('      arguments: ' + str(args))
        if len(args) != 5:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def open_directory(self, args):
        # 'opendir', path
        logging.info('  Opening directory')
        logging.info('      arguments: ' + str(args))
        if len(args) != 2:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def read_directory(self, args):
        # 'readdir', path
        logging.info('  Reading directory')
        logging.info('      arguments: ' + str(args))
        if len(args) != 2:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def make_directory(self, args):
        # 'makedir', path, dirname
        logging.info('  Making directory')
        logging.info('      arguments: ' + str(args))
        if len(args) != 3:
            logging.error(" Incorrect number of arguments")
            return
        pass

    def delete_directory(self, args):
        # 'deletedir', path
        logging.info('  Deleting directory')
        logging.info('      arguments: ' + str(args))
        if len(args) != 2:
            logging.error(" Incorrect number of arguments")
            return
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


if __name__ == '__main__':
    # Spot in mode user wants to run the program
    # (command - line or interactive)

    client = Client()

    if len(sys.argv) == 1:
        client.interactive_mode()
    else:
        client.command_line_mode()
