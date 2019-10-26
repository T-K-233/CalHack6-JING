import pyaudio
import tts
import wave
obj = wave.open('test.wav','r')
print( "Number of channels",obj.getnchannels())
print ( "Sample width",obj.getsampwidth())
print ( "Frame rate.",obj.getframerate())
print ("Number of frames",obj.getnframes())
print ( "parameters:",obj.getparams())
obj.close()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 24000
RECORD_SECONDS = 5


p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    output = True,
    frames_per_buffer = chunk)


data = tts.textToSpeech("Test content", "test.as")


stream.write(data)
