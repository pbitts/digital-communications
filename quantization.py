import numpy as np


class Quantization:
    def __init__(self, signal_x_values: list, signal_y_values: list, sample_catcher_frequency: float):
        self.signal_x_values = np.array(signal_x_values)
        self.signal_y_values = np.array(signal_y_values)
        self.sample_catcher_frequency = sample_catcher_frequency

        self.samples = None
        self.time_hops = None
        self.quantization_values = None
        self.indexes = None
        self.quantization_levels = 0
        self.delta = 0

    def sample_catcher(self) -> dict:
        """Efficiently sample the signal using interpolation."""
        period = 1 / self.sample_catcher_frequency
        self.time_hops = np.arange(0, self.signal_x_values[-1] + period, period)

        # Interpolate the y values at desired sample times
        self.samples = np.interp(self.time_hops, self.signal_x_values, self.signal_y_values)

        return {'y': self.samples, 'x': self.time_hops}

    def mid_rise(self, bits_resolution: int):
        """Mid-rise quantization using vectorized operations."""
        self.quantization_levels = 2 ** bits_resolution
        y_min = self.samples.min()
        y_max = self.samples.max()
        self.delta = (y_max - y_min) / self.quantization_levels

        # Compute quantization indexes
        self.indexes = np.floor((self.samples - y_min) / self.delta).astype(int)
        self.indexes = np.clip(self.indexes, 0, self.quantization_levels - 1)

        self.quantization_values = y_min + (self.indexes + 0.5) * self.delta
        return self.quantization_values, self.indexes

    def quantization_error(self):
        """Return the quantization error."""
        return self.samples - self.quantization_values
