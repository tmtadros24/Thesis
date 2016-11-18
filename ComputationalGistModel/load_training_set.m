%%
Nimages = 250*205;
imagesPerCategory = 250;
numCategories = 205;

% load training set into cell C
filename = 'train_places205.txt';
fileID = fopen(filename);
C = textscan(fileID,'%s %s');

% where the images are located to copy
imagefile = 'F:\data\vision\torralba\deeplearning\images256\';

% convert cell to array of imagenames and image categories
imagenames = char(C{:,1});
imagecategories = str2num(char(C{:,2}));

clear C;
clear fileID;
clear filename;
%%

% GIST Parameters:
clear param
param.imageSize = [256 256]; % set a normalized image size
param.orientationsPerScale = [8 8 8 8]; % number of orientations per scale (from HF to LF)
param.numberBlocks = 4;
param.fc_prefilt = 4;

% Pre-allocate gist:
Nfeatures = sum(param.orientationsPerScale)*param.numberBlocks^2;
gist = zeros([Nimages Nfeatures]);
labels = zeros([Nimages 1]) + 2;


%% get the gist for 250 images in each category

numimages = zeros(205,1);
for i = 1:205
    numimages(i) = sum(imagecategories == i-1);
end

%% read in indoor outdoor category labels
[mapping,txt,~] = xlsread('IndoorOutdoor_places205.csv');

%%
imagenum = 1;

for ii = 1:numCategories
    directory = strcat(imagefile, char(txt(ii)));
    directory = strrep(directory,'/','\');
    directory = strtok(directory);
    directory = directory(1:end-1);
    directory
    cd(directory);
    % get a random permutation of 250 images in the specfied range
    index = randperm(numimages(ii)) + imagenum - 1;
    
    % get label
    if ( mapping(ii) == 1 )
        label = 0;
    else
        label = 1;
    end    
    % save each image to the indoor directory
    for jj = 1:imagesPerCategory
        %imagename = strcat(imagefile, imagenames(index(jj, :)));
        imagename = imagenames(index(jj),:);
        imagename = strrep(imagename,'/','\');
        list = strsplit(imagename, '\');
        imagename = char(strtok(list(end)));
        image = imread(imagename);
        cd('C:\Users\Timothy\Documents\ScrambledImagesResearchSpring2016\ComputationalGistModel');
        gist((ii-1)*imagesPerCategory+jj, :) = LMgist(image, [], param); % the next calls will be faster
        cd(directory);
        % update labels
        labels((ii-1)*imagesPerCategory+jj) = label;
    end
    imagenum = imagenum + numimages(ii);
end
