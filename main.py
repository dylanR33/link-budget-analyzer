import LinkBudgetAnalyzer as lb
import numpy as np

freq = 2.4E9
bw   = 1E6
txG  = 10
rxG  = 10
tempK = 290
radio = lb.Radio( freq, bw, txG, rxG, tempK )

analyzer = lb.LinkBudgetAnalyzer( radio )

graph = lb.GraphicalLink( 2, 1, radio )

distances = np.linspace( 1, 100 , 100)
graph.plotRequiredPtx( distances, 10, 0 )
graph.plotReceivedP( distances, 10, 0 )
graph.plotPathLoss( distances, 0 )

bandwidths = np.linspace( 1E6, 3E6, 100 )
graph.plotNoisePower( bandwidths, 1 )

graph.showPlots()
