import pyaudio
import sys
import struct
import numpy
from pylab import *
import numpy


chunk = 1024
FORMAT = pyaudio.paInt16  # 16-bit integers
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()

#temp = raw_input('File name? ')
#temp += ".txt"
#print(temp)

file = open(str(sys.argv[1]), "rb")
snddata = file.read()


print ("* playing")
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=chunk)

stream.write(snddata)
stream.stop_stream()
stream.close()
print ("* done")

p.terminate()
