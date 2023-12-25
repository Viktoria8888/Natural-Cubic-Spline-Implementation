from Polynomial import *

def difference_quotient(xs:list,ys:list) ->int:
    """
    returns a difference quotient
    -------
    x1 y1 ->
            (y2-y1)/(x2-x1) = A
    x2 y2 ->                    -> (B-A)/ (x3-x1)
            (y3-y2)/(x3-x2) = B
    x3 y3 ->
    """
    xs,ys = np.array(xs), np.array(ys)
    if (xs.size != ys.size):
        raise ValueError
    n = len(xs) - 1;
    # Building the table: i-column, k-row
    for i in range(1,n+1):
        for k in range(n,i-1,-1):
           ys[k] = (ys[k] - ys[k-1]) / (xs[k] - xs[k-i])
    return ys[n]


def NIFS3(xs, ys_list):
    if len(xs) != len(ys_list[0]):
        raise ValueError
    N = len(xs) - 1
    M = len(ys_list)
    q = np.full((M, N), None)
    u = np.full((M, N), None)
    p = np.full((M, N), None)
    for m in range(M):
        q[m][0] = 0
        u[m][0] = 0
        p[m][0] = 0

    h = np.full(N+1, None)
    for i in range(1, N+1):
        h[i] = xs[i] - xs[i-1]

    Lambda = np.full(N+1,None)
    for i in range(1, N):
        Lambda[i] = h[i] / (h[i] + h[i+1])

    d = np.full((M,N),None)
    for i in range(1, N):
        for m in range(M):
            d[m][i] = 6 * difference_quotient(xs[i-1:i+1+1], ys_list[m][i-1:i+1+1])

    for i in range(1, N):
        for m in range(M):
            p[m][i] = Lambda[i] * q[m][i-1] + 2
            q[m][i] = (Lambda[i] -1) / p[m][i]
            u[m][i] = (d[m][i] - Lambda[i]*u[m][i-1]) / p[m][i]

    matrix = np.full((M,N+1), None)

    for m in range(M):
        matrix[m][N] = 0
        matrix[m][0] = 0
        matrix[m][N-1] = u[m][N-1]
    for i in range(N-2, 1 -1, -1):
        for m in range(M):
            matrix[m][i] = u[m][i] + q[m][i] * matrix[m][i+1]
    s_list = []
    for m in range(M):
        si_list = []
        for i in range(1, N+1):
            si = (1/h[i]) * ((1/6)*matrix[m][i-1]*(Polynomial(-1, xs[i])**3) +\
                            (1/6)*matrix[m][i  ]*(Polynomial(1, -xs[i-1])**3) +\
                            (ys_list[1][i-1]-(1/6)*matrix[m][i-1]*(h[i]**2))*Polynomial(-1, xs[i]) +\
                            (ys_list[1][i  ]-(1/6)*matrix[m][i  ]*(h[i]**2))*Polynomial(1, -xs[i-1]))
            # print(si)
            si_list.append(si)

        s_list.append(PiecewisePoly(si_list, xs))
        print(s_list)
    return s_list

ts = [k/95 for k in range(0, 95+1)]

xs =  [5.5, 8.5, 10.5, 13, 17, 20.5, 24.5, 28, 32.5, 37.5, 40.5, 42.5, 45, 47,
49.5, 50.5, 51, 51.5, 52.5, 53, 52.8, 52, 51.5, 53, 54, 55, 56, 55.5, 54.5, 54, 55, 57, 58.5,
59, 61.5, 62.5, 63.5, 63, 61.5, 59, 55, 53.5, 52.5, 50.5, 49.5, 50, 51, 50.5, 49, 47.5, 46,
45.5, 45.5, 45.5, 46, 47.5, 47.5, 46, 43, 41, 41.5, 41.5, 41, 39.5, 37.5, 34.5, 31.5, 28, 24,
21, 18.5, 17.5, 16.5, 15, 13, 10, 8, 6, 6, 6, 5.5, 3.5, 1, 0, 0, 0.5, 1.5, 3.5, 5, 5, 4.5, 4.5, 5.5,
6.5, 6.5, 5.5]

ys = [41, 40.5, 40, 40.5, 41.5, 41.5, 42, 42.5, 43.5, 45, 47, 49.5, 53, 57, 59,
59.5, 61.5, 63, 64, 64.5, 63, 61.5, 60.5, 61, 62, 63, 62.5, 61.5, 60.5, 60, 59.5, 59, 58.5,
57.5, 55.5, 54, 53, 51.5, 50, 50, 50.5, 51, 50.5, 47.5, 44, 40.5, 36, 30.5, 28, 25.5, 21.5,
18, 14.5, 10.5, 7.50, 4, 2.50, 1.50, 2, 3.50, 7, 12.5, 17.5, 22.5, 25, 25, 25, 25.5, 26.5,
27.5, 27.5, 26.5, 23.5, 21, 19, 17, 14.5, 11.5, 8, 4, 1, 0, 0.5, 3, 6.50, 10, 13, 16.5, 20.5,
25.5, 29, 33, 35, 36.5, 39, 41]
NIFS3(ts,[xs,ys])

