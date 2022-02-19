# config2.py

def main():
    try:
        open("config.txt")
    except FileNotFoundError:
        print('¡No se encontro el archivo "config.txt"!')
    except IsADirectoryError:
        print('¡Se encontro "config.txt" pero es un directorio y no se puede leer!')
    except (BlockingIOError, TimeoutError):
        print('Sistema de archivos con mucha carga, no se puede completar la lectura del archivo de configuración')
    except PermissionError:
        print('¡Se encontro "config.txt" pero no se puede leer!')

if __name__ == '__main__':
    main()
