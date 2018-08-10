import pytube
import  os

print("Enter you yt link")
link = input()
yt = pytube.YouTube(link)
videos = yt.fmt_streams
s = 1
for v in videos:
    print(str(s) + ". " + str(v))
    s += 1

print("Enter your download number")

n = int(input())
vid = videos[n-1]

destination = r"C:\Users\Aish\Desktop\yt"

#C:\Users\Aish\Desktop\yt\
des =os.path.join(destination)
vid.download(des)