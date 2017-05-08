import pyaudio, wave, datetime
from struct import pack
import wave

BUFFER_SIZE = 512
REC_SECONDS = 5
RATE = 44100
#WAV_FILENAME = utils.generate_random_token()
WAV_FILENAME = "Test"+str(datetime.datetime.now())
FORMAT = pyaudio.paInt16

#init sound stream
pa = pyaudio.PyAudio()
stream = pa.open(
    format = FORMAT,
    input = True,
    channels = 1,
    rate = RATE,
    #input_device_index=1,
    frames_per_buffer = BUFFER_SIZE
)

#run recording
print('Recording...')
data_frames = []
for f in range(0, RATE/BUFFER_SIZE * REC_SECONDS):
    data = stream.read(BUFFER_SIZE)
    data_frames.append(data)

print('Finished recording...')
stream.stop_stream()
stream.close()
pa.terminate()

#finaldata = pack('<' + ('h' * len(data_frames)), *data_frames)

#wave_file = wave.open(WAV_FILENAME, 'wb')
#wave_file.setnchannels(1)
#wave_file.setsampwidth(BUFFER_SIZE)
#wave_file.setframerate(RATE)
#wave_file.writeframes(finaldata)
#wave_file.close()

