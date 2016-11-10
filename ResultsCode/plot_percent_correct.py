import numpy as np
import matplotlib.pyplot as plt

def plot_accuracy_by_blocksize(results):
	blocksize_misses_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_misses_without_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_entries_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_entries_without_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0}
	original_blocksize_misses_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	original_blocksize_entries_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if grid == 1:
			if scramble == 1:
				blocksize_entries_with_grid[blocksize] += 1
				if result != ground_truth:
					blocksize_misses_with_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if grid == 0:
			if scramble == 1:
				blocksize_entries_without_grid[blocksize] += 1
				if result != ground_truth:
					blocksize_misses_without_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if blocksize == 256:
			blocksize_entries_without_grid[blocksize] += 1
			blocksize_entries_with_grid[blocksize] += 1
			if result != ground_truth:
				blocksize_misses_without_grid[blocksize] += 1
				blocksize_misses_with_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if scramble == 0:
			original_blocksize_entries_with_grid[blocksize] += 1
			if result != ground_truth:
				original_blocksize_misses_with_grid[blocksize] += 1

	# get percent accuracy for each blocksize, with and without grid
	blocksizes = [2, 4, 8, 16, 32, 64, 128, 256]
	percent_accuracy_with_grid = []
	percent_accuracy_without_grid = []
	original_percent_accuracy = []
	for i in range(0,len(blocksizes)):
		percent_accuracy_with_grid.append(((float) (blocksize_entries_with_grid[blocksizes[i]]) - (float) (blocksize_misses_with_grid[blocksizes[i]])) / (float) (blocksize_entries_with_grid[blocksizes[i]]))
		percent_accuracy_without_grid.append(((float) (blocksize_entries_without_grid[blocksizes[i]]) - (float) (blocksize_misses_without_grid[blocksizes[i]])) / (float) (blocksize_entries_without_grid[blocksizes[i]]))
		original_percent_accuracy.append(((float) (original_blocksize_entries_with_grid[blocksizes[i]]) - (float) (original_blocksize_misses_with_grid[blocksizes[i]])) / (float) (original_blocksize_entries_with_grid[blocksizes[i]]))

	print percent_accuracy_with_grid
	print percent_accuracy_without_grid
	print original_percent_accuracy
	# plot the two sets of points	
	#plt.plot(blocksizes, percent_accuracy_with_grid, marker='o', color='b')
	plt.plot(blocksizes, percent_accuracy_without_grid, marker='o', color='g')
	#plt.plot(blocksizes, original_percent_accuracy, marker='o', color='r')
	plt.xlabel("blocksize")
	plt.ylabel("Percent Correct")
	axes = plt.gca()
	axes.set_ylim([-.1,1.1])
	#plt.legend(["with grid", "without grid", "unscrambled image"], loc='lower center')
	plt.title("Computer Vision")
	plt.show()


def plot_outside_images_accuracy_by_blocksize(results):
	blocksize_misses_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_misses_without_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_entries_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_entries_without_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0}
	original_blocksize_misses_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	original_blocksize_entries_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if grid == 1 and ground_truth == 1:
			if scramble == 1:
				blocksize_entries_with_grid[blocksize] += 1
				if result != ground_truth:
					blocksize_misses_with_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if grid == 0 and ground_truth == 1:
			if scramble == 1:
				blocksize_entries_without_grid[blocksize] += 1
				if result != ground_truth:
					blocksize_misses_without_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if blocksize == 256 and ground_truth == 1:
			blocksize_entries_without_grid[blocksize] += 1
			blocksize_entries_with_grid[blocksize] += 1
			if result != ground_truth:
				blocksize_misses_without_grid[blocksize] += 1
				blocksize_misses_with_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if scramble == 0 and ground_truth == 1:
			original_blocksize_entries_with_grid[blocksize] += 1
			if result != ground_truth:
				original_blocksize_misses_with_grid[blocksize] += 1

	# get percent accuracy for each blocksize, with and without grid
	blocksizes = [2, 4, 8, 16, 32, 64, 128, 256]
	percent_accuracy_with_grid = []
	percent_accuracy_without_grid = []
	original_percent_accuracy = []
	for i in range(0,len(blocksizes)):
		percent_accuracy_with_grid.append(((float) (blocksize_entries_with_grid[blocksizes[i]]) - (float) (blocksize_misses_with_grid[blocksizes[i]])) / (float) (blocksize_entries_with_grid[blocksizes[i]]))
		percent_accuracy_without_grid.append(((float) (blocksize_entries_without_grid[blocksizes[i]]) - (float) (blocksize_misses_without_grid[blocksizes[i]])) / (float) (blocksize_entries_without_grid[blocksizes[i]]))
		original_percent_accuracy.append(((float) (original_blocksize_entries_with_grid[blocksizes[i]]) - (float) (original_blocksize_misses_with_grid[blocksizes[i]])) / (float) (original_blocksize_entries_with_grid[blocksizes[i]]))

	print blocksize_entries_without_grid
	print blocksize_entries_with_grid
	print original_blocksize_entries_with_grid
	print percent_accuracy_with_grid
	print percent_accuracy_without_grid
	print original_percent_accuracy
	# plot the two sets of points	
	plt.plot(blocksizes, percent_accuracy_with_grid, marker='o', color='b')
	plt.plot(blocksizes, percent_accuracy_without_grid, marker='o', color='g')
	plt.plot(blocksizes, original_percent_accuracy, marker='o', color='r')
	plt.xlabel("blocksize")
	plt.ylabel("Percent Correct")
	axes = plt.gca()
	axes.set_ylim([-.1,1.1])
	plt.legend(["with grid", "without grid", "unscrambled image"], loc='lower center')
	plt.show()

