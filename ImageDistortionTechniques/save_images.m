function save_images(initial_directory, new_directory)
	directory = strcat(initial_directory, '\*.jpg');
	imagefiles = dir(directory);      
	blocksizes = [2, 4, 8, 16, 32, 64, 128];
    stddevs = [2, 4, 8, 16, 32, 64, 128];
    weights = [0.2, 0.4, 0.6, 0.8];
	nfiles = length(imagefiles);    % Number of files found
	for i=1:nfiles
   		currentfilename = strcat(initial_directory, imagefiles(i).name);
   		currentimage = imread(currentfilename);
   		filename_pieces = strsplit(currentfilename, '.');
        directory = strcat(filename_pieces{1}, '\');
        
        % add a grid to unscrambled and scrambled images based on blocksize
        %s and save.
        mkdir(directory);
   		for j=1:length(blocksizes)
   			[new, original] = scramble( currentimage, 1, blocksizes(j), 0, 1);
        
   			newfilename = strcat(directory, 'scrambled_', num2str(blocksizes(j)), 'pixelsWithGrid.png');
   			imwrite(new, newfilename);
   			newfilename = strcat(directory, 'original_', num2str(blocksizes(j)), 'pixelsWithGrid.png');
   			imwrite(original, newfilename);
        end
        
        % scrambled, no grid
         for j=1:length(blocksizes)
            [new, original] = scramble( currentimage, 1, blocksizes(j), 0, 0);
            newfilename = strcat(directory, 'scrambled_', num2str(blocksizes(j)), 'pixelsWithoutGrid.png');
            imwrite(new, newfilename);
         end
         
         % save original
         newfilename = strcat(directory, 'original.png');
         imwrite(original, newfilename);
         
         % greyscale
         grayscale = greyscale(currentimage);
         newfilename = strcat(directory, 'greyscale.png');
         imwrite(grayscale, newfilename);
         
         % blur the image
         for j = 1:length(stddevs)
            blurred = blur_image(currentimage, stddevs(j));
            newfilename = strcat(directory, 'blurred_', num2str(stddevs(j)),'.png');
            imwrite(blurred, newfilename);
         end
         
         % add gaussian noise
         for j = 1:length(weights)
            noisy = AddNoise(currentimage, weights(j));
            newfilename= strcat(directory, 'noisy_', num2str(weights(j)),'.png');
            imwrite(noisy,newfilename);
         end
         
         % change color sceme
         colored = reverse_colors(currentimage);
         newfilename = strcat(directory, 'reversedcolors.png');
         imwrite(colored, newfilename);
	end
end