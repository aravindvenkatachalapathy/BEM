clearvars;close all;clc

% load data
Airfoil    = importdata('Naca64_618.txt');

% plot
figure
plot(Airfoil.data(:,1),Airfoil.data(:,2))
axis equal
ylim([min(Airfoil.data(:,2)) max(Airfoil.data(:,2))])
xlim([0 1])
set(gca,'visible','off')
ResizeAndSaveFigure( 6,2,'NACA64_618.pdf')
