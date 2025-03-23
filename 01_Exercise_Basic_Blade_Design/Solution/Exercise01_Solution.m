% -----------------------------
% Solution to Exercise 01 of Course "Introduction to Wind Turbine Aerodynamics".
% ----------------------------------
clearvars;close all;clc

%% a) find R, lambda_D and z
% design parameters: please adjust
R               = 63;               % [m]
lambda_D        = 7.55;           	% [-]
z               = 3;                % [-]

%% b) find optimal AoA and cL
% import Airfoil file
AirfoilFile  	= 'NACA64_A17.dat'; 
fid            	= fopen(AirfoilFile);
AirfoilData   	= textscan(fid,'%f %f %f %f','HeaderLines',14);
fclose(fid);
BEM.AoA         = AirfoilData{1};
BEM.Cl          = AirfoilData{2};
BEM.Cd          = AirfoilData{3};
BEM.Cm          = AirfoilData{4};

% calculate lift-to-drag-ratio
epsilon         = BEM.Cl./BEM.Cd;

% find maximum value
[MaxVal,MaxIdx] = max(epsilon);

% plot
figure
box on;grid on;hold on
plot(BEM.AoA,[BEM.Cl,BEM.Cd])
xlabel('\alpha_{{A}} [deg]')
ylabel('c_{L}, c_{D} [-]')
legend({'Lift','Drag'})

figure
box on;grid on;hold on
plot(BEM.AoA,epsilon)
xlabel('\alpha_{{A}} [deg]')
ylabel('\epsilon [-]')

%% c) find twist and chord
% import AeroDyn file
AeroFile        = 'NRELOffshrBsline5MW_AeroDyn_Equil_noTwr.dat';
fid             = fopen(AeroFile);
NodeData        = textscan(fid,'%f %f %f %f %d %s','HeaderLines',26);
fclose(fid);
BEM.RNodes  	= NodeData{1};
BEM.AeroTwst 	= NodeData{2};
BEM.DRNodes     = NodeData{3};
BEM.Chord       = NodeData{4};
BEM.NFoil       = NodeData{5};

% missing design parameters: please adjust
alpha_A         = BEM.AoA(MaxIdx);	% [deg]
c_L             = BEM.Cl(MaxIdx);   % [-]

% calculate twist angle: please adjust
r               = BEM.RNodes;
beta            = atand(2/3*R/lambda_D./r)-alpha_A;
c               = 1/z*8/9*2*pi*R/c_L*1./(lambda_D*sqrt((lambda_D*r/R).^2+4/9));

%% d) compare to NREL results
figure
box on;grid on;hold on
plot(BEM.RNodes,beta,'.-')
plot(BEM.RNodes,BEM.AeroTwst,'o-')
xlabel('r [m]')
ylabel('\beta [deg]')
title('Comparison Twist Angle')
legend('Betz','NREL')

figure
box on;grid on;hold on
plot(BEM.RNodes,c,'.-')
plot(BEM.RNodes,BEM.Chord,'o-')
xlabel('r [m]')
ylabel('c [m]')
title('Comparison Chord Length')
legend('Betz','NREL')