import wave
# import pyaudio
import numpy as np
import pylab as plt


class MyWav:
    def __init__(self, audioName):
        self.wf = wave.open(audioName, "r")
        buffer = self.wf.readframes(self.wf.getnframes())
        self.data = plt.frombuffer(buffer, dtype="int16")
        self.Y = None
        self.freqs = None
        self.bins = None

        print ("MyWav_init")

    def printWaveInfo(self):
        print "num:", self.wf.getnchannels()
        print "fu:", self.wf.getsampwidth()
        print "zhouboshu:", self.wf.getframerate()
        print "shu:", self.wf.getnframes()
        print "param:", self.wf.getparams()
        print "seconds:", float(self.wf.getnframes()) / self.wf.getframerate()

    def getDataLength(self):
        print "dataLength", len(self.data)

    def printAllPlot(self):
        # print len(self.data)
        plt.plot(self.data[:])
        plt.show()

    def printPlot(self, start, end):
        # print len(self.data)
        plt.plot(self.data[start: end])
        plt.grid()
        plt.show()

    def plotSpecgram(self):
        N = 512
        hamming = np.hamming(N)


        plt.figure(1)
        plt.suptitle('Spectrogram')
        plt.xlabel('time [sec]')
        plt.ylabel('freqency [Hz]')


        self.Y, self.freqs, self.bins, im = plt.specgram(self.data, NFFT=N, Fs=self.wf.getframerate(),
                                                         noverlap=0, window=hamming)
        plt.savefig('../picDatas/specgram.png', format='png')

    def showPlot(self):
        plt.show()


if __name__ == '__main__':
    mywav = MyWav("1.wav")
    mywav.printWaveInfo()
    # mywav.printAllPlot()
    mywav.printPlot(0, 500)
    mywav.getDataLength()
    mywav.plotSpecgram()
    mywav.showPlot()
