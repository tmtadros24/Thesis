import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import glob
import caffe

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def create_matrix_entry(image, image_directory, index, labels):
	# if "WithGrid" is in the image name, then the image has a grid
	if ("WithGrid" in image):
		grid = 1
	else:
		grid = 0

	if ("pixels" not in image):
		blocksize = 256
	else:
		image_stats = image.split("_", 2)
		pixels = image_stats[1].split("pixels", 1)
		blocksize = int(pixels[0])

	# check if image is scrambled or unscrambled
	if ("original" in image):
		scramble = 0
	else:
		scramble = 1 
			
	# check if image was in indoor or outdoor directory
	if ('indoor' in image):
		ground_truth = 0
	else:
		ground_truth = 1
			
	filename = image

	# check result by counting the top 5 results
	indoor = 0
	outdoor = 0
	for result in labels:
		if ('2' in result):
			outdoor = outdoor + 1
		else:
			indoor = indoor + 1
	if outdoor > indoor:
		result = 1
	else:
		result = 0
	# take the top result
	#if ('2' in result_string):
	#	result = 1
	#else:
	#	result = 0

	entry = [index, filename, grid, blocksize, scramble, ground_truth, result]
	return entry


def create_text_file(filename, results):
	file = open(filename, "w")
	for entry in results:
		file.write(str(entry[0]) + " " + entry[1] + " " + str(entry[2]) + " " + str(entry[3]) + " " + str(entry[4]) + " " + str(entry[5]) + " " + str(entry[6])+ '\n')
	file.close()


caffe.set_device(0)
caffe.set_mode_gpu()

#load the model
net = caffe.Net('places205CNN_deploy_upgraded.prototxt',
                'places205CNN_iter_300000_upgraded.caffemodel',
                caffe.TEST)

# load input and configure preprocessing
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', np.load('C:\Users\Timothy\Documents\pycaffe\caffe\imagenet\ilsvrc_2012_mean.npy').mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)

#note we can change the batch size on-the-fly
#since we classify only one image, we change batch size from 10 to 1
net.blobs['data'].reshape(1,3,227,227)

directory = 'C:\Users\Timothy\Documents\ScrambledImagesResearchSpring2016\images'
results = []
index = 1
for category in get_immediate_subdirectories(directory):
	for image_directory in get_immediate_subdirectories(category):
		im_dir = category + '\\' + image_directory + "\\*.jpg"
		for image in glob.glob(im_dir): 
			print image

			#load the image in the data layer
			im = caffe.io.load_image(image)
			net.blobs['data'].data[...] = transformer.preprocess('data', im)

			#compute
			out = net.forward()

			# other possibility : out = net.forward_all(data=np.asarray([transformer.preprocess('data', im)]))

			#predicted predicted class
			#print out['prob'].argmax()

			#print predicted labels
			labels = np.loadtxt("IndoorOutdoor_Places205.txt", str, delimiter='\t')
			top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1] 
			print labels[top_k]

			# produce output matrix
			results.append(create_matrix_entry(image, image_directory, index, labels[top_k]))
			index = index + 1

np.save('matrix.npy', results)
create_text_file("DeepCNN_Results", results)
