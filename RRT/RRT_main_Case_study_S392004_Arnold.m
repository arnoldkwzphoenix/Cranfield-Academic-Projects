close all;
clear;
clc;

x_max = 1000;%Max X map range 
y_max = 1000;%Max Y map range    

%Obstacle positions on map
poly = { [300,500; 200,200;450,300],[600,700;650,500;750,600;800,780],[550,450;750,350;700,250;530,300],[310,750;340,600;500,550;480,650]};
      
%parameters of RRT
EPS = 70; %Epsilon, max distance that a new node can be from nearest neighbour
numNodes = 300; %number of nodes generated within this program

%% Initialization %%%%%%%%%%%
q_start.coord = [0,0];   %%%*** Write value, starting point
q_start.cost = 0;    %%%*** Write value 
q_start.parent = 0;  %%%*** Write value, state config to generate path
q_goal.coord = [600,600];    %%%*** Write value, ending point
q_goal.cost = 0;     %%%*** Write value

nodes(1) = q_start; %starting node
%%%%%%%%%%%%%%%%%%%%%%%%%%
%drawing map 
figure(1)
axis([-5 x_max -5 y_max])
hold on
plot(q_start.coord(1),q_start.coord(2),'r*','LineWidth',2)
plot(q_goal.coord(1),q_goal.coord(2),'k*','LineWidth',2)
RRT_obstacles_plot_poly(gca, poly);

%%
%start to generate nodes for RRT
for i = 1:1:numNodes


    %% Step 1:Generate Random state or points 
    %%%%==========================================
    q_rand = [floor(rand(1)*x_max) floor(rand(1)*y_max)];%% ***write function, generate random nodes

    %%%%% Break if goal node is already reached
    for j = 1:1:length(nodes)
        if dist(nodes(j).coord, q_goal.coord) <= 50%%%%nodes(j).coord == q_goal.coord
            break
        end
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    %% Step 2: Pick the closest node from existing list to branch out from
    %%%%%==================================================================
    ndist = [];
    for j = 1:1:length(nodes)
        n = nodes(j);   %initializing with randomly generated nodes
        tmp = dist(n.coord, q_rand);%% **write input arguments
        ndist = [ndist tmp]; %randomly generated nodes and their distance 
    end
    [val, idx] = min(ndist);%%%***Write the function
    q_nearest = nodes(idx);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    %% Step 3: Steer from ������_������������������������������������������ to ������_������������������������ 
    %%%%==========================================
    %steering from newly generated coordinates
    q_new.coord = steer(q_rand, q_nearest.coord, val, EPS);%% ***write the Steer function;
    edge_rand = [q_nearest.coord(1),q_nearest.coord(2); q_new.coord];
    plot(q_rand(1),q_rand(2),'r.')
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    %% Step 4: Collision check %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%===================================================
    chk_collision(edge_rand,poly); %%%% ***write the input
    
    if chk_collision(edge_rand,poly) == 0  %checking if collision present
        line([q_nearest.coord(1), q_new.coord(1)], [q_nearest.coord(2), q_new.coord(2)], 'Color', 'k', 'LineWidth', 1);
        drawnow
        hold on
        q_new.cost = dist(q_new.coord, q_nearest.coord) + q_nearest.cost;%% ***write cost expression, new cost generated for new coords
        q_new.parent =  idx;%nearest node assigned as parent of new node

  
        %% Step 5: Append to nodes %%%%%%%%%%%
        %%%%====================================
        nodes = [nodes q_new]; 
    end
end


%% Find Path : Search backwards from goal to start to find the optimal least cost path
%%%%=================================================================================

%%%% Step 1:
D = []; %optimal nodes 
for j = 1:1:length(nodes)
    tmpdist = dist(nodes(j).coord, q_goal.coord);%%***write input arguments
    D = [D tmpdist];
end

%%%%Step 2:
[val, idx] = min(D);     %%***write input arguments

q_final = nodes(idx);
q_goal.parent = idx;
q_end = q_goal;
nodes = [nodes q_goal];
k =0;
while q_end.parent ~= 0
    start = q_end.parent;   %from goal nodes
    k=k+1;
    via_points(k,:) = nodes(start);

    %%%%Step 3:
    %%%% ***write experession
    %drawing line to join each nodes
    line([q_end.coord(1), nodes(start).coord(1)], [q_end.coord(2),nodes(start).coord(2)],'Color','r','LineWidth',2);
    hold on
    %%%% Step 4:
    %%%% ***write experession
    %starting node
    %generate nodes
    q_end = nodes(start);
end