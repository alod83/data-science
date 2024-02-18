import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
from jellyfish import levenshtein_distance

# load the cognomi.csv file as a dataframe
df = pd.read_csv('surnames.csv')

similarity_df = pd.DataFrame(columns=['surname1', 'surname2', 'levenshtein_distance'])

for i in range(len(df)):
    surname1 = df['surname'][i]
    print(surname1)
    
    for j in range(i+1, len(df)):
        surname2 = df['surname'][j]
        leven_distance = levenshtein_distance(surname1, surname2)
        similarity_df = similarity_df.append({'surname1': surname1, 'surname2': surname2, 'levenshtein_distance' : leven_distance}, ignore_index=True)

# save the new dataframe to a file
similarity_df.to_csv('leven_similarity.csv', index=False)

candidates_levenshtein_df = similarity_df[similarity_df['levenshtein_distance'] <= 1].reset_index(drop=True)
candidates_levenshtein_df.to_csv('candidates_levenshtein.csv', index=False)