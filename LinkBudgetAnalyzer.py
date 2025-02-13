import math
import matplotlib.pyplot as plt

class Radio:
    def __init__( self, frequency, bandwidth, txGain, rxGain ):
        self.frequency = frequency
        self.bandwidth = bandwidth
        self.txGain    = txGain
        self.rxGain    = rxGain



class LinkBudgetAnalyzer:

    # radio : radio object containing its unique attributes
    # n     : path loss exponent (2 for open space)
    def __init__( self, radio: Radio , n=2 ):
        self.radio = radio
        self.n     = n

    # Required TX power [dBm]
    #
    # d      : distance between receiver and transmitter
    # pRxMin : minimum allowable received signal power (receiver sensitivity)
    def requiredPtx( self, d, pRxMin ):
        return pRxMin - self.radio.txGain - self.radio.rxGain + self.pathLoss( d )
    
    # Received signal power [dBm]
    #
    # d   : distance between receiver and transmitter [m]
    # pTx : transmission power [dBm]
    def receivedP( self, d, pTx ):
        return pTx + self.radio.txGain + self.radio.rxGain - self.pathLoss( d )

    # Path loss [dB]
    #
    # d   : distance between receiver and transmitter [m]
    def pathLoss( self, d ):
        return 10 * self.n * math.log10( ( 4 * math.pi * d ) / self.waveLen() )

    # Wave length [m]
    def waveLen( self ):
        return self._c / self.radio.frequency

    # Noise power [dBm]
    #
    # tempK : ambient temperature [K]
    def noisePower( self, tempK ):
        pNoise = self._k * tempK * self.radio.bandwidth
        return 10 * math.log10( pNoise / self._mW )

    # Signal to noise ratio [dB]
    #
    # tempK     : ambient temperature [K]
    # receivedP : received signal power [dBm]
    def snr( self, tempK, receivedP ):
        return receivedP - self.noisePower( tempK )

    # Max bit rate (Shannon-Hartley Theorem)
    #
    # snr : signal to noise ratio [dB]
    def maxBitRate( self, snr ):
        linearSnr = 10**( snr / 10 )
        return int( self.radio.bandwidth * math.log( 1 + linearSnr, 2 ) )

    _k = 1.38E-23   # Boltzmans const
    _c = 2.99E8     # Speed of light
    _mW = 1E-3      # 1 milliwatt



class GraphicalLink( LinkBudgetAnalyzer ):
    def __init__( self, nrows, ncols, radio: Radio, n=2 ):
        super().__init__( radio, n )
        self.fig, self.axes = plt.subplots( nrows=nrows, ncols=ncols )

    def plotRequiredPtx( self ):
        return 0

    def plotReceivedP( self ):
        return 0

    def plotPathLoss( self, distances, axesNum ):
        pathLosses = []
        for d in distances:
            pathLosses.append( self.pathLoss( d ) )
        self.axes[ axesNum ].plot( distances, pathLosses )

    def plotNoisePower( self ):
        return 0

    def plotSNR( self ):
        return 0

    def plotMaxBitRate( self ):
        return 0

    def showPlots( self ):
        plt.tight_layout()
        plt.show()


