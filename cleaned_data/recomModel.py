## remember gl-env should be activated
## and python2 should be run

import graphlab
import pandas as pd

# Reading csv file
sf = graphlab.SFrame(data = './turiRecomen.csv')
sf.rename(names={'userid':'user_id',
                'isbn':'item_id','bookrating':'rating'})

m = graphlab.recommender.create(sf, target='rating')
recs = m.recommend()
recs.to_dataframe().to_csv("recommendation.csv",index = None)
