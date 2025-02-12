import LinkBudgetAnalyzer as lba

radio = lba.Radio( 3960E6, 0, 0, 0, 0 )

analyzer = lba.LinkBudgetAnalyzer( radio )

for d in range( 10 ):
    Pl = analyzer.pathLoss( d + 1, 2.7 )
    print( Pl )

