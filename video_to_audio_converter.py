import moviepy.editor

filename=input("Enter the video file path: ")
video=moviepy.editor.VideoFileClip(filename)

audio=video.audio

audioname=input("Enter the name of converted audio file you want to give with .mp3 extension: ")

audio.write_audiofile(audioname + ".mp3") 
