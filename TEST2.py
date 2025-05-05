import matplotlib.pyplot as plt

def ShowPlot():
    str_speeds = "38 42 20 40 39"
    str_armor = "80 50 17 50 51"

    speeds = str_speeds.split()
    armors = str_armor.split()

    markers = ["o", "v", "^", "<", ">"]

    for idx in range(len(speeds)):
        x = int(speeds[idx])
        y = int(armors[idx])

        plt.scatter(x, y, marker=markers[idx])

    plt.show()

ShowPlot()