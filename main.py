import plottings as plt
import data_operations as data
from scipy import signal as sg
import math as math
import scipy.io as scipy

"""Reading the Data"""
mat = scipy.loadmat('a01m.mat')
sign = mat['val'][0]
sample = list(range(6000))

"""Sample: Data"""
plt.plot_samples(sample,sign,'Muestra de Datos')

norm_data = data.normalized_signal(sign)
"""Datos Normalizados"""
#Normed Signal
plt.plot_samples(sample,norm_data,'Muestra Normalizada')

#Significative Signal
sm = 300
plt.plot_significative_sample(sample,norm_data,sm,'Muestra Significativa')

#Corrupting Data
r=data.corrupt_signal(norm_data,0.25,5.0/16.0,0)
plt.plot_significative_sample(sample,r,sm,'Corrupt Signal')

#Comparison Between Good and Bad Signal
plt.plot_comparison(sm,norm_data,r,'Comparison')

#Frequency Response of the Filter
plt.frequency_response_magnitude([1,-1.11114,1],[1,-1.1,0.9801],'Respuesta en Frecuencia')

#Filtering Data
yss = sg.lfilter([1,-1.11114,1],[1,-1.1,0.9801],r)

plt.plot_significative_sample(sample,yss,sm,'Salida del Sistema')
plt.plot_comparison(sm,norm_data,yss,'Comparacion')
plt.plot_fft(sign,'Tranformada Discreta de Fourier - Muestra')
