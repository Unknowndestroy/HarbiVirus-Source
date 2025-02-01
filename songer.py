from pydub import AudioSegment
from pydub.playback import play

# MP3 dosyasını yükle
song = AudioSegment.from_mp3("glitchsong.mp3")

# Ses seviyesini artır (dB cinsinden)
song = song + 30  # Ses seviyesini 30 dB artırmak

# Sesi çal
play(song)
