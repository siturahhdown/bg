from pytube import YouTube
import os

def download_audio(url):
    try:
        yt = YouTube(url) 
        video = yt.streams.filter(only_audio=True).first() 

        print("Enter the destination (leave blank for current directory)") 
        destination = str(input(">> ")) or '.'

        out_file = video.download(output_path=destination) 

        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 

        print(yt.title + " has been successfully downloaded as audio.")
    except Exception as e:
        print(f"An error occurred while downloading audio: {e}")

def download_video(url):
    try:
        video = YouTube(url)
        print(f"Title: {video.title}")
        print(f"Number of views: {video.views}")
        print(f"Length of video: {video.length} seconds")
        print(f"Description: {video.description}")
        print(f"Ratings: {video.rating}")

        downloader = video.streams.get_highest_resolution()
        print(f"Downloading {video.title}...")
        destination = input("Enter the destination (leave blank for default Downloads folder): ") or "C:/Users/your_username/Downloads"
        downloader.download(destination)
        print(f"Download completed!! {video.title}")
    except Exception as e:
        print(f"An error occurred while downloading video: {e}")

while True:
    ask = input("Do you want to download a video or audio? (video/audio/exit) ")
    if ask.lower() == "video":
        url = input("Enter your url > ")
        download_video(url)
    elif ask.lower() == "audio":
        url = input("Enter the URL of the video you want to download audio from: \n>> ")
        download_audio(url)
    elif ask.lower() == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose 'video', 'audio', or 'exit'.")