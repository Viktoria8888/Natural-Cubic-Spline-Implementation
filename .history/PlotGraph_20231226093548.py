import matplotlib.pyplot as plt
from CubicSpilneFunctions import CreatePolynomials, np
data = """112 -128
111 -133
112 -142
113 -149
115 -157
117 -167
118 -170
119 -181
119 -197
120 -205
120 -215
120 -230
120 -244
114 -245
108 -254
108 -244
105 -231
105 -222
105 -213
104 -204
103 -195
101 -188
101 -177
103 -163
105 -154
108 -142
111 -132
113 -131
117 -135
126 -144
132 -152
137 -159
143 -173
151 -183
159 -193
165 -200
173 -213
181 -225
193 -239
203 -249
214 -257
224 -253
234 -240
239 -231
240 -228
240 -214
238 -200
236 -189
234 -175
234 -162
232 -147
229 -138
224 -124
221 -109
219 -102
230 -111
234 -116
242 -126
247 -131"""

# Parse the data into separate lists for x and y
x_values, y_values = zip(*[map(int, line.split()) for line in data.split("\n") if line.strip()])
STEP = 0.001
def ShowCubicSpline(xs,ys,step=STEP):
    n = len(xs) - 1
    ts = [k / n for k in range(0, n + 1)]
    fxs, fys = CreatePolynomials(ts, [xs, ys])
    ts_plot = np.arange(ts[0], ts[-1] + STEP, STEP)
    xs_plot = np.array([fxs(t) for t in ts_plot])
    ys_plot = np.array([fys(t) for t in ts_plot])

    plt.plot(xs_plot,ys_plot)
    plt.show()

ShowCubicSpline(x_values,y_values)
