import matplotlib.pyplot as plt
from scipy import signal as sg

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
