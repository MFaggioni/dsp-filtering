import scipy.io as scipy
import plottings as plt
import data_operations as data

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

#Frequency Response
plt.frequency_response_magnitude([1,-1.1111,1],[1,-1.08336,0.950625],'Respuesta en Frecuencia')
