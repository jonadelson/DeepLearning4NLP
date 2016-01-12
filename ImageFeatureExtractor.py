import Util
from scipy.misc import imread
import urllib2

def get_image_from_submission(submission):
    thumbnail_url = submission.thumbnail
    image_fid = urllib2.urlopen(thumbnail_url)
    
    
def get_thumbnail_feature_from_submission(submission):
    """
    Given a praw Submission object, get a 4096 dimensional feature vector 
    for its thumbnail,
    
    or None if there is no thumbnail
    """
    pass
    
def get_image_features_from_full_ids(full_ids):
    """
    Given an iterable of full_id for reddit posts,
    get all image features for these posts
    """
    submissions = Util.reddit_api.get_submissions(full_ids)
    images = [get_image_from_submission(sub) for sub in submissions]

