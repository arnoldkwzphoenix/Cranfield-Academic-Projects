function carrot = CCA_carrot(x_initialCarrot, y_initialCarrot, x_outCarrot, y_outCarrot, heading_angle, orbit_center, flag)

%% Initialization


%% Parameters
%.. Angle Converting Parameters
r2d                     =               180 / pi ;          % Radian to Degree [-]
d2r                     =               1 / r2d ;           % Degree to Radian [-]

%.. Time Step Size
dt                      =               0.1 ;               % Time Step Size [s]

%.. Time
t(1)                    =               0 ;                 % Simulation Time [s]

%.. Circular Orbit
O                       =               orbit_center' ;      % Centre of Orbit [m]
r                       =               5 ;                 % Radius of Orbit [m] same as dubins 

%.. Position and Velocity of Robot
x(1)                    =               x_initialCarrot;     % Initial Robot X Position [m]
y(1)                    =               y_initialCarrot;     % Initial Robot Y Position [m]
psi(1)                  =               heading_angle * d2r;% Initial Robot Heading Angle [rad]

p(:,1)                  =               [ x(1), y(1) ]' ;   % Robot Position Initialization [m]
va                      =               5 ;                 % Robot Velocity [m/s]

%.. Maximum Lateral Acceleration of Robot
Rmin                    =               5;                  % Robot Minimum Turn Radius [m]
umax                    =               va^2 / Rmin ;       % Robot Maximum Lateral Acceleration [m]

%.. Design Parameters
kappa                   =               10;                 % Gain
lambda                  =               flag * 10 * d2r ;   % Carrot Distance

%% Path Following Algorithm
i                       =               0 ;                 % Time Index
while all(abs(x_outCarrot-x(i+1))>0.08 & abs(y_outCarrot-y(i+1))>0.05)
    i                   =               i + 1 ;
    
    %==============================================================================%
    %.. Path Following Algorithm
    
    % Step 1
    % Distance between orbit and current Robot position, d
    d                   =                norm(O - p(:,1),2) - r;
    
    % Step 2
    % Orientation of vector from initial waypoint to final waypoint, theta
    theta               =                atan2(p(2,i) - O(2), p(1,i) - O(1));
    
    % Step 3
    % Carrot position, s = ( xt, yt )
    xt                  =                O(1) + r*cos(theta + lambda);
    yt                  =                O(2) + r*sin(theta + lambda);
    
    % Step 4
    % Desired heading angle, psid
    psid                =                atan2(yt - y(i), xt - x(i));

    % Heading angle error, DEL_psi
    DEL_psi             =                psid - psi(i);
    % Wrapping up DEL_psi
    DEL_psi             =               rem(DEL_psi,2*pi);
    if DEL_psi < -pi
        DEL_psi = DEL_psi + 2*pi;
    elseif DEL_psi > pi
        DEL_psi = DEL_psi-2*pi;
    end
    
    % Step 5
    % Guidance command, u
    u(i)                =               kappa * (DEL_psi) * va;
    % Limit u
    if u(i) > umax
        u(i)            =               umax;
    elseif u(i) < -umax
        u(i)            =             - umax;
    end
    %==============================================================================%
    
    %.. Robot Dynamics
    % Dynamic Model of Robot
    dx                  =               va * cos( psi(i) ) ;
    dy                  =               va * sin( psi(i) ) ;
    dpsi                =               u(i) / va ;
    
    % Robot State Update
    x(i+1)              =               x(i) + dx * dt ;
    y(i+1)              =               y(i) + dy * dt ;
    psi(i+1)            =               psi(i) + dpsi * dt ;
    
    % Robot Position Vector Update
    p(:,i+1)            =               [ x(i+1), y(i+1) ]' ;
    robot_position      =               [x(i+1);y(i+1)];
    robot_heading       =               psi(i+1);
    
    %.. Time Update
    t(i+1)              =               t(i) + dt ;
    if(i == 500)
        break;
    end
end

%% Result Plot
% Parameterized Circular Orbit
TH                      =               0:0.01:2*pi ;
Xc                      =               O(1) + r * cos( TH ) ;
Yc                      =               O(2) + r * sin( TH ) ;

%.. Trajectory Plot
figure(1) ;
plot( Xc, Yc, 'b', 'LineWidth', 2 ) ;
hold on ;
plot( x, y, 'LineWidth', 2 ) ;
hold on ;
xlabel('X (m)') ;
ylabel('Y (m)') ;
title('Carrot Chasing');
legend('Desired Path', 'Robot Trajectory', 'Location', 'southeast' ) ;
axis auto;

%.. Guidance Command
figure(2) ;
plot( t(1:end-1), u, 'LineWidth', 2 ) ;
xlabel('Time (s)') ;
ylabel('u (m/s^2)') ;
carrot = [robot_position;robot_heading*r2d];
end