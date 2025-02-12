import math

class LinkBudgetAnalyzer:

    def __init__( self, radio ):
        self.radio = radio

    def waveLen( self ):
        return self._c / self.radio.frequency

    def pathLoss( self, d, n ):
        return 10 * math.log10( ( 16 * ( math.pi**2 ) * ( d**n ) ) / ( self.waveLen()**2 ) )

    def cnr( self ):
        return 0

    def sensitivity( self ):
        return 0

    def nf( self ):
        return 0

    def requiredPtx( self, Ps, d, n ):
        return -self.radio.txGain - self.radio.rxGain + self.pathLoss( d, n ) + Ps

    _k = 1.38E-23   # Boltzmans const
    _c = 2.99E8     # Speed of light


class Radio:
    def __init__( self, frequency, bandwidth, txGain, rxGain, tempK ):
        self.frequency = frequency
        self.bandwidth = bandwidth
        self.txGain    = txGain
        self.rxGain    = rxGain
        self.tempK     = tempK
