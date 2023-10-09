function [ending_circle_centres] = ending_circle_centres(x_f, y_f, heading_f)
    %ending circle centres coordinates
    radius = 5;
    x_cf_ccw = x_f + radius*cosd(heading_f + 90);
    y_cf_ccw = y_f + radius*sind(heading_f + 90);
    x_cf_cw = x_f - radius*cosd(heading_f + 90);
    y_cf_cw = y_f - radius*sind(heading_f  + 90);

    ending_circle_centres = [round(x_cf_ccw,2), round(y_cf_ccw,2);
                               round(x_cf_cw,2), round(y_cf_cw,2                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )]; 
    
end