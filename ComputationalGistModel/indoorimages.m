Nimages = 100;
imagefile = '\trainingset\';

% the file names.
images = zeros(256,256,3,100);

cd 'trainingset\';

indoorimagefiles = dir('*.jpg');
nfiles = length(indoorimagefiles);    % Number of files found
for ii=1:nfiles
   currentfilename = indoorimagefiles(ii).name;
   currentimage = imread(currentfilename);
   cd '..';
   currentimage = imresizecrop(currentimage,[256 256]);
   images(:,:,:,ii) = currentimage;
   cd 'trainingset\';
end

cd '..\outdoortrainingset\';

% the file names.
outdoorimagefiles = dir('*.jpg');    
nfiles = length(outdoorimagefiles)    % Number of files found
for ii=1:nfiles
   currentfilename = outdoorimagefiles(ii).name;
   currentimage = imread(currentfilename);
   cd '..';
   currentimage = imresizecrop(currentimage,[256 256]);
   images(:,:,:,ii + 50) = currentimage;
   cd 'outdoortrainingset\';
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
gist = zeros([Nimages Nfeatures]); 

% Loop:
for i = 1:100
   gist(i, :) = LMgist(images(:,:,:,i), [], param); % the next calls will be faster
end

% Set first 50 images to label 0 for indoor and last 50 to 1 for outdoor
output = zeros(100,1);
output(51:100) = 1;


