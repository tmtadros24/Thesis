function [new] =  reverse_colors(im)
% Get the dimensions of the image. numberOfColorBands should be = 3.
[rows columns numberOfColorBands] = size(im);

% Construct the rgb image with swapped red and green channels.
%cform = makecform('srgb2lab');
%lab = applycform(im, cform); 
%L_channel = lab(:,:,1);
%A_channel = lab(:,:,2);
%B_channel = lab(:,:,3);
%L_channelNew = 100 - L_channel;
%A_channelNew = 255-A_channel;
%labNew = cat(3, L_channelNew, A_channelNew, B_channel);
%cform2 = makecform('lab2srgb');
%new = applycform(labNew,cform2); 
new = imcomplement(im);
end
