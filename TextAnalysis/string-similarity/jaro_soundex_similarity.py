import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
from jellyfish import soundex, jaro_similarity

# load the cognomi.csv file as a dataframe
df = pd.read_csv('surnames.csv')

similarity_df = pd.DataFrame(columns=['surname1', 'surname2', 'jaro_soundex_similarity'])

for i in range(len(df)):
    surname1 = df['surname'][i]
    print(surname1)
    
    for j in range(i+1, len(df)):
        surname2 = df['surname'][j]
        jaro_sim = jaro_similarity(soundex(surname1), soundex(surname2))
        similarity_df = similarity_df.append({'surname1': surname1, 'surname2': surname2, 'jaro_soundex_similarity' : jaro_sim}, ignore_index=True)

# save the new dataframe to a file
similarity_df.to_csv('jaro_soundex_similarity.csv', index=False)

candidates_jaro_df = similarity_df[similarity_df['jaro_soundex_similarity'] >= 0.9].reset_index(drop=True)
candidates_jaro_df.to_csv('candidates_jaro_soundex.csv', index=False)