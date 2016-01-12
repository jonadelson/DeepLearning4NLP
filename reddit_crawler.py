import praw
import time 
import pickle
import sys

def main(argv):

	limit = int(argv[1]) # Number of posts to collect each call
	sleep = int(argv[2]) # Time to sleep between calls
	out_file = argv[3]   # File to dump reddit objects

	post_ids = set() # ID set so we don't collect same ones twice

	f = open(out_file, 'wb')

	r = praw.Reddit('Data Collection') 

	# Run until keyboard interruption
	loop = True
	while loop:
		try:
			new_front_page = r.get_new(limit=limit)

			new_posts = [post for post in new_front_page if post.id not in post_ids]
			
			# Just cotinue if we got nothing
			if len(new_posts) == 0:
				continue

			# Update the set of post ids
			post_ids.update([post.fullname for post in new_posts])

			# Print some information
			print "Collected {} new posts".format(len(new_posts))
			print "Title of last new post = {}".format(new_posts[-1].title)
			
			#Sleep till next call
			time.sleep(sleep)

		# Sleep until next call
		except praw.errors.HTTPException:
			continue
		except UnicodeEncodeError:
			pass
		except KeyboardInterrupt:
			pickle.dump(post_ids, f)
			loop = False
			break

if __name__ == "__main__":
	main(sys.argv)