

Store_all = []
with open("3nvf.pdb") as protein:
    for lines in protein:
        if "ATOM   " in lines:
            lines = lines.split()
            #'ATOM', '1', 'N', 'LEU', 'A', '125', '4.329', '-12.012', '2.376', '1.00', '0.00', 'N'
            Store_all.append(list(map(float, lines[6:9])))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x,y,z = list(zip(*Store_all))

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x,y,z, "o")
ax.axis("off")

plt.show()
