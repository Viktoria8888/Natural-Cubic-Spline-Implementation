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
            si = (1/h[i]) * ((1/6)*matrix[m][i-1]*(Polynomial([-1, xs[i]])**3) +\
                            (1/6)*matrix[m][i  ]*(Polynomial([1, -xs[i-1]])**3) +\
                            (ys_list[1][i-1]-(1/6)*matrix[m][i-1]*(h[i]**2))*Polynomial([-1, xs[i]]) +\
                            (ys_list[1][i  ]-(1/6)*matrix[m][i  ]*(h[i]**2))*Polynomial([1, -xs[i-1]]))
            si_list.append(si)
        s_list.append(PolyRange(si_list, xs))

    return s_list


