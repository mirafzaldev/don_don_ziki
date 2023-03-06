"this projecct name don_don_ziki"
import random
import  time
import  os
import   itertools

"Bissmilahi Rohmani Rohim"

from random import randint
def don_don_ziki():
    while True:
        ls = ["tosh", "qogoz","qaychi"]
        n = ls[random.randint(0,2)]
        tanlov = input("tanlang (qogoz,qaychi,tosh): ")
        if tanlov.lower() == n:
            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(30):
                time.sleep(.2)  # выполнение функции
                print(next(it), end='', flush=True)

            os.system('cls')
            print(f"{n} == {tanlov} birxil bolip qoldiku! boshqatan tanglang....")
        if tanlov.lower() == "tosh" and n == "qaychi":
            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(30):
                time.sleep(.1)  # выполнение функции
                print(next(it), end='', flush=True)
            os.system('cls')
            print(f"sizniki {tanlov}  bizninki {n} siz yutingiz")
            print("oyindan chiqmoxchi bolsangiz 'chiqish' ni bosing")

        elif tanlov.lower() == "qaychi" and n == "tosh":
            os.system('cls')

            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(30):
                time.sleep(.1)  # выполнение функции
                print(next(it), end='', flush=True)

            print(f"sizniki {tanlov}  bizninki {n} men yudim ")
            print("oyindan chiqmoxchi bolsangiz 'chiqish' ni bosing")
        elif tanlov.lower()=="tosh" and n == "qogoz":

            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(30):
                time.sleep(.1)  # выполнение функции
                print(next(it), end='', flush=True)

            os.system('cls')
            print(f"sizniki {tanlov}  bizninki {n} men yudim ")
            print("oyindan chiqmoxchi bolsangiz 'chiqish' ni bosing")
        elif tanlov.lower() == "qogoz" and n == "tosh":

            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(30):
                time.sleep(.1)  # выполнение функции
                print(next(it), end='', flush=True)

            os.system('cls')
            print(f"sizniki {tanlov}  bizninki {n} siz yutingiz ")
            print("oyindan chiqmoxchi bolsangiz 'chiqish ni bosing")
        elif tanlov.lower() == "qogoz" and n== "qaychi":

            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(30):
                time.sleep(.1)  # выполнение функции
                print(next(it), end='', flush=True)

            os.system('cls')
            print(f"sizniki {tanlov}  bizninki {n} men yudim")
            print("oyindan chiqmoxchi bolsangiz 'chiqish' ni bosing")
        elif tanlov.lower() == "qaychi" and n == "qogoz":


            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(30):
                time.sleep(.1)  # выполнение функции
                print(next(it), end='', flush=True)

            os.system('cls')
            print(f"sizniki {tanlov}  bizninki {n} siz yuditngiz")
            print("oyindan chiqmoxchi bolsangiz 'chiqish' ni bosing")
        elif tanlov.lower() == "chiqish":

            break



x = input("DON DON ZIKI  OYNAYMIZMI JIYZAN: ")
if x.lower() == "xa" or x.lower() == "ha":
    don_don_ziki()

else:
    print("Qumingni oyna unda ....")

