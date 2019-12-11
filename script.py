import pandas as pd
import numpy as np
import graphlab
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer

warnings.filterwarnings('ignore')

df = pd.read_csv('users.csv', sep='\t', names=['user_id','prof_id','subject1', 'subject2','score'])

train_data_df = pd.read_csv('train_data.csv', sep='\t', names=r_cols)
test_data_df = pd.read_csv('test_data.csv', sep='\t', names=r_cols)

tfidf = TfidfVectorizer(stop_words='english')

#Replace NaN with an empty string
metadata['overview'] = metadata['overview'].fillna('')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(metadata['overview'])

#Output the shape of tfidf_matrix
tfidf_matrix.shape

ratings = pd.DataFrame(df.groupby('user_id')['score'].mean())

# Convert the pandas dataframes to graph lab SFrames
train_data = graphlab.SFrame(train_data_df)
test_data = graphlab.SFrame(test_data_df)

# Train the model
collab_filter_model = graphlab.item_similarity_recommender.create(train_data,
                                                                  user_id='user_id',
                                                                  item_id='prof_id',
                                                                  target=['subject1', 'subject2'],
                                                                  similarity_type='score')

# Make recommendations
how_many_recommendations = 10
item_recomendation = collab_filter_model.recommend(users=which_user_ids,
                                                   k=how_many_recommendations)
def get_recommendations(user_id, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[user_id]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the prof indices
    prof_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return metadata['user_id'].iloc[prof_indices]

def get_list(x):
    if isinstance(x, list):
        names = [i['prof_id'] for i in x]
        #Check if more than 3 elements exist. If yes, return only first three. If no, return entire list.
        if len(names) > 3:
            names = names[:3]
        return names
    #Return empty list in case of missing/malformed data
    return []

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''