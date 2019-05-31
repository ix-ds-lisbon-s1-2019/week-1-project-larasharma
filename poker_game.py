
import random

cards = [2,3,4,5,6,7,8,9,10,11,12,13,14,
         2,3,4,5,6,7,8,9,10,11,12,13,14,
         2,3,4,5,6,7,8,9,10,11,12,13,14,
         2,3,4,5,6,7,8,9,10,11,12,13,14,]

###########################################################################################################

num_play = input( "Numerical number of players: ")
num_play = int(num_play)

names = []

for number in range( 0, num_play ):
    reply = input("Name: ")
    names.append(reply)

###########################################################################################################

picks = []

random.shuffle( cards )

for person in names:
    hand = cards[0:5]
    picks.append(hand)
    del cards[0:5]

dictionary = dict(zip(names, picks))

###########################################################################################################

winner = []

for indexes in range(0, len(dictionary) ):
    index_a = 0
    index_b = index_a + 1

    for i in dictionary:
        a = list(dictionary.values())
        a = a[index_a]

        b = list(dictionary.values())
        b = b[index_b]

        if max(a) > max (b):                                            #winner is person a

            y = list( dictionary.keys() )
            y = y[ index_a ]

            win = y

            if len( dictionary ) > 2:
                index_b = index_b + 1
            else:
                index_b = index_b

        elif max(a) < max(b):                                          #winner is person b

            x = list( dictionary.keys() )
            x = x[ index_b ]

            win = x
            index_a = index_b

            if len( dictionary ) > 2:
                index_a = index_b + 1
            else:
                index_a = index_b


        elif max(a) == max(b) :                                         #it's a tie

            r = a.copy()
            s = b.copy()

            while ( max(r) == max(s) ):                                #remove duplicates from the list then analyze it
                m = r.index( max(r) )
                n = s.index( max(r) )

                r.pop(m)
                s.pop(n)

                if len(r) == 1 and len(s) == 1:
                    break

            if max(r) > max (s):

                y = list( dictionary.keys() )
                y = y[ index_a ]

                win = y

                if len( dictionary ) > 2:
                    index_b = index_b + 1
                else:
                    index_b = index_b

            elif max(r) < max(s):

                x = list( dictionary.keys() )
                x = x[ index_b ]

                win = x
                index_a = index_b

            elif r == s:
                y = list( dictionary.keys() )
                y = y[ index_a ]

                x = list( dictionary.keys() )
                x = x[ index_b ]

                win = '{} and {}'.format(x, y)


winner.append(win)

###########################################################################################################

winning_player = ''.join(winner)


print( "The following hands are: ", dictionary )

print()

print(winning_player ,"wins." )

###########################################################################################################
