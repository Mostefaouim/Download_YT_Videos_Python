from pytube import YouTube

video_url = input("Enter The Link Of Video: ")

save_path = input("Enter The Path Where To Save The Video: ")

yt = YouTube(video_url)

video = yt.streams.get_highest_resolution()

print(f"Downloading {yt.title}")

video.download(save_path)

print("Download finished!")
