## Methodology

### Dataset Generation

We generated synthetic datasets for BPSK, QPSK, 16-QAM, and 64-QAM modulations using GNU Radio 10.12.0 on Ubuntu 22.04. For each modulation type, random data symbols were mapped to constellation points and converted to complex I/Q samples. We varied the signal-to-noise ratio (SNR) across four levels (0, 10, 20, 30 dB) by injecting Gaussian noise.

All signal samples were stored as NumPy arrays (`.npy`), with each array containing 100,000 samples. The modulation type and SNR level are encoded in the filename for clarity.

### Signal Generation Flow

A Python script leveraging GNU Radio's digital modulation blocks was used for data generation. The script parameters include modulation type, sample rate, number of samples, and SNR. The flowgraph consists of a random symbol source, a modulation block, a noise generator, and a summing block to combine signal and noise.

### Quality Control

Generated signals were visualized using constellation plots and time-domain analysis to verify proper modulation and noise characteristics. Scripts and data are version-controlled and shared openly for reproducibility.

### Data Accessibility

All scripts and datasets are available via [GitHub/Zenodo link], ensuring reproducibility and accessibility for future research.
