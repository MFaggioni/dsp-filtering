



%DISCRETIZAR PLANTA ANALOGICA

T=0.5;
num=[1 -2];
den=[1 0 -1];
[A,B,C,D]=tf2ss(num,den);
[G,H]=c2d(A,B,T);
[numz,denz]=ss2tf(G,H,C,D);
disp(numz);
disp(denz);

A=[1 0 0 0;-2.2553 1 .2658 0;1 -2.2553 -.7763 .2658;0 1 0 -.7763];
b=[1;-1.8754;.9963;-.08188];
 
x=A\b;











