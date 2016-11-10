% build classifier based on gist and output, must run loadtrainingset first
cl2 = fitcsvm(gist,output,'KernelFunction','rbf');

% load gists of test set

cd 'testset\';

images = zeros(256,256,3,40);
% the file names.
imagefiles = dir('*.jpg');    
nfiles = length(imagefiles)    % Number of files found
for ii=1:nfiles
   currentfilename = imagefiles(ii).name;
   currentimage = imread(currentfilename);
   cd '..';
   currentimage = imresizecrop(currentimage,[256 256]);
   images(:,:,:,ii) = currentimage;
   cd 'testset\';
end

cd '..';

% GIST Parameters:
clear param
param.imageSize = [256 256]; % set a normalized image size
param.orientationsPerScale = [8 8 8 8]; % number of orientations per scale (from HF to LF)
param.numberBlocks = 4;
param.fc_prefilt = 4;

% Pre-allocate gist:
Nfeatures = sum(param.orientationsPerScale)*param.numberBlocks^2;
testgist = zeros([40 Nfeatures]); 

% Loop:
for i = 1:nfiles
   testgist(i, :) = LMgist(images(:,:,:,i), [], param); % the next calls will be faster
end

% Set first 50 images to label 0 for indoor and last 50 to 1 for outdoor
labels = zeros(40,1);
labels(1:20) = 1;

[~,scores2] = predict(cl2,testgist);
scores = zeros(40,1);
for i = 1:length(scores2)
    if ( scores2(i,1) > scores2(i,2) )
        scores(i) = 0;
    else 
        scores(i) = 1;
    end
end


