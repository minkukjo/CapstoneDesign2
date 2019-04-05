import sys
import requests
import pyaudio
import wave
import time

def record_sound():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # only mono
    RATE = 16000
    CHUNK = 1024  # 스트림에서 읽는 프레임의 샘플 수
    RECORD_SECONDS = 3  # 3초 녹음
    now = time.localtime()
    fileName = "%02d-%02d-%02d:%02d:%02d" % (now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    global WAVE_OUTPUT_FILENAME
    WAVE_OUTPUT_FILENAME = fileName+".wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def startConnection():

    url = "http://13.124.216.150:5000/"
    print(url)
    
    files = {'file': open(WAVE_OUTPUT_FILENAME, 'rb')}

    r = requests.post(url, files=files)
    r.text
    print(r)

if __name__ == '__main__':
    record_sound()
    startConnection()

