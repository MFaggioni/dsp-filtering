import numpy as np
import scipy as sci
import math as math

"""
    corrupt_signal:
        Corrupt Signal with A*cos(angle*n+phase) function
    args:
        y: Array for Corrupt
        max: Contants A
        frec_ang: Angular Frequency
        phase: Phase Angle
    return:
        list: corrupt signal
"""
def corrupt_signal(y,max,ang_freq,phase):
    try:
        signal_corrupt = list(range(len(y)))
        for i in range(len(signal_corrupt)):
            signal_corrupt[i] = y[i] + (max * math.cos((ang_freq * math.pi * float(i)) + phase))
        return signal_corrupt
    except ValueError:
        print('Error al Introducir los Datos, Vuelva a Intentarlo')


"""
    normalized_data:
    args:
        y: Array to Normalized
    return:
        list: normalized list
"""
def normalized_signal(y):
    try:
        signal_nor = list(range(len(y)))
        max_value = max(y)
        min_value = min(y)
        maximus =max([abs(max_value),abs(min_value)])

        for i in range(len(y)):
            signal_nor[i] = float(y[i]) / maximus
        return signal_nor
    except ValueError:
        print('Error al Introducir los Datos, Vuelva a Intentarlo')
