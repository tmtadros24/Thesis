% Function to put a grid over (with the average pixel color of an image) an image where the size of each square in the grid is specified by blocksize
function[image] = make_color_grid( im, blocksize )
    % get the values of each color channel
    color_r = im(:,:,1);
    color_g = im(:,:,2);
    color_b = im(:,:,3);
    
    % compute the means
    mean_r = mean(color_r(:));
    mean_g = mean(color_g(:));
    mean_b = mean(color_b(:));
    
    % Assign each of the r,g,b components at the border to the mean 
    % Note: this overwrites the pixel values that were at the grid location
	im(blocksize:blocksize:end, :, 1) = mean_r;
	im(:, blocksize:blocksize:end, 1) = mean_r;
    
    im(blocksize:blocksize:end, :, 2) = mean_g;
	im(:, blocksize:blocksize:end, 2) = mean_g;
    
    im(blocksize:blocksize:end, :, 3) = mean_b;
	im(:, blocksize:blocksize:end, 3) = mean_b;
    
    image = im;
end	