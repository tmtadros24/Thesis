import numpy as np
import matplotlib.pyplot as plt

def load_results(results):
    correct = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    indoor_correct = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    outdoor_correct = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for entry in results:
        image_number = int(entry[2])
        ground_truth = int(entry[3])
        result = int(entry[4])
        if ( image_number == 12 ):
            print result
            print ground_truth

        if ( ground_truth == result ):
            correct[image_number] += 1

        if ( ground_truth == 0 and ground_truth == result ):
            indoor_correct[image_number] += 1

        if ( ground_truth == 1 and ground_truth == result ) :
            outdoor_correct[image_number] += 1
    return correct, indoor_correct, outdoor_correct

def load_results_from_file(file):
    correct = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    indoor_correct = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    outdoor_correct = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    f = open(file, 'r')
    for line in f:
        entry = line.split()
        image_number = int(entry[2])
        ground_truth = int(entry[3])
        result = int(entry[4])
        if ( ground_truth == result ):
            correct[image_number] += 1

        if ( ground_truth == 0 and ground_truth == result ):
            indoor_correct[image_number] += 1

        if ( ground_truth == 1 and ground_truth == result ) :
            outdoor_correct[image_number] += 1
    return correct, indoor_correct, outdoor_correct
	# plot the two sets of points
	#plt.plot(blocksizes, percent_accuracy_with_grid, marker='o', color='b')
	#plt.plot(blocksizes, percent_accuracy_without_grid, marker='o', color='g')
	#plt.plot(blocksizes, original_percent_accuracy, marker='o', color='r')
	#plt.xlabel("blocksize")
	#plt.ylabel("Percent Correct")
	#plt.legend(["with grid", "without grid", "unscrambled image"], loc='lower center')
	#axes = plt.gca()
	#axes.set_ylim([-.1,1.1])
	#plt.show()

def plot_blurred_images(correct, full):
    num = 200
    indices = [19, 0, 1, 2, 3, 4, 5, 6]
    error_rate = [0, 0, 0, 0, 0, 0, 0, 0]
    xaxis = [0, 2, 4, 8, 16,32,64,128]
    if (full == 1):
        num = 100

    for i in range(0,len(indices)):
        print indices[i]
        print correct[indices[i]]
        error_rate[i] = float(float(correct[indices[i]]) / float(num))
        print error_rate[i]

    plt.plot(xaxis, error_rate, marker='o', color='b')
    plt.xlabel("Blur Level")
    plt.ylabel("Percent Correct")
    axes = plt.gca()
    axes.set_ylim([-.1,1.1])
    plt.show()

def plot_noisy_images(correct, full):
    num = 200
    indices = [19, 8, 9, 10, 11]
    error_rate = [0, 0, 0, 0, 0,]
    xaxis = [0, .2, .4, .6, .8]
    if (full == 1):
        num = 100

    for i in range(0,len(indices)):
        print indices[i]
        print correct[indices[i]]
        error_rate[i] = float(float(correct[indices[i]]) / float(num))
        print error_rate[i]

    plt.plot(xaxis, error_rate, marker='o', color='b')
    plt.xlabel("Noise Level")
    plt.ylabel("Percent Correct")
    axes = plt.gca()
    axes.set_ylim([-.1,1.1])
    plt.show()

def plot_scrambled_images(correct, full):
    num = 200
    original_indices = [12, 13, 14, 15, 16, 17, 18, 19]
    original_error_rate = [0, 0, 0, 0, 0, 0, 0, 0]

    scrambled_grid_indices = [21, 23, 25, 27, 29, 31, 33, 19]
    scrambled_grid_error_rate = [0, 0, 0, 0, 0, 0, 0, 0]

    scrambled_no_grid_indices = [22, 24, 26, 28, 30, 32, 34, 19]
    scrambled_no_grid_error_rate = [0, 0, 0, 0, 0, 0, 0, 0]

    xaxis = [2, 4, 8, 16, 32, 64, 128, 256]
    if (full == 1):
        num = 100

    for i in range(0,len(original_indices)):
        original_error_rate[i] = float(float(correct[original_indices[i]]) / float(num))


    for i in range(0,len(scrambled_grid_indices)):
        scrambled_grid_error_rate[i] = float(float(correct[scrambled_grid_indices[i]]) / float(num))


    for i in range(0,len(scrambled_no_grid_indices)):
        scrambled_no_grid_error_rate[i] = float(float(correct[scrambled_no_grid_indices[i]]) / float(num))

	# plot the two sets of points
    plt.plot(xaxis, scrambled_grid_error_rate, marker='o', color='b')
    plt.plot(xaxis, scrambled_no_grid_error_rate, marker='o', color='g')
    plt.plot(xaxis, original_error_rate, marker='o', color='r')
    plt.xlabel("blocksize")
    plt.ylabel("Percent Correct")
    plt.legend(["with grid", "without grid", "unscrambled image"], loc='lower center')
    axes = plt.gca()
    axes.set_ylim([-.1,1.1])
    plt.show()

def plot_greyscale(correct, full):
    num = 200
    indices = [19, 7]
    error_rate = [0, 0]
    xaxis = [0, 1]
    if (full == 1):
        num = 100

    for i in range(0,len(indices)):
        error_rate[i] = float(float(correct[indices[i]]) / float(num))

    plt.bar([0,1], error_rate, 1, color='b')
    plt.xlabel("Greyscale Level (1)")
    plt.ylabel("Percent Correct")
    axes = plt.gca()
    axes.set_ylim([-.1,1.1])
    plt.show()

def plot_colors(correct, full):
    num = 200
    indices = [19, 20]
    error_rate = [0, 0]
    xaxis = [0, 1]
    if (full == 1):
        num = 100

    for i in range(0,len(indices)):
        error_rate[i] = float(float(correct[indices[i]]) / float(num))

    plt.bar([0,1], error_rate, 1, color='b')
    plt.xlabel("Reversed colors (1)")
    plt.ylabel("Percent Correct")
    axes = plt.gca()
    axes.set_ylim([-.1,1.1])
    plt.show()

correct, indoor, outdoor = load_results_from_file('SVMResults.txt')

plot_blurred_images(correct, 0)
plot_blurred_images(indoor, 1)
plot_blurred_images(outdoor, 1)

plot_noisy_images(correct, 0)
plot_noisy_images(indoor, 1)
plot_noisy_images(outdoor, 1)

plot_scrambled_images(correct, 0)
plot_scrambled_images(indoor, 1)
plot_scrambled_images(outdoor, 1)

plot_greyscale(correct, 0)
plot_greyscale(indoor, 1)
plot_greyscale(outdoor, 1)

plot_colors(correct, 0)
plot_colors(indoor, 1)
plot_colors(outdoor, 1)
