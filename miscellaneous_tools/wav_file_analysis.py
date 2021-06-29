import os
from pprint import pprint
import numpy as np
from scipy.io import wavfile


BASE_DIRECTORY = 'C:\\Users\\Matthew\\OneDrive\\Free Samples\\Drum Machines\\Music Machines'


def traverse_directory_for_wav_files(directory):
    wav_files = list()
    for object in os.listdir(directory):
        path = os.path.join(directory, object)
        if os.path.isdir(path):
            wav_files.extend(traverse_directory_for_wav_files(path))
        elif os.path.splitext(path)[1].lower() == '.wav':
            wav_files.append(path)
    return wav_files


def main():
    wav_files = traverse_directory_for_wav_files(BASE_DIRECTORY)
    instruments = dict()
    for wav_file in wav_files:
        bitrate, data = wavfile.read(wav_file)
        spectrum = np.abs(np.fft.rfft(data))
        frequency = np.fft.rfftfreq(len(data), d=1/bitrate)
        amplitude = spectrum / spectrum.sum()
        mean_frequency = (frequency * amplitude).sum()
        length = len(data) / bitrate
        instrument = wav_file.split(os.sep)[-2]
        instrument_data = instruments.get(instrument)
        if instrument_data:
            sample_count = instrument_data['samples']
            mean_frequency_numerator = (instrument_data['mean_frequency'] * sample_count) + mean_frequency
            mean_length_numerator = (instrument_data['mean_length'] * sample_count) + length
            instruments[instrument] = {
                'samples': sample_count + 1,
                'mean_frequency': mean_frequency_numerator / (sample_count + 1),
                'mean_length': mean_length_numerator / (sample_count + 1),
            }
        else:
            instruments[instrument] = {
                'samples': 1,
                'mean_frequency': mean_frequency,
                'mean_length': length,
            }
        print(wav_file, mean_frequency, length)
    pprint(instruments)


if __name__ == '__main__':
    main()
