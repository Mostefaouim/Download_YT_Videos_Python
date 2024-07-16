# Import the necessary module from pytube
from pytube import YouTube

# Prompt the user to enter the URL of the video they want to download
video_url = input("Enter The Link Of Video: ")

# Prompt the user to enter the path where the video should be saved
save_path = input("Enter The Path Where To Save The Video: ")

# Create a YouTube object using the provided video URL
yt = YouTube(video_url)

# Get the highest resolution stream available for the video
video = yt.streams.get_highest_resolution()

# Print the title of the video being downloaded
print(f"Downloading {yt.title}")

# Download the video to the specified path
video.download(save_path)

# Notify the user that the download is complete
print("Download finished!")
