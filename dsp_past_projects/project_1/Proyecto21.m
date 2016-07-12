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
teta1=pi/3;
teta2=pi*2/3;
teta3=pi;
g=linspace(1,6000,6000);
g1=linspace(1,6000,6000);
g2=linspace(1,6000,6000);
g3=linspace(1,6000,6000);

%SENAL DE CONTAMINACION TOTAL
g1=0.15*cos(teta1.*n);
g2=-0.25*sin(teta2.*n + (pi/12));
g3=0.20*cos(teta3.*n);

g=g1+g2+g3;

%MUESTRA DE LA SENAL CONTAMINANTE
gm=linspace(1,muestras,muestras);
%CICLO PARA PASAR LA GRAFICA A UN INTERVALO DONDE SE PUEDA APRECIAR LA
%GRAFICA
for cont3 = 1:muestras

    gm(cont3)=g(cont3);
end

%plot(nm,gm),xlabel('DOMINIO TEMPORAAL'),ylabel('MAGNIITUD'),title('SENAL INDESEADA'),grid;


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
%plot(nm,rm,nm,ecgm);

subplot (3,1,1),plot(nm,rm),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL DE ENTRADA AL SISTEMA'),grid
subplot (3,1,2),plot(nm,ecgm),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL DESEADA'),grid;
subplot (3,1,3),plot(nm,gm),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL INDESEADA'),grid;


%PROCEDAMOS CON LA INSTRUCCION FILTER


num=[1 1 1 1 1 1];
den = [1 0 0 0 0 0];
[H,teta]=freqz(num,den,6000);

%BUSCAR UN AJUSTE OPTIMO
%H=10*H;

%ESPECTRO DE FRECUENCIA
%transf = fft(val);
%plot(teta,transf);

%GRAFICA DE RESPUESTA EN FRECUENCIA DEL FILTRO
%subplot(2,1,1),plot(teta,abs(H)),xlabel('FRECUENCIA'),ylabel('MAGNITUD'),title('RESPUESTA EN FRECUENCIA - MAGNITUD')
%subplot(2,1,2),plot(teta,angle(H)),xlabel('FRECUENCIA (theta)'),ylabel('MAGNITUD'),title('RESPUESTA EN FRECUENCIA - FASE');

%SALIDA DEL ECG
%s1 = (((exp(j*pi))-(exp(5*pi*(1/16))))*((exp(j*pi))-(exp(-(5*pi*(1/16))))))/(((exp(j*pi))-(0.99*exp(5*pi*(1/16))))*((exp(j*pi))-(0.99*exp(-(5*pi*(1/16))))));
%SALIDA DE LA SENAL CORROMPIDA
%s2 = (((exp(j*5*pi*(1/16)))-(exp(5*pi*(1/16))))*((exp(j*5*pi*(1/16)))-(exp(-(5*pi*(1/16))))))/(((exp(j*5*pi*(1/16)))-(0.99*exp(5*pi*(1/16))))*((exp(j*5*pi*(1/16)))-(0.99*exp(-(5*pi*(1/16))))));
%m1 = abs(s1);
%m2 = abs(s2);
%f1 = angle(s1);
%f2 = angle(s2);
%yss = (m1*cos((pi.*n) + f1))+(0.25*m2*cos((5*pi*(1/16).*n) + f2));

yss = filter(num,den,r);
yss = (1/max(abs(yss)))*yss;
yssm = linspace(1,muestras,muestras);

for cont4 = 1:muestras
   
    yssm(cont4) = yss(cont4);
end

%GRAFICAS DE COMPARACION DE SENALES - MUESTRAS 
subplot(2,1,1),plot(nm,rm),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL CORROMPIDA')
subplot(2,1,2),plot(nm,ecgm,nm,yssm),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL DESEADA Vs SENAL DE SALIDA');

%GRAFICAS DE COMPARACION DE SENALES - TOTAL
%subplot(2,1,1),plot(n,r),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL CORROMPIDA')
%subplot(2,1,2),plot(n,ecg,n,yss),xlabel('DOMINIO TEMPORAL'),ylabel('MAGNITUD'),title('SENAL DESEADA Vs SENAL DE SALIDA');







    
    