function [new] =  blur_image(im, stddev)
	new = imgaussfilt(im, stddev, 'padding', 'replicate');
end
