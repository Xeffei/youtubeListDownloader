import os
import google.auth
import google.auth.transport.requests
import google.auth.transport.urllib3
import google.oauth2.credentials
import pytube
import requests
from pydub import AudioSegment


# Replace YOUR_API_KEY with your own API key
API_KEY = "enter api key" #youtube un size verdiği api key

# Replace PLAYLIST_ID with the ID of the playlist you want to download
PLAYLIST_ID = "enter playlst id" #playlist id si

SAVE_DIR = "videos" # kaydedilecek dosyanın adı

# Set the API endpoint
ENDPOINT = "https://www.googleapis.com/youtube/v3/playlistItems"

# Set the parameters for the API request
PARAMETERS = {
    "part": "contentDetails",
    "playlistId": PLAYLIST_ID,
    "key": API_KEY,
    "maxResults": 50
}



# Create the save directory if it doesn't exist
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Set the initial page token to an empty string
page_token = ""

# Set the counter for the number of videos downloaded
count = 0

# Set the flag to indicate whether there are more pages
more_pages = True

while more_pages:
    # Set the page token parameter
    PARAMETERS["pageToken"] = page_token

    # Send the API request
    response = requests.get(ENDPOINT, params=PARAMETERS)

    # Get the JSON data from the response
    data = response.json()
    items=[]
    # Get the items from the data
    
    if "items" in data:
        items = data["items"]
    else:
        print("The 'items' key does not exist in the dictionary")

    
    # Iterate through the items
    for item in items:
        # Get the video ID
        try:
            video_id = item["contentDetails"].get("videoId", "")
            
            # Get the video URL
            if(video_id != "UcRtFYAz2Yo"):
                video_url = f"https://www.youtube.com/watch?v={video_id}"
            else:continue
            # Download the video
            video = pytube.YouTube(video_url)
            # Import the AudioSegment class
            from pydub import AudioSegment

            # Get the highest quality video and audio streams
            try:
                
                video_stream = video.streams.filter(progressive=True).order_by("resolution").desc().first().download(SAVE_DIR)
                print(count,"  ",video_stream)
            except:""

             # Download the video and audio streams
        
            
        
        except:
            ""
        count += 1

    # Check if there are more pages
    if "nextPageToken" in data:
        page_token = data["nextPageToken"]
    else:
        more_pages = False

# Print the number of videos downloaded
print(f"{count} videos downloaded")
