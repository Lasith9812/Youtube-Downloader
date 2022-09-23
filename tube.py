from pytube import YouTube



while True:
    url = input("Input URL: ")
    yt = YouTube(url)
    print(yt.title)
    vid = yt.streams.get_by_itag(160)
    vid.download()
