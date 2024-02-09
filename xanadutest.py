import pennylane as qml
import pennylane.numpy as np
import scipy.io.wavfile
import wave
import time


# Function to load a WAV file
def load_wav(filename):
    sample_rate, data = scipy.io.wavfile.read(filename)
    # If stereo, convert to mono by averaging the two channels
    if len(data.shape) == 2:
        data = data.mean(axis=1)
    return sample_rate, data

# Function to save a WAV file
def save_wav(filename, sample_rate, data):
    scipy.io.wavfile.write(filename, sample_rate, data)

# Function to convert audio samples to 8-bit
def convert_to_8bit(data):
    # Normalize data to the range of 8-bit audio [-128, 127]
    data = ((data - data.min()) / (data.max() - data.min()) * 255 - 128).astype(np.int8)
    return data

NB_QUBITS = 16
sample_rate = 44100  # Sample rate in Hz
duration = 0.2  # Duration in seconds
frequency = 440  # Frequency of the sine wave in Hz
amplitude = 2**(NB_QUBITS-1)/2-1 # Max amplitude for a N-bit audio file
dev = qml.device("default.qubit", wires=range(NB_QUBITS), shots=1)
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
samples = (amplitude * np.sin(2 * np.pi * frequency * t)).astype(np.int16)

filename = 'Megalovania Meme Sound Effect.wav'  # Specify your input file name here
sample_rate, original_data = load_wav(filename)

# Convert the original audio to 8-bit if it's not already
data_8bit = original_data#convert_to_8bit(original_data)

# Save the 8-bit version
save_wav(f'original_8bit_{filename}.wav', sample_rate, data_8bit)

samples = data_8bit
print("done converting wav data")

quantum_samples = []
low1 = -amplitude
low2 = 0
high1 = amplitude
high2 = 2*np.pi

def remapTo2Pi(value):
    return low2 + (value - low1) * (high2 - low2) / (high1 - low1)

@qml.qnode(dev)
def circuit1(global_iterator):
    for i in range(NB_QUBITS):
        #print(f"the lenght of global_iterator : {len(samples)}")
        if global_iterator < len(samples):
            #print(global_iterator)
            qml.RX(remapTo2Pi(samples[global_iterator]), i)
            #print(remapTo2Pi(samples[global_iterator]))
        else:
            print(f"uselesscalculations{i}")
    return [qml.sample(qml.PauliZ(i)) for i in range(NB_QUBITS)]#qml.probs(wires=range(NB_QUBITS))


for i in range(len(samples)):
    sample = circuit1(i)

    normal_list = [array.item() for array in sample]

    # Adjusting the list so that -1 becomes 0, and 1 remains 1
    adjusted_list = [0 if x == -1 else 1 for x in normal_list]

    binary_string = ''.join(map(str, adjusted_list))  # Convert the list to a string of binary digits
    binary_to_int = int(binary_string, 2)  # Convert binary string to integer

    quantum_samples.append(binary_to_int)
    if i % 1000 == 0:
        print(i)

# Create a WAV file
with wave.open(f'mega{time.time()}.wav', 'w') as wav_file:
    # Set the parameters: 1 channel, 2 bytes per sample, sample rate, number of frames, compression type, compression name
    wav_file.setparams((1, 2, sample_rate, len(samples), 'NONE', 'not compressed'))
    
    # Write the samples to the file
    quantum_samples_array = np.array(quantum_samples, dtype=np.int16)
    print(quantum_samples_array)
    wav_file.writeframes(np.array(quantum_samples_array).tobytes())

print("WAV file has been created.")