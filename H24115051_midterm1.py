i = 9 # we set 9 to start define as the number
while i>6: # we use "while" to show that i should be > 6 so that i could not be smaller than 6
    a = i
    b = i- 3 # we set b = i-3 because we want 9  x 6
    c = i - 6 # we set this line because we want 9 x 3
    d = 9 # this is for the number  9 8 7 6 5 4 3 2 1
    while d>0: # we use while because we dont want d <0 so we use while d>0 we set this number for the ones being multiplied 9 8 7 6 5 4 3 2 1
        print('%d x %d = %d' % (d, a, a*d), end='\t') # for printing the lines we use \t for tabbing after this line is executed
        print('%d x %d = %d' % (d, b, b*d), end='\t') # for printing the lines we use \t for tabbing after this line is executed
        print('%d x %d = %d' % (d, c, c * d), end='\t')# for printing the lines we use \t for tabbing after this line is executed
        print()
        d -=1
    i-=1



