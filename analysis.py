from datetime import datetime
import matplotlib.pyplot as plt

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
    quantization_values = quantization.mid_rise(quant_resolution)
    quantization_error = quantization.quantization_error()

    fig = plt.figure(figsize=(16, 9), dpi=150)

    ax1 = fig.add_subplot(311)
    ax1.plot(signal['x'], signal['y'], color='b')
    ax1.scatter(samples['x'], samples['y'], color='k')
    ax1.set_title("Signal and discrete samples")

    ax2 = fig.add_subplot(312)
    ax2.plot(quantization_values)
    ax2.set_title("Mid rise quantization")


    ax3 = fig.add_subplot(313)
    ax3.plot(quantization_error)
    ax3.set_title("Quantization Error")

    fig.tight_layout()

    # Generate and save plot
    current_datetime = datetime.now()
    filename = f'static/plots/quantization_result_{current_datetime}.png'
    plt.savefig(filename)

    return filename, quantization.quantization_levels, quantization.delta

        