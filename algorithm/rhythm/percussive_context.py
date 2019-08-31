from bisect import bisect_left
from collections import namedtuple
import os
import numpy as np
from scipy.io import wavfile


Sample = namedtuple('Sample', ['mean_frequency', 'length', 'sample_set', 'instrument_name', 'file_path'])


class PercussiveContext:

    def __init__(self, sample_directory=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'percussion'),
                 maximum_sample_length=1.0):
        self.sample_directory = sample_directory
        self.maximum_sample_length = maximum_sample_length
        self.samples = self.retrieve_samples()

    def retrieve_wav_files(self, directory):
        wav_files = list()
        for object in os.listdir(directory):
            path = os.path.join(directory, object)
            if os.path.isdir(path):
                wav_files.extend(self.retrieve_wav_files(path))
            elif os.path.splitext(path)[1].lower() == '.wav':
                wav_files.append(path)
        return wav_files

    def retrieve_samples(self):
        sample_files = self.retrieve_wav_files(self.sample_directory)
        samples = list()
        keys = list()
        for sample_file in sample_files:
            bitrate, data = wavfile.read(sample_file)
            length = len(data) / bitrate
            if length > self.maximum_sample_length:
                continue
            spectrum = np.abs(np.fft.rfft(data))
            frequency = np.fft.rfftfreq(len(data), d=1/bitrate)
            amplitude = spectrum / spectrum.sum()
            mean_frequency = (frequency * amplitude).sum()
            sample_set = sample_file.split(os.sep)[-3]
            instrument_name = sample_file.split(os.sep)[-2]
            index = bisect_left(keys, mean_frequency)
            keys.insert(index, mean_frequency)
            samples.insert(index, Sample(mean_frequency, length, sample_set, instrument_name, sample_file))
        return samples
