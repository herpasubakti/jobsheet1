import random
from guess import cek

jawaban = random.randint(1, 10)

while True:
    tebakan = int(input('tebak angka dari 1 s.d 10; '))

    if cek(tebakan, jawaban):
        print("jawaban kamu benar")
        break
    else:
        print("jawaban kamu salah")
