import numpy as np

x = input("Podaj długość wektora: ")

def diag(a):
    v = np.arange(a, 0, -1, dtype='int64')
    m_diag = np.diag(v)
    print(m_diag)


diag(int(x))
