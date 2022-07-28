import matplotlib.pyplot as plt

from waveproducer import Wave
from quantization import Quantization



#Initiate class instance and produce a sine wave 
#1000 bits, 1Hz frequency, 10 Volts amplitude and 0 Volts DC
wave = Wave()
signal = wave.sine(1000,1,10,0)

#Initiate class instance and cacthe discrete samples 
#Impulse frequency 30Hz
quantization = Quantization(signal['x'], signal['y'], 100 )
samples = quantization.sample_catcher()

#Mid rise quantization process 4 bits resolution
#Get quantization error
quantization_values = quantization.mid_rise(4)
quantization_error = quantization.quantization_error()


#Plotting results
fig = plt.figure()

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

plt.show()
