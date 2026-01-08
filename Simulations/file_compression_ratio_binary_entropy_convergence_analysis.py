import numpy as np
import zstd
import matplotlib.pyplot as plt
p = np.arange(0.001,0.999,0.02)
def bernoullicompression(N,p):
    compression_ratio = np.zeros_like(p)
    for i in range(np.size(p)):
        randomstring = np.random.choice(['0','1'],size=N,p=[p[i],1-p[i]])
        rawfile = bytes(randomstring)
        compressedfile = zstd.compress(rawfile)
        compression_ratio[i] = len(compressedfile)/len(rawfile)
    return compression_ratio
compression_ratio = bernoullicompression(32,p)
plt.plot(p,compression_ratio/np.max(compression_ratio),marker='x',label='N=32')
compression_ratio = bernoullicompression(1024,p)
plt.plot(p,compression_ratio/np.max(compression_ratio),marker='+',label='N=1024')
compression_ratio = bernoullicompression(2**14,p)
plt.plot(p,compression_ratio/np.max(compression_ratio),marker='o',label='N=2**14')
plt.plot(p,-p*np.log2(p)-(1-p)*np.log2(1-p),label='Entropy')
plt.xlabel('p')
plt.ylabel('Compression␣ratio')
plt.legend()
plt.grid(True)
plt.show()
