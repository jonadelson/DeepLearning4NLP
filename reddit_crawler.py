import praw
import time 
import pickle
from exceptions import UnicodeEncodeError
import sys

def main(argv):

	limit = int(argv[1]) # Number of posts to collect each call
	sleep = int(argv[2]) # Time to sleep between calls
	out_file = argv[3]   # File to dump reddit objects

	post_ids = set() # ID set so we don't collect same ones twice

	f = open(out_file, 'wb')

	r = praw.Reddit('Data Collection') 

	# Run until keyboard interruption
	while True:
		
		new_front_page = r.get_new(limit=limit)

		# Catch any errors in collecting the posts 
		try:
			new_posts = [post for post in new_front_page if post.id not in post_ids]
		except praw.errors.HTTPException:
			print "error"
			continue

		# Just cotinue if we got nothing
		if len(new_posts) == 0:
			continue

		# Update the set of post ids
		post_ids.update([post.id for post in new_posts])

		# Print last post title
		print "Collected {} new posts".format(len(new_posts))
		try:
			print "Title of last new post = {}".format(new_posts[-1].title)
		except UnicodeEncodeError:
			pass

		# Write comment list to file
		print "Writing reddit comment object list to file"
		pickle.dump(new_posts, f)

		# Sleep until next call
		time.sleep(sleep)

if __name__ == "__main__":
	main(sys.argv)