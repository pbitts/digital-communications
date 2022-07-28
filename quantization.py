import numpy as np


class Quantization:

    def __init__(self, signal_x_values: list, signal_y_values: list, sample_catcher_frequency: float):
        '''Signal_x_values: Related to time vector, x axis values
        signal_y_values: the signal values itself, y axis
        sample_catcher_frequency: the frequency used to do the mapping of finite number of samples from 
                                the sample_y_values, also referred as number of samples'''
        self.signal_x_values = signal_x_values
        self.signal_y_values = signal_y_values
        self.sample_catcher_frequency = sample_catcher_frequency



    def sample_catcher(self) -> dict:
        '''Mapping a finite number of samples from the signal_y_values and their related
        point in time (stored under the time_hops variable)
        It returns a dict x: time hops related to the samples caught
                          y: the samples'''
        self.samples: list = []
        self.time_hops: list = []

        sample_catcher_period: float = 1/self.sample_catcher_frequency
        impulse: list = np.arange(self.sample_catcher_frequency)*sample_catcher_period
        for i in range(len(impulse)):
            for j in range(len(self.signal_x_values)):
                if round(impulse[i],5) == round(self.signal_x_values[j],5):
                    self.samples.append(round(self.signal_y_values[j],5))
                    self.time_hops.append(round(impulse[i],5))
        return {'y':self.samples, 'x':self.time_hops}


    def mid_rise (self, bits_resolution: int) -> list:
        '''Mid Rise Quantization (no levels on zero)
        receives the bits resolution and returns the quantized values'''
        print('Mid Rise Quantization')
        quantization_levels: int = 2**bits_resolution
        print("=============================")
        print('Levels:', quantization_levels)
        delta: float =  ( max(self.signal_y_values) - min(self.signal_y_values) ) / quantization_levels
        print('Delta:', delta)
        print("=============================")

        indexes: list = np.zeros(len(self.samples))
        index: int = 0
        self.quantization_values: list = np.zeros(len(self.samples))
        
        for i in range(len(self.samples)):
            index =  round (   (self.samples[i] - min(self.samples)  ) / delta    )   
            if index == quantization_levels:
                index = index -1
                indexes[i] = index 
            else:
                indexes[i] = index
            self.quantization_values[i] = min(self.signal_y_values) + (delta/2 + delta*index)
        return self.quantization_values


    def quantization_error(self) -> list:
        '''Returns the quantization error comparing the samples taken from the original
        signal minus the quantized values from the mid rise quantization process'''
        quantization_error: list = np.array(self.samples) - self.quantization_values
        return quantization_error

            