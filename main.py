import LinkBudgetAnalyzer as lb

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
