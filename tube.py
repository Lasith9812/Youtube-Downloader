from pytube import YouTube
from pytube import Playlist


y = int(input("Download single video[1] or Playlist[2] : "))

if y == 1:
    while True:
        url = input("Input URL: ")
        yt = YouTube(url)
        print(yt.title)
        llls = yt.streams.filter(adaptive=True)
        for i in range(0,int(len(llls))):
            print(llls[i])
        ta = int(input("Enter tag number : "))
        vid = yt.streams.get_by_itag(ta)
        vid.download()
        print("Download Completed")
else:
    tag_no = "Nope"
    url = input("Input URL: ")
    yt = Playlist(url)
    for vid in yt.videos:
        lsss = str(vid).split('=')[1]
        lsss = lsss.replace('>','')
        link = str("https://www.youtube.com/watch?v=")+str(lsss)
        video = YouTube(link)
        qua = video.streams.filter(adaptive=True)
        for i in range(0,int(len(qua))):
                print(qua[i])
        if tag_no == "Nope":
            ta = int(input("Enter tag number : "))
            tag_no = "yes"
            vids = video.streams.get_by_itag(ta)
            print("Downloading",str(video.title))
            vids.download()
            print("Download Completed",str(video.title))
        else:
            vids = video.streams.get_by_itag(ta)
            print("Downloading",str(video.title))
            vids.download()
            print("Download Completed",str(video.title))