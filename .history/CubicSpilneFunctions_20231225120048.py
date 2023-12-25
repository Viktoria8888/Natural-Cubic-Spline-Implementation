from Polynomial import *
"""
x1 y1 ->
        (y2-y1)/(x2-x1) = A
x2 y2 ->                    -> (B-A)/ (x3-x1)
        (y3-y2)/(x3-x2) = B
x3 y3 ->
"""
def difference_quotient(xs:list,ys:list) ->int: # f[x_k-1, x_k, x_k+1]
    xs,ys = np.array(xs), np.array(ys)
    if (xs.size != ys.size):
        raise ValueError
    n = len(xs) - 1;
    # Building the table: i-column, k-row
    for i in range(1,n+1):
        for k in range(n,i-1,-1):
           ys[k] = (ys[k] - ys[k-1]) / (xs[k] - xs[k-i])
           print(ys[k])
    return ys[n]


difference_quotient([0,1,3,5],[0,1,27,125])
