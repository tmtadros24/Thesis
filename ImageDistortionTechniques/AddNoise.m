function [new] = AddNoise(im, weight)
%AddNoise creates a new image with added gaussian noise to each 
% color channel

im = im2double(im);
[x,y,~] = size(im);
new = zeros(size(im));

% create 3 gaussian images with the same size of the image
gauss_r = rand(x,y);
gauss_g = rand(x,y);
gauss_b = rand(x,y);

new(:,:,1) = ( im(:,:,1) + (weight*gauss_r) ) / 2;
new(:,:,2) = ( im(:,:,2) + (weight*gauss_g) ) / 2;
new(:,:,3) = ( im(:,:,3) + (weight*gauss_b) ) / 2;

% unnormalize image
new(:,:,1) = new(:,:,1) * 255;
new(:,:,2) = new(:,:,2) * 255;
new(:,:,3) = new(:,:,3) * 255;

new = uint8(new);

end
