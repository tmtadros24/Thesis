% This function scrambles an image and blacks out a certain percentage of blocks in the image
% im is the image to process
% jumble is 1 or 0, 1 if you want to scramble the image, 0 otherwise
% blocksize is the size in pixels of the blocks in the image you want to scramble or black out
% pRemoval is the percent of blocks to remove

function[new, original] = scramble( im, jumble, blocksize, pRemoval, grid )
	% scramble image
	if ( jumble == 1 )
		numBlocks = floor( size(im)/blocksize ); % extra pixels are cut off
		x_Blocks = numBlocks(1); % number of blocks in x dimension
		y_Blocks = numBlocks(2); % number of blocks in y dimension
		scrambled_image = zeros( x_Blocks*blocksize, y_Blocks*blocksize, 3 );
		ind = randperm( x_Blocks*y_Blocks ); % returns a vector with random numbers from 1 to the total number of blocks (in the new image)
		[ind1,ind2] = ind2sub( [x_Blocks,y_Blocks],ind ); % takes the random integer and converts it to a ixj entry in the matrix image

		for k = 1:x_Blocks*y_Blocks
    		[i,j] = ind2sub( [x_Blocks,y_Blocks],k );
    		scrambled_image((i-1)*blocksize+1:i*blocksize,(j-1)*blocksize+1:j*blocksize,:) = im((ind1(k)-1)*blocksize+1:ind1(k)*blocksize,(ind2(k)-1)*blocksize+1:ind2(k)*blocksize,:);
    	end
    	
    	% black out blocks
    	if ( pRemoval > 0 )
    		numRemoval = floor( (pRemoval * x_Blocks * y_Blocks) / 100 ); % number of blocks to black out
			ind = randperm( x_Blocks * y_Blocks ); % returns a vector with random numbers from 1 to total number of blocks to remove
			[ind1,ind2] = ind2sub( [x_Blocks, y_Blocks],ind );

			for k = 1:numRemoval
				i = ind1(k);
				j = ind2(k);
				scrambled_image((i-1)*blocksize+1:i*blocksize,(j-1)*blocksize+1:j*blocksize,:) = zeros(blocksize,blocksize,3);
			end	
    	end
    	
    	scrambled_image = uint8(scrambled_image); % convert from double to uint8
    	
    	% change original image if necessary
    	[x, y, r] = size(scrambled_image);
    	[x_1, y_1, r_1] = size(im);
    	image = im;
    	if (x_1 ~= x || y_1 ~= y )
            warning('Resizing the original image');
            image = image(1:x,1:y,:);
    	end	
    
    elseif ( pRemoval > 0 ) % black out blocks without scrambling
    	numBlocks = floor( size(im)/blocksize );
    	x_Blocks = numBlocks(1); % number of blocks in x dimension
		y_Blocks = numBlocks(2); % number of blocks in y dimension
		scrambled_image = im;
		numRemoval = floor( (pRemoval * x_Blocks * y_Blocks) / 100 ); % number of blocks to black out
		ind = randperm( x_Blocks * y_Blocks ); % returns a vector with random numbers from 1 to total number of blocks to remove
		[ind1,ind2] = ind2sub( [x_Blocks, y_Blocks],ind );

		for k = 1:numRemoval
			i = ind1(k);
			j = ind2(k);
			scrambled_image((i-1)*blocksize+1:i*blocksize,(j-1)*blocksize+1:j*blocksize,:) = zeros(blocksize,blocksize,3);
		end	
		
		scrambled_image = uint8(scrambled_image); % convert from double to uint8
		
		% change original image if necessary
		[x, y, r] = size(scrambled_image);
    	[x_1, y_1, r_1] = size(im);
    	image = im;
    	
    	if (x_1 ~= x || y_1 ~= y )
            warning('Resizing the original image');
            image = image(1:x,1:y,:);
    	end	
	
	else % don't do anything
		scrambled_image = im;
		image = im;
    end

    if ( grid == 1 )
    	scrambled_image = make_color_grid(scrambled_image, blocksize);
    	image = make_color_grid(image, blocksize);
    end

    new = scrambled_image;
    original = image;
end