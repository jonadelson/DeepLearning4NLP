import Util

def get_image_from_post(post):
    
    
def get_image_features_from_full_ids(full_ids):
    submissions = Util.reddit_api.get_submissions(full_ids)

p = praw.Reddit('Data Collection') 
ids = ['t3_40n9x2','t3_40mj8x']
#s1 = p.get_submission(submission_id=ids[0])
subs = p.get_submissions(ids)