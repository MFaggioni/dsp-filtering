close all;
clear all;
clc;

load ('a01m');
who;

%disp(val);
ecg=linspace(1,6000,6000);
n=linspace(1,6000,6000);

for cont = 1:6000
    ecg(cont)=val(cont);
end



% SE VA A ESCALAR LA FUNCION EN EL INTERVALO [-1,1]
% SI SE QUIERE ELIMINAR EL ESCALAMIENTO SOLO BASTA COMENTAR LA LINEA DE
% CODIGO
ecg = ecg*(1/max(abs(ecg)));
plot(n,ecg),xlabel('MUESTRAS'),ylabel('MAGNITUD (mV)'),title('MUESTRA DE SENAL ELECTROCARDIOGRAFICA')


% MUESTRAS A TOMAR PARA ANALIZAR / SUBINTERVALO DE LAS MUESTRAS ORIGINALES
muestras=300;


%GRAFICA DE LA SENAL DE PRUEBA / 5% DE LAS MUESTRAS TOTALES
nm = linspace(1,muestras,muestras);

%VAN A ESTAR LAS MUESTRAS A GRAFICAR
ecgm = linspace(1,muestras,muestras);

%CICLO PARA PASAR LA GRAFICA A UN INTERVALO DONDE SE PUEDA APRECIAR LA
%GRAFICA
for cont1 = 1:muestras

    ecgm(cont1)=ecg(cont1);

end




% SENAL CONTAMINADA
teta1=5*pi/16;
g=linspace(1,6000,6000);
%SENAL DE CONTAMINACION TOTAL
g=0.25*cos(teta1.*n);



%MUESTRA DE LA SENAL CONTAMINANTE
gm=linspace(1,muestras,muestras);
%CICLO PARA PASAR LA GRAFICA A UN INTERVALO DONDE SE PUEDA APRECIAR LA
%GRAFICA
for cont3 = 1:muestras

    gm(cont3)=g(cont3);
end

plot(nm,ecgm),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL MUESTREADA'),grid;

r=linspace(1,6000,6000);
%SENAL TOTAL CONTAMINADA
r=ecg+g;

%MUESTRA DE LA SENAL CONTAMINADA
rm=linspace(1,muestras,muestras);

%CICLO PARA PASAR LA GRAFICA A UN INTERVALO DONDE SE PUEDA APRECIAR LA
%GRAFICA
for cont2=1:muestras

    rm(cont2)=r(cont2);

end

%AQUI SE PUEDEN VER LA SENAL ORIGINAL Y LA SENAL CONTAMINADA QUE ENTRAN AL
%FILTRO
plot(nm,rm,nm,ecgm);



%POLO CON MODULO 0.975 
num=[1 -1.111140466 1];
den = [1 -1.083361954 .950625];
[H,teta]=freqz(num,den,6000);

%ESPECTRO DE FRECUENCIA
transf = fft(ecg);
plot(teta,transf),xlabel('DOMINIO FRECUENCIAL'),ylabel('MAGNITUD'),title('TRANSFORMADA DE FOURIER DE LA SENAL ECG'),grid;

%GRAFICA DE RESPUESTA EN FRECUENCIA DEL FILTRO
subplot(2,1,1),plot(teta,abs(H)),xlabel('FRECUENCIA'),ylabel('MAGNITUD'),title('RESPUESTA EN FRECUENCIA - MAGNITUD')
subplot(2,1,2),plot(teta,angle(H)),xlabel('FRECUENCIA (rad)'),ylabel('MAGNITUD'),title('RESPUESTA EN FRECUENCIA - FASE');

%PROCEDAMOS CON LA INSTRUCCION FILTER
yss = filter(num,den,r);
yssm = linspace(1,muestras,muestras);

for cont4 = 1:muestras
   
    yssm(cont4) = yss(cont4);
end

%GRAFICAS DE COMPARACION DE SENALES - MUESTRAS 
subplot(2,1,1),plot(nm,rm),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL CORROMPIDA')
subplot(2,1,2),plot(nm,ecgm,nm,yssm),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL DESEADA + SENAL DE ESTADO ESTACIONARIO');

%GRAFICAS DE COMPARACION DE SENALES - TOTAL
subplot(2,1,1),plot(n,r),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL CORROMPIDA')
subplot(2,1,2),plot(n,ecg,n,yss),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL DESEADA Vs SENAL DE SALIDA')

%ERROR ASOCIADO A CADA MUESTRA
error = abs(yss-ecg);
errorm = abs(yssm-ecgm);
disp('ERROR MAXIMO DEL FILTRO ES:');
disp(max(error));


%ERROR PROMEDIO
errorpromedio = 0;
for cont5 = 1:6000
    errorpromedio = errorpromedio + error(cont5);
end
errorpromedio = errorpromedio/6000;

disp('ERROR PROMEDIO COMETIDO:');
disp(errorpromedio);
plot(nm,errorm,nm,yssm,nm,ecgm),xlabel('DOMINIO TEMPORAL'),ylabel(''),title('ERRORES EN EL PROCESAMIENTO DE LA SENAL'),grid;
plot(nm,errorm),xlabel('DOMINIO TEMPORAL'),ylabel('ERROR'),title('ERRORES EN EL PROCESAMIENTO DE LA SENAL'),grid;








    
    