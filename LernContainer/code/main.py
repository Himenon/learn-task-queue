from time import sleep

def loop():
    while True:
        sleep(0.1)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        print("Processを終了します")
    