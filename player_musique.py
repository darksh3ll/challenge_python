import playsound
import threading
from time import sleep


def loop():
    for i in range(10):
        sleep(5)
        print(i)


def play_sound():
    playsound.playsound('a.mp3')


# création de thread
t1 = threading.Thread(target=play_sound)
t2 = threading.Thread(target=loop)

# démarrer le thread t1
t1.start()
# démarrer le thread t2
t2.start()

# attendre que t1 soit exécuté
t1.join()
# attendre que t2 soit exécuté
t2.join()