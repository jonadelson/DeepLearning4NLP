import Util
import numpy as np

def read_glove_vector(file_line):
	"""
	Read in one word vector from the file
	Each line comes in as a word followed by the 
	300 dimensional vector where each coordinate is
	separated by a space
	"""
	split_line = file_line.split()
	word, vector = split_line[0], split_line[1:]
	vector = np.asarray([float(num) for num in vector], dtype='float32')

	return word, vector

def read_glove_vectors(file_name, word_set):
	"""
	Read in words from the file and yield the word/vector
	if they are in the word set
	"""
	for word_vector in open(file_name):
		word, vector = read_glove_vector(word_vector)
		if word in word_set:
			yield word, vector