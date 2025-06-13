#!/usr/bin/env python
# coding: utf-8

# In[6]:


import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="1b8bc780d59c42c8a6e009036cd08885",
    client_secret="7eed8aba12804843845a949d9cc1b770",
    redirect_uri="http://127.0.0.1:8888/callback/",
    scope="user-read-recently-played"
))

recent_tracks = sp.current_user_recently_played(limit=50)  
tracks_data = [{
    'played_at': item['played_at'],
    'track_name': item['track']['name'],
    'artist_name': item['track']['artists'][0]['name'],
    'album': item['track']['album']['name'],
    'release_date': item['track']['album']['release_date'],
    'duration_ms': item['track']['duration_ms'],
    'track_id': item['track']['id'],
    'track_uri': item['track']['uri']
} for item in recent_tracks['items']]

df = pd.DataFrame(tracks_data)
df.head()



# In[7]:


df.to_csv('recent_tracks.csv', index=False)
print("recent tracks data saved to 'recent_tracks.csv'")


# In[ ]:




