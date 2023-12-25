import matplotlib.pyplot as plt
from CubicSpilneFunctions import CreatePolynomials, np
ts = [k/95 for k in range(0, 95+1)]

# xs =  [5.5, 8.5, 10.5, 13, 17, 20.5, 24.5, 28, 32.5, 37.5, 40.5, 42.5, 45, 47,
# 49.5, 50.5, 51, 51.5, 52.5, 53, 52.8, 52, 51.5, 53, 54, 55, 56, 55.5, 54.5, 54, 55, 57, 58.5,
# 59, 61.5, 62.5, 63.5, 63, 61.5, 59, 55, 53.5, 52.5, 50.5, 49.5, 50, 51, 50.5, 49, 47.5, 46,
# 45.5, 45.5, 45.5, 46, 47.5, 47.5, 46, 43, 41, 41.5, 41.5, 41, 39.5, 37.5, 34.5, 31.5, 28, 24,
# 21, 18.5, 17.5, 16.5, 15, 13, 10, 8, 6, 6, 6, 5.5, 3.5, 1, 0, 0, 0.5, 1.5, 3.5, 5, 5, 4.5, 4.5, 5.5,
# 6.5, 6.5, 5.5]

# ys = [41, 40.5, 40, 40.5, 41.5, 41.5, 42, 42.5, 43.5, 45, 47, 49.5, 53, 57, 59,
# 59.5, 61.5, 63, 64, 64.5, 63, 61.5, 60.5, 61, 62, 63, 62.5, 61.5, 60.5, 60, 59.5, 59, 58.5,
# 57.5, 55.5, 54, 53, 51.5, 50, 50, 50.5, 51, 50.5, 47.5, 44, 40.5, 36, 30.5, 28, 25.5, 21.5,
# 18, 14.5, 10.5, 7.50, 4, 2.50, 1.50, 2, 3.50, 7, 12.5, 17.5, 22.5, 25, 25, 25, 25.5, 26.5,
# 27.5, 27.5, 26.5, 23.5, 21, 19, 17, 14.5, 11.5, 8, 4, 1, 0, 0.5, 3, 6.50, 10, 13, 16.5, 20.5,
# 25.5, 29, 33, 35, 36.5, 39, 41]
a = [(31, 102), (28, 84), (29, 64), (31, 54), (41, 69), (54, 88), (67, 107), (79, 107), (82, 88), (79, 68), (76, 49), (83, 51), (101, 72), (103, 87), (106, 100), (115, 103), (124, 94), (126, 80), (124, 72), (142, 72), (138, 84), (140, 89), (146, 82), (148, 75), (153, 83), (162, 78), (170, 83), (174, 90), (182, 77), (189, 80), (197, 82), (204, 79), (203, 68), (196, 74), (193, 82), (196, 88), (201, 93), (207, 93), (214, 79), (218, 71), (217, 76), (215, 85), (217, 92), (225, 87), (229, 74), (230, 71), (242, 52), (243, 52), (239, 66), (239, 74), (244, 86), (251, 84), (261, 77), (264, 69), (260, 83), (264, 87), (272, 88), (279, 74), (282, 66), (282, 61), (290, 49), (282, 76), (284, 87), (367, 60), (361, 59), (355, 59), (365, 70), (375, 77), (380, 83), (369, 87), (363, 86)]
xs = [p[0] for p in a]
ys = [p[1] for p in a]
import matplotlib.pyplot as plt

STEP = 0.001

def plot_NIFS3_zad6(ts, xs, ys, step=STEP):
    fxs, fys = CreatePolynomials(ts, [xs, ys])

    ts_plot = np.arange(ts[0], ts[-1] + step, step)
    xs_plot = np.array([fxs(t) for t in ts_plot])
    ys_plot = np.array([fys(t) for t in ts_plot])

    plt.plot(xs_plot, ys_plot)
    plt.show()
plot_NIFS3_zad6(ts, xs, ys, 0.001)
