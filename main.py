import numpy as np
import threading
from random import randint
from datetime import datetime


def TreadMatrix(a, b, i):
    for j in range(len(A)):
        C[i][j] = sum(map(lambda x, y: x * y, a[i], b[j]))


n = int(input('Введите желаемую размерность матриц: '))
A = ([[randint(-10, 10) for j in range(n)] for i in range(n)])
B = ([[randint(-10, 10) for j in range(n)] for i in range(n)])
B_new = np.transpose(np.array(B)).tolist()


C = ([[randint(0, 0) for j in range(n)] for i in range(n)])


A1 = np.array(A)
B1 = np.array(B)


startTime = datetime.now()

for i in range(len(A)):
    threading.Thread(target=TreadMatrix, args=(A, B_new, i)).start()

endTime = datetime.now()

startTime2 = datetime.now()
C2 = np.dot(A1, B1)

endTime2 = datetime.now()

print('Сгенерированная матрица: \n', C2)
print('Затраченное время (threads):', endTime-startTime)
print('Затраченное время (numpy): ', endTime2-startTime2)
