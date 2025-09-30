# modulation-dataset-gnuradio
# Modulated Signal Dataset

## Overview
This dataset contains I/Q samples generated for various digital modulation schemes (BPSK, QPSK, 16-QAM, 64-QAM) using GNU Radio 10.12.0 on Ubuntu 22.04. The data is intended for research in modulation classification and machine learning.

## Modulation Types
- BPSK
- QPSK
- 16-QAM
- 64-QAM

## Parameters
- Sample Rate: 1 MS/s
- SNR: 0, 10, 20, 30 dB
- Number of Samples: 100,000 per file

## File Format
- Each file: `.npy` (NumPy array of complex64 I/Q samples)
- File naming: `<modulation>_snr<snr>.npy` (e.g., qpsk_snr10.npy)

## Generation Method
Signals generated using GNU Radio Python scripts (`generate_modulated_data.py`).

## Usage Example
```python
import numpy as np
data = np.load('qpsk_snr10.npy')
```

## Citation
If using the dataset, please cite:
> [Your Paper Title], [Your Name], [Year], [Journal/Conference]

## License
[Specify license, e.g., MIT, CC-BY]
