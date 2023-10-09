clear,clc;
headings = [0,45,30,-90,-120,-180];
entry_centres=[0,15; 56.46,63.54; 82.5,115.67; 145,70; 104.33, 27.5];

exit_centres=[56.46,63.54;82.5,115.67;145,70;104.33, 27.5;50,5];

%dubins_final();

entry=[3.2 11.16;61.33 62.37;85.41 119.74;148.44 66.38;98.24 28.21;52.57 0.713];

exit=[59.67 59.67;77.64 116.84;147.91, 74.07;100.89 31.12;52.57 0.713;50 0];

c2_prev=[0;10;0];

flag=[+1,-1;+1,-1;+1,-1;-1,+1;-1,-1];

for i=1:1:5

    c1_prev=CCA_carrot(c2_prev(1,1),c2_prev(2,1),entry(i,:),entry(i,:),c2_prev(3,1),entry_centres(i,:),flag(i,1));

    c2_prev=CCA_carrot(c1_prev(1,1),c1_prev(2,1),exit(i,:),exit(i,:),c1_prev(3,1),exit_centres(i,:),flag(i,2));

end