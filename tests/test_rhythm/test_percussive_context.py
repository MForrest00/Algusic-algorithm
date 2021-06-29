import unittest
from algorithm.rhythm import PercussiveContext


class TestPercussiveContext(unittest.TestCase):
    def test_generate_percussive_context(self):
        percussive_context = PercussiveContext()
        for i, sample in enumerate(percussive_context.samples):
            if i > 0:
                self.assertGreaterEqual(sample.mean_frequency, percussive_context.samples[i - 1].mean_frequency)
            self.assertLessEqual(sample.length, percussive_context.maximum_sample_length)
