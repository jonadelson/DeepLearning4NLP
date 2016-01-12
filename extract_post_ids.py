import os
import sys
import pickle

def main(argv):
	directory_name = sys.argv[1]
	out_file = sys.argv[2]

	file_names = os.listdir(directory_name)

	out_file = open(out_file, 'wb')


	submission_ids = set()

	for file_name in file_names:
		file_name = '/'.join([directory_name, file_name])
		print "Working on file {}".format(file_name)
		f = open(file_name)
		while True:
			try:
				submission_list = pickle.load(f)
				ids = [submission.fullname for submission in submission_list]
				submission_ids.update(ids)
			except EOFError:
				break

	pickle.dump(submission_ids, out_file)

if __name__ == "__main__":
	main(sys.argv)

