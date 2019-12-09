from os import listdir, stat
from sys import argv
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

def transform(n):
    dirs = listdir('./audio/')
    files = []
    for file in dirs:
        files.append(file)
    chosenfile = "./audio/" + files[n]
    print(chosenfile)

    input_data = read(chosenfile)
    audio = input_data[1]
    plt.plot(audio[0:1024])
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("Waveform for " + chosenfile)
    plt.show()

if __name__ == "__main__":
    num = int(argv[1])
    print(num)
    transform(num)