import csv
import numpy as np
import matplotlib.pyplot as plt

blocksize_misses_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
blocksize_misses_without_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
blocksize_entries_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
blocksize_entries_without_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0}
original_blocksize_misses_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 
original_blocksize_entries_with_grid = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0} 

# modular division if block - [blocksize, scrambled (1 if scrambled), grid (1 if grid)]
modular_results = {1:[256, 0, 0], 2:[2, 0, 1], 3:[4, 0, 1], 4:[8, 0, 1], 5:[16, 0, 1], 6:[32, 0, 1], 7:[64, 0, 1], 8:[128, 0, 1],
				 9:[2, 1, 1], 10:[2, 1, 0], 11:[4, 1, 1], 12:[4, 1, 0], 13:[8, 1, 1], 14:[8, 1, 0], 
				 15:[16,1,1],16:[16,1,0], 17:[32,1,1], 18:[32,1,0], 19:[64,1,1], 20:[64,1,0], 21:[128,1,1], 0:[128,1,0]}

data = []
with open('FullResults.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		row_list = ','.join(row).split(',')
		data.append(row_list)

numQs = len(data[0]) + 1

for row in range(1,len(data)):
	for index in range((numQs / 2 + 1),len(data[row])):
		if data[row][index] == "":
			continue

		result = int(data[row][index])

		q = index + 1
		ground_truth = 2

		# get other info of the image
		mod_index = q % 22
		info = modular_results.get(mod_index)
		blocksize = info[0]
		scramble = info[1]
		grid = info[2]

		if grid == 1:
			if scramble == 1:
				blocksize_entries_with_grid[blocksize] += 1
				if result != ground_truth:
					blocksize_misses_with_grid[blocksize] += 1

		if grid == 0:
			if scramble == 1:
				blocksize_entries_without_grid[blocksize] += 1
				if result != ground_truth:
					blocksize_misses_without_grid[blocksize] += 1

		if scramble == 0:
			original_blocksize_entries_with_grid[blocksize] += 1
			if result != ground_truth:
				original_blocksize_misses_with_grid[blocksize] += 1

		if blocksize == 256:
			blocksize_entries_with_grid[blocksize] += 1
			blocksize_entries_without_grid[blocksize] += 1
			if result != ground_truth:
				blocksize_misses_without_grid[blocksize] += 1
				blocksize_misses_with_grid[blocksize] += 1

# get percent accuracy for each blocksize, with and without grid
blocksizes = [2, 4, 8, 16, 32, 64, 128, 256]
percent_accuracy_with_grid = []
percent_accuracy_without_grid = []
original_percent_accuracy = []
for i in range(0,len(blocksizes)):
	if blocksize_entries_with_grid[blocksizes[i]] == 0:
		percent_accuracy_with_grid.append(0)
	else:
		percent_accuracy_with_grid.append(((float) (blocksize_entries_with_grid[blocksizes[i]]) - (float) (blocksize_misses_with_grid[blocksizes[i]])) / (float) (blocksize_entries_with_grid[blocksizes[i]]))
	
	if blocksize_entries_without_grid[blocksizes[i]] == 0:
		percent_accuracy_without_grid.append(0)
	else:
		percent_accuracy_without_grid.append(((float) (blocksize_entries_without_grid[blocksizes[i]]) - (float) (blocksize_misses_without_grid[blocksizes[i]])) / (float) (blocksize_entries_without_grid[blocksizes[i]]))

	if original_blocksize_entries_with_grid[blocksizes[i]] == 0:
		original_percent_accuracy.append(0)
	else:
		original_percent_accuracy.append(((float) (original_blocksize_entries_with_grid[blocksizes[i]]) - (float) (original_blocksize_misses_with_grid[blocksizes[i]])) / (float) (original_blocksize_entries_with_grid[blocksizes[i]]))
print blocksize_misses_with_grid
print blocksize_entries_with_grid
print blocksize_misses_without_grid 
print blocksize_entries_without_grid
print original_blocksize_misses_with_grid
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