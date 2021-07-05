from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {} \n'.format(piloto, trajeto))


t_carro1 = Thread(target=carro, args=[50, "Kaio"])
t_carro2 = Thread(target=carro, args=[25, "Diego"])

t_carro1.start()
t_carro2.start()

