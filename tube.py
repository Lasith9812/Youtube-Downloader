from pytube import YouTube

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