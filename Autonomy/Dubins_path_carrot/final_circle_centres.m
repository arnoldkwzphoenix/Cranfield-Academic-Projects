function [end_circle_centres] = final_circle_centres(x_f, y_f, heading)
    %starting circle centres coordinates
    radius = 5;
    x_cf_ccw = x_f + radius*cosd(heading + 90);
    y_cf_ccw = y_f + radius*sind(heading + 90);
    x_cf_cw = x_f - radius*cosd(heading + 90);
    y_cf_cw = y_f - radius*sind(heading  + 90);
    
    end_circle_centres = [round(x_cf_ccw,4), round(y_cf_ccw,4);
                                   round(x_cf_cw,4), round(y_cf_cw,4)]; 

end       