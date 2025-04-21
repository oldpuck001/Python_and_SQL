# mutagen_mp3.py

from mutagen.id3 import ID3, ID3NoHeaderError, TIT2, TPE1, TALB, COMM
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

mp3_file_path = '/Users/lei/Downloads/a.mp3'

# 假設mp3_file_path是你的MP3文件路徑
try:
    tags = ID3(mp3_file_path)
except ID3NoHeaderError:
    print("No ID3 tag found.")
    tags = ID3()                # 初始化一個空的ID3對象，如果需要的話

# 獲取歌曲標題
title = tags.get('TIT2')
if title is not None:
    title = title.text[0]
else:
    title = 'Unknown Title'

# 獲取歌手名稱
artist = tags.get('TPE1')
if artist is not None:
    artist = artist.text[0]
else:
    artist = 'Unknown Artist'

# 獲取專輯名稱
album = tags.get('TALB')
if album is not None:
    album = album.text[0]
else:
    album = 'Unknown Album'

print(f'Title: {title}')
print(f'Artist: {artist}')
print(f'Album: {album}')


# 修改標籤
print(EasyID3.valid_keys.keys())
audio = MP3(mp3_file_path, ID3=EasyID3)
audio['title'] = 'my title'
audio['artist'] = 'my artist'
audio['album'] = 'my album'
audio.save()


# 再次讀取
# 假設mp3_file_path是你的MP3文件路徑
try:
    tags = ID3(mp3_file_path)
except ID3NoHeaderError:
    print("No ID3 tag found.")
    tags = ID3()                # 初始化一個空的ID3對象，如果需要的話

# 獲取歌曲標題
title = tags.get('TIT2')
if title is not None:
    title = title.text[0]
else:
    title = 'Unknown Title'

# 獲取歌手名稱
artist = tags.get('TPE1')
if artist is not None:
    artist = artist.text[0]
else:
    artist = 'Unknown Artist'

# 獲取專輯名稱
album = tags.get('TALB')
if album is not None:
    album = album.text[0]
else:
    album = 'Unknown Album'

print(f'Title: {title}')
print(f'Artist: {artist}')
print(f'Album: {album}')