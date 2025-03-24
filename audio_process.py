import pyaudio
import threading
import numpy as np


class Audio():
    def __init__(self, device_index, rate=44100, chunk=1024):
        self.rate = rate
        self.chunk = chunk
        self.device_index = device_index
        self.audio_level = 0
        self.running = False

        self.p = pyaudio.PyAudio()
        self.stream = None
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.record)
        self.thread.start()

    def record(self):
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.rate, input=True, frames_per_buffer=self.chunk, input_device_index=self.device_index)

        while self.running:
            data = np.frombuffer(self.stream.read(self.chunk, exception_on_overflow=False), dtype=np.int16)
            self.audio_level = np.abs(data).mean()

    def stop(self):
        self.running = False

        if self.thread:
            self.thread.join()

        if self.stream:
            self.stream.stop_stream()
            self.stream.close()

        self.p.terminate()

    def get_audio_level(self):
        return self.audio_level
