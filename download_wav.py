import yt_dlp
def download_wav(url): #download a song from a url
    URLS = url
    ydl_opts = {
        'format': 'wav/bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }]
    

    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)
    
def search_for_song(song_name): #search for a song and download it
    ydl_opts = {
        'format': 'wav/bestaudio/best',
        'default_search': 'ytsearch',
        'outtmpl': 'song.%(ext)s',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download([song_name])

