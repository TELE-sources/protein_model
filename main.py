import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Store_all = []
with open("protein_model/3nvf.pdb") as protein:
    for lines in protein:
        if "ATOM   " in lines:
            lines = lines.split()
            #'ATOM', '1', 'N', 'LEU', 'A', '125', '4.329', '-12.012', '2.376', '1.00', '0.00', 'N'
            Store_all.append(list(map(float, lines[6:9])))

x,y,z = list(zip(*Store_all))

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(x,y,z, s=1200, edgecolors="black", alpha = 0.7)
#markeredgecolor="black"
ax.axis("off")

plt.show()
