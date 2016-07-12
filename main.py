import plottings as plt
import data_operations as data
from scipy import signal as sg
import math as math
import scipy.io as scipy

"""Reading the Data"""
mat = scipy.loadmat('a01m.mat')
sign = mat['val'][0]
sample = list(range(6000))

"""Muestra: Datos"""
plt.plot_samples(sample,sign,'Muestra de Datos')

norm_data = data.normalized_signal(sign)
"""Datos Normalizados"""
#Normalicemos la Senal
plt.plot_samples(sample,norm_data,'Muestra Normalizada')

#Muestra Significativa
sm = 600
plt.plot_significative_sample(sample,norm_data,sm,'Muestra Significativa')

#Corrupting Data
r=data.corrupt_signal(norm_data,0.25,5/16,0)

#Frequency Response of the Filter
plt.frequency_response_magnitude([1,-1.1111,1],[1,-1.08336,0.950625],'Respuesta en Frecuencia')

#Filtering Data
yss = sg.lfilter([1,-1.1111,1],[1,-1.08336,0.950625],r)

plt.plot_samples(sample,yss,'Salida de Sistema')

plt.plot_significative_sample(sample,yss,sm,'Salida del Sistema')

plt.plot_fft(sign,'Tranformada Discreta de Fourier')
