#The program calculates and output how many players from the given list are in the range of one standard deviation from the mean.
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean = sum(players)/len(players)
stdvar = (sum((v-mean)**2 for v in players)/len(players))**0.5
l,h = mean-stdvar,mean+stdvar
range = len([v for v in players if l < v < h])
print(range)
