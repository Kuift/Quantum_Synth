# Quantum Signal processing for audio application

This project was developed during the in-person PennyLane Quantum Hackathon. Our aim is to demonstrate the capabilities of quantum signal processing by using audio as a medium, highlighting what might be possible with a quantum synthesizer as a bonus. Therefore, you will find various experiments that may not necessarily provide a quantum advantage but instead offer intriguing audio effects intended to draw interest to the field. The field of Quantum Signal Processing (QSP) lags behind quantum image processing[1] since one-dimensional data structures garner less attention in quantum computing. However, advancing the development of QSP could aid in creating better algorithms and enhance our understanding of how quantum computing can process data. 

## Running the project

The primary file to execute for this project is 'quantum_audio.ipynb'. Within this file, you will find all the audio experiments we have conducted. Accompanying each experiment is a descriptive comment that explains the effect produced. All the sound effects generated can be found in the 'audio' folder.

## Futur work

During this project, we tried to perform multiple quantum signal processing technique[2][3]. However, some of them weren't interesting or would require too much work to implement during a short Hackathon.

### QRAM

In many of the papers related to audio that inspired this project, quantum random access memory (QRAM)[4] has been discussed as a concept to build upon. Such QRAM could have a beneficial impact on various applications. A bucket-brigade QRAM was considered for conducting tests on its limitations and providing examples of how QRAM could be utilized in quantum signal processing. However, this concept would require further development, as there is currently no straightforward implementation of QRAM in PennyLane.

### Pitch modification

One of the first effects we explored was pitch modification. However, it appears that this type of operation requires additional effort, as it is not obviously feasible to simply perform a Fourier transform and modify the frequency. Performing such an operation would likely involve quantum machine learning (QML) techniques.


## Sources

[1] Itaboraí, P. V., & Miranda, E. R. (2023). Quantum Representations of Sound: from mechanical waves to quantum circuits. In E. R. Miranda (Ed.), Quantum Computer Music: Foundations, Methods and Advanced Concepts (pp. 223-274). [Springer]. https://link.springer.com/book/10.1007/978-3-031-13909-3

[2] Laneve, L. (2023). Quantum Signal Processing, Phase Extraction, and Proportional Sampling. arXiv preprint arXiv:2303.11077. Retrieved from https://arxiv.org/abs/2303.11077

[3] Yan, F., Guo, Y., Iliyasu, A. M., & Yang, H. (2017). Flexible Representation and Manipulation of Audio Signals on Quantum Computers. arXiv preprint arXiv:1701.01294. Retrieved from https://arxiv.org/abs/1701.01294

[4] Casares, P. A. M. (2020). Circuit implementation of bucket brigade qRAM for quantum state preparation. arXiv preprint arXiv:2006.11761. Retrieved from https://arxiv.org/abs/2006.11761