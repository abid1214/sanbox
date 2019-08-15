import numpy as np

def lanczos(Av_func, n):
    alpha = np.zeros(n)
    beta  = np.zeros(n-1)
    v = [None]*n

    v[0] = np.random.random(n)
    v[0] /= np.linalg.norm(v[0])

    wp = Av_func(v[0])

    alpha[0] = np.dot(wp.conj(), v[0])

    w_prev = wp - alpha[0]*v[0]

    for j in range(1, n):
        beta[j-1] = np.linalg.norm(w_prev)

        if beta[j-1] >= 1e-14:
            v[j] = w_prev/beta[j-1]
        else:
            v[j] = np.random.random(n)
            for i in range(j):
                v[j] -= np.dot(v[i].conj(), v[i])*v[i]
            v[j] /= np.linalg.norm(v[j])

        wp = Av_func(v[j])

        alpha[j] = np.dot(wp.conj(), v[j])

        w_prev = wp - alpha[j]*v[j] - beta[j-1]*v[j-1]

    V = np.array(v).conj().T
    T = np.diag(beta, -1) + np.diag(alpha, 0) + np.diag(beta, 1)

    return T, V

if __name__ == '__main__':
    n = 3
    H = np.random.random((n,n))
    H = H + H.conj().T

    T, V = lanczos(lambda v: H@v, n)

