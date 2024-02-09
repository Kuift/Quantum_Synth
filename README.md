# Quantum Signal processing for audio application

This project was developed during the in-person PennyLane Quantum Hackathon. Our aim is to demonstrate the capabilities of quantum signal processing by using audio as a medium, highlighting what might be possible with a quantum synthesizer. Therefore, you will find various experiments that may not necessarily provide a quantum advantage but instead offer intriguing audio effects intended to draw interest to the field.

## Running the project

The primary file to execute for this project is 'quantum_audio.ipynb'. Within this file, you will find all the audio experiments we have conducted. Accompanying each experiment is a descriptive comment that explains the effect produced. All the sound effects generated can be found in the 'audio' folder.

## Futur work

During this project, we tried to perform multiple quantum signal processing technique. However, some of them weren't interesting or would require too much work to implement during a short Hackathon.

### QRAM

In many of the papers related to audio that inspired this project, quantum random access memory (QRAM) has been discussed as a concept to build upon. Such QRAM could have a beneficial impact on various applications. A bucket-brigade QRAM was considered for conducting tests on its limitations and providing examples of how QRAM could be utilized in quantum signal processing. However, this concept would require further development, as there is currently no straightforward implementation of QRAM in PennyLane.

### Pitch modification

One of the first effects we explored was pitch modification. However, it appears that this type of operation requires additional effort, as it is not feasible to simply perform a Fourier transform and modify the frequency. Performing such an operation would likely involve quantum machine learning (QML) techniques.


## Sources

Itaboraí, P. V., & Miranda, E. R. (2023). Quantum Representations of Sound: from mechanical waves to quantum circuits. In E. R. Miranda (Ed.), Quantum Computer Music: Foundations, Methods and Advanced Concepts (pp. 223-274). [Springer]. https://link.springer.com/book/10.1007/978-3-031-13909-3

Laneve, L. (2023). Quantum Signal Processing, Phase Extraction, and Proportional Sampling. arXiv preprint arXiv:2303.11077. Retrieved from https://arxiv.org/abs/2303.11077

Yan, F., Guo, Y., Iliyasu, A. M., & Yang, H. (2017). Flexible Representation and Manipulation of Audio Signals on Quantum Computers. arXiv preprint arXiv:1701.01294. Retrieved from https://arxiv.org/abs/1701.01294