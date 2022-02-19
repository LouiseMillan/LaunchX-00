# config3.py

import errno


def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print('¡No se encontro el archivo "config.txt"!')
        elif err.errno == 13:
            print('Se encontro el archivo pero no se puede leer')
        else:
            print('Error:', err)

if __name__ == '__main__':
    main()
