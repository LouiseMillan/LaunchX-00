# errors2.py

def main():
    try:
        open("mars.jpg")
    except FileNotFoundError as err:
        print('Hay un problema al intentar leer el archivo', err)

if __name__ == '__main__':
    main()
