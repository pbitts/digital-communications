import numpy as np


class Wave:   
        
    def sine (self, bits: int, frequency: float, amplitude: float, \
        dc: float) -> dict:
        '''Sine wave = Amplitude*sin(2*pi*frequency*x) + dc
        returns a dict containing x (time) and y (sine) values'''
        interval = 1/bits
        time = np.arange(bits)*interval
        sine = amplitude*np.sin(2*np.pi*frequency*time) + dc
        return {'x':time, 'y':sine}

    def cosine (self, bits: int, frequency: float, amplitude: float, \
        dc: float) -> dict:
        '''Cosine wave = Amplitude*sin(2*pi*frequency*x) + dc
        returns a dict containing x (time) and y (cosine) values'''
        interval = 1/bits
        time = np.arange(bits)*interval
        sine = amplitude*np.cos(2*np.pi*frequency*time) + dc
        return {'x':time, 'y':sine}

    def sine_plus_cosine (self, bits: int, sine_frequency: float, sine_amplitude: float, \
        sine_dc: float, cosine_frequency: float, cosine_amplitude: float, cosine_dc: float) -> dict:
        '''Sine + Cosine wave = Amplitude*sin(2*pi*frequency*x) + dc + Amplitude*cosine(2*pi*frequency*x) + dc
        returns a dict containing x (time) and y (sine + cosine) values'''
        sine_wave = self.sine(bits, sine_frequency, sine_amplitude, sine_dc)
        cosine_wave = self.cosine(bits, cosine_frequency, cosine_amplitude, cosine_dc)
        return {'x': sine_wave['x'], 'y': sine_wave['y']+cosine_wave['y']}

    def sine_times_cosine (self, bits: int, sine_frequency: float, sine_amplitude: float, \
        sine_dc: float, cosine_frequency: float, cosine_amplitude: float, cosine_dc: float) -> dict:
        '''Sine * Cosine wave = [Amplitude*sin(2*pi*frequency*x) + dc] * [Amplitude*cosine(2*pi*frequency*x) + dc]
        returns a dict containing x (time) and y (sine * cosine) values'''
        sine_wave = self.sine(bits, sine_frequency, sine_amplitude, sine_dc)
        cosine_wave = self.cosine(bits, cosine_frequency, cosine_amplitude, cosine_dc)
        return {'x': sine_wave['x'], 'y': sine_wave['y']*cosine_wave['y']}


    @staticmethod
    def interpolation( signal_y_values, signal_x_values):   #TO DO
        '''Ideal Interpolation to recover the signal using sinc functions.'''
        pass
            