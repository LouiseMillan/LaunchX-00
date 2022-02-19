# errors.py

def main():
    try:
        open("config.txt")
    except FileNotFoundError:
        print('¡No se encontro el archivo "config.txt"!')

if __name__ == '__main__':
    main()
