import sys
import numpy as np
import matplotlib.pyplot as plt

names = sys.argv[1:]
print(names)
x_data = np.loadtxt(names[0], delimiter='\t', unpack=True)
y_data = np.loadtxt(names[1], delimiter='\t', unpack=True)

plt.style.use('science')
fig, ax = plt.subplots()
plt.title(names[3])
plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0.0))

ax.errorbar(x_data[0], y_data[0], xerr=x_data[1], yerr=y_data[1], fmt='.', color='blue')
m, b = np.polyfit(x_data[0], y_data[0], 1)
ax.plot(x_data[0], m * x_data[0] + b, ':r', label=f'$y = ({m:.3e})x + {b:.3e}$')

ax.set_xlabel(names[4])
ax.set_ylabel(names[5])
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig(names[2], dpi=250)

# python src/lin_regression_errors.py data/1_lambdas2.dat data/n.dat images/Cauchy_2.png 'Regressione lineare' '$1 / \lambda^2 [m^{-2}]$' '$n(\lambda)$'
# python3 tools/plots/lin_regression_errors.py data_path1/.txt data_path2/.txt image_path/output.png 'title' 'x-axis' 'y-axis'