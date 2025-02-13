import LinkBudgetAnalyzer as lb
import numpy as np

freq = 2.4E9
bw   = 1E6
txG  = 10
rxG  = 10
radio = lb.Radio( freq, bw, txG, rxG )
analyzer = lb.LinkBudgetAnalyzer( radio )

print( analyzer.pathLoss( 20E3 ) )
print( f"Received signal power: {analyzer.receivedP( 20E3, 30 )}" )
print( f"Necessary TX power: {analyzer.requiredPtx( 20E3, -90 )}" )

print( analyzer.noisePower( 290 ) )

print( analyzer.maxBitRate( 30 ) )

graph = lb.GraphicalLink( 2, 1, radio )
distances = np.linspace( 1, 100 , 100)

graph.plotPathLoss( distances, 1 )
graph.radio.frequency = 915E6
graph.plotPathLoss( distances, 1 )

graph.showPlots()
