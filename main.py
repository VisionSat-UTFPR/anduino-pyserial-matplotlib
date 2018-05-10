import serial
import matplotlib.pyplot as plt

if __name__ == '__main__':

    ser = serial.Serial('/dev/ttyUSB0', 9600)
    count = 0
    data_umi = []
    data_temp = []

    while count <= 15:
        out = ser.readline().decode('utf-8', 'strict')
        out = out.split(' ')
        data_umi.append(out[2])
        data_temp.append(out[7])
        print('x')
        count += 1

    plt.plot(data_umi)
    plt.savefig('plot-umi.png')

    plt.plot(data_temp)
    plt.savefig('plot-temp.png')
