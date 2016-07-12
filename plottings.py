import matplotlib.pyplot as plt
from scipy import signal as sg
import numpy as np
import plotly.plotly as py
import plotly as ply
ply.tools.set_credentials_file(username='Faggioni', api_key='kd2jy07h6q')
"""
    frequency_response_magnitude:
    args:
        num: Numerator of the transfer function
        den: Denominator of the transfer function
        name: Graphic Title
    return:
        Frecuency Response Magnitude
"""
def frequency_response_magnitude(num,den,title):
    try:
        w,h = sg.freqz(num,den)
        fig = plt.figure(title)
        plt.title(title)
        plt.grid()
        plt.plot(w,abs(h), 'b')
        plt.ylabel('Magnitud', color='b')
        plt.xlabel('Frecuencia [rad/muestra]')
        plt.show()
    except ValueError:
        print('Error al Introducir los Datos, Vuelva a Intentarlo')

"""
    plot_samples:
    args:
        x:  x-axis
        y:  y-axis
        title:  Title of the Figure and Plot
    return:
        Plot of the Signals
"""
def plot_samples(x,y,title):
    try:
        plt.figure(title)
        plt.plot(x,y)
        plt.title(title)
        plt.xlabel('Muestras')
        plt.ylabel('Magnitud')
        plt.show()
    except ValueError:
        print('Error al Introducir los Datos, Vuelva a Intentarlo')


"""
    plot_norm_samples:
    args:
        x:  x-axis
        y:  y-axis
        title:  Title of the Figure and Plot
    return:
        Plot of the Signals between [-1,1]
"""
def plot_norm_samples(x,y,title):
    try:
        signal_nor = list(range(len(y)))
        max_value = max(y)
        min_value = min(y)
        maximus =max([abs(max_value),abs(min_value)])

        for i in range(len(y)):
            signal_nor[i] = float(y[i]) / maximus

        plt.figure(title)
        plt.plot(x,signal_nor)
        plt.title(title)
        plt.xlabel('Muestras')
        plt.ylabel('Magnitud')
        plt.show()
    except ValueError:
        print('Error al Introducir los Datos, Vuelva a Intentarlo')

"""
    plot_significative_sample:
    args:
        x:  x-axis
        y:  y-axis
        number_of_samples: Number of Samples to be Plot
        title:  Title of the Figure and Plot
    return:
        Plot a Smaller number of Samples
"""
def plot_significative_sample(x,y,number_of_samples,title):
    try:
        spl = list(range(number_of_samples))
        sgn = list(range(number_of_samples))

        for i in range(len(spl)):
            sgn[i] = y[i]

        plt.figure(title)
        plt.plot(spl,sgn)
        plt.grid()
        plt.title(title)
        plt.xlabel('Muestras')
        plt.ylabel('Magnitud')
        plt.show()
    except ValueError:
        print('Error al Introducir los Datos, Vuelva a Intentarlo')


"""
    plot_fft:
    args:
        y:  sample

        title:  Title of the Figure and Plot
    return:
        Plot a Smaller number of Samples
"""
def plot_fft(y,title):
        try:
            Fs = 100.0;  # sampling rate
            Ts = 1.0/Fs; # sampling interval
            t = np.arange(0,1,Ts) # time vector

            #ff = 5;   # frequency of the signal
            #y = np.sin(2*np.pi*ff*t)

            n = len(y) # length of the signal
            k = np.arange(n)
            T = n/Fs
            frq = k/T # two sides frequency range
            frq = frq[range(n/2)] # one side frequency range

            Y = np.fft.fft(y)/n # fft computing and normalization
            Y = Y[range(n/2)]

            fig, ax = plt.subplots(2, 1)
            ax[0].plot(t,y)
            ax[0].set_xlabel('Tiempo')
            ax[0].set_ylabel('Amplitud')
            ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
            ax[1].set_xlabel('Freq (Hz)')
            ax[1].set_ylabel('|Y(freq)|')
            plot_url = py.plot_mpl(fig, filename='Fouier Transform')

        except ValueError:
            print('Error al Introducir los Datos, Vuelva a Intentarlo')
