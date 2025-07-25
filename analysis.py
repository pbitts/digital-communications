from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

from waveproducer import Wave
from quantization import Quantization


def process(sinewave_resolution: int = 1000,
                    sinewave_frequency: float = 1, 
                    sinewave_amplitude: float = 10, 
                    sinewave_dc_offset: float = 0, 
                    quant_resolution: int = 4,
                    sample_catcher_frequency: int = 100):
    
    #Initiate class instance and produce a sine wave 
    #1000 bits, 1Hz frequency, 10 Volts amplitude and 0 Volts DC
    wave = Wave()
    signal = wave.sine(sinewave_resolution,
                       sinewave_frequency,
                       sinewave_amplitude,
                       sinewave_dc_offset)

    #Initiate class instance and cacth discrete samples 
    #Impulse frequency 30Hz
    quantization = Quantization(signal['x'], signal['y'], sample_catcher_frequency )
    samples = quantization.sample_catcher()

    #Mid rise quantization process 4 bits resolution
    #Get quantization error
    quantization_values, indexes = quantization.mid_rise(quant_resolution)
    quantization_error = quantization.quantization_error()

    fig = plt.figure(figsize=(16, 5), dpi=150)

    ax1 = fig.add_subplot(311)
    ax1.plot(signal['x'], signal['y'], color='b')
    ax1.scatter(samples['x'], samples['y'], color='k')
    ax1.set_title("Signal and discrete samples")
    ax1.grid(True)
    y_min, y_max = np.min(signal['y']), np.max(signal['y'])
    y_range = y_max - y_min
    ax1.set_ylim(y_min - 0.1*y_range, y_max + 0.1*y_range)

    ax2 = fig.add_subplot(312)
    ax2.plot(quantization_values)
    ax2.set_title("Mid rise quantization")
    ax2.grid(True)
    y_min, y_max = np.min(quantization_values), np.max(quantization_values)
    y_range = y_max - y_min
    ax2.set_ylim(y_min - 0.1*y_range, y_max + 0.1*y_range)

    ax3 = fig.add_subplot(313)
    ax3.plot(quantization_error)
    ax3.set_title("Quantization Error")
    ax3.grid(True)
    y_min, y_max = np.min(quantization_error), np.max(quantization_error)
    y_range = y_max - y_min
    ax3.set_ylim(y_min - 0.1*y_range, y_max + 0.1*y_range)

    fig.tight_layout()

    filename = f'static/plots/quantization_result-{datetime.now()}.png'
    plt.savefig(filename)

    return filename, \
            quantization.quantization_levels, \
            quantization.delta, \
            quantization.samples, \
            indexes, \
            quantization.quantization_values, \
            quantization_error

        