def plot_inside_images_accuracy_by_blocksize(results):
	blocksize_misses_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_misses_without_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_entries_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	blocksize_entries_without_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0}
	original_blocksize_misses_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
	original_blocksize_entries_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if grid == 1 and ground_truth == 0:
			if scramble == 1:
				blocksize_entries_with_grid[blocksize] += 1
				if result != ground_truth:
					blocksize_misses_with_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if grid == 0 and ground_truth == 0:
			if scramble == 1:
				blocksize_entries_without_grid[blocksize] += 1
				if result != ground_truth:
					blocksize_misses_without_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if blocksize == 256 and ground_truth == 0:
			blocksize_entries_without_grid[blocksize] += 1
			blocksize_entries_with_grid[blocksize] += 1
			if result != ground_truth:
				blocksize_misses_without_grid[blocksize] += 1
				blocksize_misses_with_grid[blocksize] += 1

	for entry in results:
		blocksize = int(entry[3])
		grid = int(entry[2])
		scramble = int(entry[4])
		ground_truth = int(entry[5])
		result = int(entry[6])
		if scramble == 0 and ground_truth == 0:
			original_blocksize_entries_with_grid[blocksize] += 1
			if result != ground_truth:
				original_blocksize_misses_with_grid[blocksize] += 1

	# get percent accuracy for each blocksize, with and without grid
	blocksizes = [2, 4, 8, 16, 32, 64, 128, 256]
	percent_accuracy_with_grid = []
	percent_accuracy_without_grid = []
	original_percent_accuracy = []
	for i in range(0,len(blocksizes)):
		percent_accuracy_with_grid.append(((float) (blocksize_entries_with_grid[blocksizes[i]]) - (float) (blocksize_misses_with_grid[blocksizes[i]])) / (float) (blocksize_entries_with_grid[blocksizes[i]]))
		percent_accuracy_without_grid.append(((float) (blocksize_entries_without_grid[blocksizes[i]]) - (float) (blocksize_misses_without_grid[blocksizes[i]])) / (float) (blocksize_entries_without_grid[blocksizes[i]]))
		original_percent_accuracy.append(((float) (original_blocksize_entries_with_grid[blocksizes[i]]) - (float) (original_blocksize_misses_with_grid[blocksizes[i]])) / (float) (original_blocksize_entries_with_grid[blocksizes[i]]))

	print blocksize_entries_without_grid
	print blocksize_misses_without_grid
	print blocksize_entries_with_grid
	print blocksize_misses_with_grid
	print original_blocksize_entries_with_grid
	print original_blocksize_misses_with_grid
	print percent_accuracy_with_grid
	print percent_accuracy_without_grid
	print original_percent_accuracy
	# plot the two sets of points	
	plt.plot(blocksizes, percent_accuracy_with_grid, marker='o', color='b')
	plt.plot(blocksizes, percent_accuracy_without_grid, marker='o', color='g')
	plt.plot(blocksizes, original_percent_accuracy, marker='o', color='r')
	plt.xlabel("blocksize")
	plt.ylabel("Percent Correct")
	plt.legend(["with grid", "without grid", "unscrambled image"], loc='lower center')
	axes = plt.gca()
	axes.set_ylim([-.1,1.1])
	plt.show()



data = np.load("matrix.npy")
plot_accuracy_by_blocksize(data)
#plot_outside_images_accuracy_by_blocksize(data)
#plot_inside_images_accuracy_by_blocksize(data)