import LinkBudgetAnalyzer as lb
import numpy as np

freq = 915E6
txG  = 1
rxG  = 1
tempK = 290
lora = lb.Radio( freq, txG, rxG, tempK )
bw = 125E3

distances = np.linspace( 1, 9144 , 100)
bandwidths = np.linspace( 7.8E3, 500E3, 100 )

analyzer = lb.LinkBudgetAnalyzer( lora )
nrows = 2
ncols = 1
graph = lb.GraphicalLink( nrows, ncols, lora )

graph.plotRequiredPtx( distances, -95, 0)

graph.showPlots()
