from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt

days = []
absences = []

def plot(*args):

    day = document.getElementById("day").value
    num = document.getElementById("num").value

    if num == "":
        return

    days.append(day)
    absences.append(int(num))

    data = np.array(absences)

    plt.clf()
    plt.plot(days, data, marker='o')

    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()

    display(plt, target="plot", append=False)