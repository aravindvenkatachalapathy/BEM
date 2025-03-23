clearvars;close all;clc

% load data
Data    = importdata('NACA64_A17.txt');
alpha   = Data.data(:,1);
c_L     = Data.data(:,2);
c_D     = Data.data(:,3);

% 
Considered  = alpha>-8 & alpha<8;
[MaxVal,MaxIdx] = max(c_L./c_D);

% plot data
MyFontSize  = 8;
MyWidth     = 8;
MyHeight    = 4;

figure
box on;grid on;hold on
plot(alpha,[c_L,c_D])
xlim([-180,180])
set(gca,'xTick',[-180:90:180])
set(gca,'fontsize',MyFontSize)
xlabel('$\alpha_{\textrm{A}}$ [deg]','Interpreter','latex','fontsize',MyFontSize)
ylabel('$c_\textrm{L}, c_\textrm{D}$ [-]','Interpreter','latex','fontsize',MyFontSize)
legend({'Lift','Drag'},'fontsize',MyFontSize,'Location','best')
ResizeAndSaveFigure(MyWidth,MyHeight,'NACA64_LiftAndDrag.pdf')

figure
box on;grid on;hold on
plot(alpha,c_L./c_D)
xlim([-20,20])
set(gca,'xtick',[-20:5:20])
set(gca,'fontsize',MyFontSize)
xlabel('$\alpha_{\textrm{A}}$ [deg]','Interpreter','latex','fontsize',MyFontSize)
ylabel('$\varepsilon$ [-]','Interpreter','latex','fontsize',MyFontSize)
ResizeAndSaveFigure(MyWidth,MyHeight,'NACA64_LiftToDrag.pdf')

figure
box on;grid on;hold on
plot(c_D(Considered),c_L(Considered),'.-')
plot([0 0.008],[0 c_L(MaxIdx)./c_D(MaxIdx)*0.008])
text(c_D(Considered),c_L(Considered),num2str(alpha(Considered)),'fontsize',MyFontSize)
set(gca,'fontsize',MyFontSize)
xlabel('$c_\textrm{D}$ [-]','Interpreter','latex','fontsize',MyFontSize)
ylabel('$c_\textrm{L}$ [-]','Interpreter','latex','fontsize',MyFontSize)
ResizeAndSaveFigure(MyWidth,MyHeight,'NACA64_Lilienthal.pdf')