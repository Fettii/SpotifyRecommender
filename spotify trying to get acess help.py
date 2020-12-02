import requests
import base64
import json
from secrets import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time 
client_id = '7bbf0bdef81f4d2a9569475b25dd28b3'
client_secret = '7cec56f6f15a4e679f5803997dd79c94'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Step 1: Collect user data from user input
runner=True
counter=0
library=dict()
lookie=''
while runner and counter<=20:
  song_collector=input("Please enter track name: ")
  if song_collector=="stop":
    runner=False
  else:
    library.update({"track "+str(counter):song_collector})
    artist_collector=input("artist name: ")
    library.update({"artist "+str(counter):artist_collector})
    counter+=1


#Step 2: Convert User data from dictionary into list
dude=list(library.values())


#Step 3: Take the name of artist and track and convert  into the track info
def this_gets_id_from_keys(tracklist):
    tracks=[]
    x=0
    for i in range(len(tracklist)//2):
        print("Track input accepted")
        track_id = sp.search(q='artist:' + tracklist[x+1] + ' track:' + tracklist[x], type='track',limit=1)
        tracks.append(track_id)
        x+=2
    return tracks


the_key=this_gets_id_from_keys(dude)

countEveryIDnum=(len(dude)//2)

#Step 4: Extract track ID from track info
def getTrackIDs(track_ids):
    ids=[]
    for i in range(countEveryIDnum):
        for item in track_ids[i]['tracks']['items']:
           track=item['id']
           ids.append(track)
    return ids
player=getTrackIDs(the_key)  

#Step 5: Look into track ID and extract metadata(stats)
def getTrackFeatures(id):
  meta = sp.tracks(id)
  data=[]
  # meta
  for i in range(countEveryIDnum):
    name = meta['tracks'][i]['name']
    album = meta['tracks'][i]['album']['name']
    artist = meta['tracks'][i]['artists'][0]['name']
    popularity = meta['tracks'][i]['popularity']
    pack=["song title: "+name,"album: "+album,"artist: "+artist,(popularity)]
    data.append(pack)
  return data
    #Spotify doesnt allow users to see song genre because they are greedy so I can only find genre of the artist;so it might be less acrruate...
    #artist = meta(['tracks'][0]["artists"][0]["external_urls"][0]["spotify"])
    #print("artist genres:", artist["genres"])
player=getTrackFeatures(player)
#Step 6:  Create a menu to select different options for your data

Quitter=True
while Quitter:
    popularity_avg=0
    print((" "))
    print((" "))
    print("Now all the things you can do with your music data :) ")
    print((" "))
    print("W- print out a list of your song selections")
    print((" "))
    print("R- See how mainstream your music taste is")
    print((" "))
    print("Q- Quit")
    print((" "))
    userinput=input("Please Select a command: ")
    if userinput=="Q":
        Quitter=False
    elif userinput=="R":
        print((" "))
        x=0
        for i in range(len(player)):
            popularity_avg+=player[i][3]
            x+=1
        popularity_avg=popularity_avg/x    
        print("Out of 10,how mainstream your taste in music is...: "+str(popularity_avg//10)+"!")
        if popularity_avg<25:
            print("Wow you really stray away from mainstream songs and listen to underground music")
        elif 25<=popularity_avg<50:
            print("You seem to listen to artists lesser known songs and sometimes tend to avoid the biggest hits")    
        elif 50<=popularity_avg<75:
            print("Ok you kinda listen to some hit songs and also stray towards indie songs; a mix")    
        else:
            print("Must be only the hottest songs for you! Very Mainstream")     
    elif userinput=="W":
        print(" ")               
        print(player)
        print(" ")
    else:
        print("I dont know that command, sorry!")
        print((" "))
        print((" "))    

 









