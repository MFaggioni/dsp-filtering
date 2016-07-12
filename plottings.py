import matplotlib.pyplot as plt
from scipy import signal as sg
import numpy as np
import plotly.plotly as py
import scipy.fftpack
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
        y:  samples
        title:  Title of the Figure and Plot
    return:
        Plot a Smaller number of Samples
"""
def plot_fft(y,title):
        try:
            # Number of samplepoints
            N = 6000
            Fs=100
            # sample spacing
            T = 1.0 / Fs
            x = np.linspace(0.0, N*T, N)
            #y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
            yf = scipy.fftpack.fft(y)
            xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

            fig, ax = plt.subplots()
            ax.plot(xf, 2.0/N * np.abs(yf[:N/2]))
            plt.grid()
            plt.title(title)
            plt.xlabel('Frequency')
            plt.ylabel('Amplitude')
            plt.show()

        except ValueError:
            print('Error al Introducir los Datos, Vuelva a Intentarlo')

def plot_comparison(number_of_samples,y1,y2,title):
    try:
        x=list(range(number_of_samples))
        sgn1=list(range(number_of_samples))
        sgn2=list(range(number_of_samples))
        for i in range(len(x)):
            sgn1[i] = y1[i]
            sgn2[i] = y2[i]

        plt.figure(title)
        plt.plot(x,sgn1,'r',label='Entrada')
        plt.plot(x,sgn2,'b',label='Senal Corrompida')
        plt.grid()
        plt.legend()
        plt.title(title)
        plt.xlabel('Samples')
        plt.ylabel('Magnitude')
        plt.show()

    except:
        print('Error al Introducir los Datos, Vuelva a Intentarlo')
