def run(a, b, i, n):
    for j in range(n):
        C[i][j] = sum(map(lambda x, y: x * y, a[i], b[j]))


if __name__ == "__main__":
    import numpy as np
    import threading
    from random import randint
    from datetime import datetime
    import multiprocessing

    n = int(input('Введите желаемую размерность матриц: '))
    A = ([[randint(-10, 10) for j in range(n)] for i in range(n)])
    B = ([[randint(-10, 10) for j in range(n)] for i in range(n)])
    B_new = np.transpose(np.array(B)).tolist()
    C = ([[randint(0, 0) for j in range(n)] for i in range(n)])
    A1 = np.array(A)
    B1 = np.array(B)
    print('Матрица А:\n', A1, '\n')
    print('Матрица B:\n', B1, '\n')

    startTime = datetime.now()
    for i in range(n):
        threading.Thread(target=run, args=(A, B_new, i, n)).start()
    endTime = datetime.now()

    startTime2 = datetime.now()
    C2 = np.dot(A1, B1)
    endTime2 = datetime.now()

    print('A*B (потоки) \n', np.array(C))
    print(f'Затраченное время: {endTime - startTime} \n')

    print('A*B (numpy) \n', C2)
    print(f'Затраченное время: {endTime2 - startTime2} \n')

    print(f'Рекомендуемое число потоков = {multiprocessing.cpu_count()}')

