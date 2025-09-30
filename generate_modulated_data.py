import numpy as np
from gnuradio import gr, blocks, analog, digital

class ModulationDataGenerator(gr.top_block):
    def __init__(self, mod_type='qpsk', samp_rate=1e6, snr_db=20, num_samples=100000):
        gr.top_block.__init__(self)
        self.samp_rate = samp_rate
        self.num_samples = int(num_samples)
        self.snr_db = snr_db

        # Choose modulation
        if mod_type == 'bpsk':
            self.mod = digital.constellation_bpsk().base()
        elif mod_type == 'qpsk':
            self.mod = digital.constellation_qpsk().base()
        elif mod_type == 'qam16':
            self.mod = digital.constellation_16qam().base()
        elif mod_type == 'qam64':
            self.mod = digital.constellation_64qam().base()
        else:
            raise ValueError("Unknown modulation type")

        # Random symbols
        self.src = blocks.vector_source_b(
            np.random.randint(0, self.mod.arity(), self.num_samples).tolist(), False
        )
        self.modulator = digital.chunks_to_symbols_bc(self.mod.points())
        self.sink = blocks.vector_sink_c()

        # Add AWGN noise
        self.noise = analog.noise_source_c(analog.GR_GAUSSIAN, 10 ** (-snr_db / 20), 0)
        self.add = blocks.add_cc()

        self.connect(self.src, self.modulator)
        self.connect(self.modulator, (self.add, 0))
        self.connect(self.noise, (self.add, 1))
        self.connect(self.add, self.sink)

    def get_data(self):
        return np.array(self.sink.data())

# Usage example
if __name__ == "__main__":
    gen = ModulationDataGenerator(mod_type='qpsk', snr_db=10)
    gen.run()
    data = gen.get_data()
    np.save('qpsk_snr10.npy', data)
