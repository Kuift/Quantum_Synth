import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

def plot_frequency_content(filename):
    # Read the WAV file
    sample_rate, data = scipy.io.wavfile.read(filename)
    print(sample_rate)
    # If stereo, convert to mono by averaging the two channels
    if len(data.shape) == 2:
        data = data.mean(axis=1)
    
    # Perform the Fourier Transform to get frequency content
    # Use np.fft.rfft to handle real inputs and improve efficiency
    freq_data = np.fft.rfft(data)
    
    # Get the power spectrum (magnitude of the Fourier coefficients)
    power_spectrum = np.abs(freq_data)
    
    # Generate frequency axis (only for positive frequencies)
    freqs = np.fft.rfftfreq(len(data), d=1/sample_rate)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(freqs, power_spectrum)
    plt.title(f'Frequency Content of {filename}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.yscale('log')  # Set the y-axis to a logarithmic scale
    plt.xlim(0, sample_rate / 2)  # Nyquist limit
    plt.grid(True)
    plt.show()


import glob

# Pattern to match all files starting with 'sine_wave'
pattern = 'mega*'

# Use glob to find all matching filenames
matching_files = glob.glob(pattern)

print("Files starting with 'sine_wave':")
filenames = [filename for filename in matching_files]
# Example usage
# Replace with your actual file names
for filename in filenames:
    plot_frequency_content(filename)
