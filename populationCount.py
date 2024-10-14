#In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage of literate men is 35 of the    total population, write a program to find the total number of illiterate men and women if the population of the town is 80,000
totalPopulation = 80000
print("Total population : " + str(totalPopulation))

percentMen = 52
print("Total percent men : " + str(percentMen))

totalMen = percentMen * totalPopulation / 100
print("Total men : " + str(totalMen))

totalWomen = totalPopulation - totalMen
print("Total women : " + str(totalWomen))

percentTotalLiteracy = 48
print("Total percent literacy : " + str(percentTotalLiteracy))

totalLiteracy = percentTotalLiteracy * totalPopulation / 100
print("Total literate population : " + str(totalLiteracy))

percentTotalLiterateMen = 35
print("Total percent literate men : " + str(percentTotalLiterateMen))

totalLiterateMen = percentTotalLiterateMen * totalPopulation / 100
print("Total literate men : " + str(totalLiterateMen))

totalLiterateWomen = totalLiteracy - totalLiterateMen
print("Total literate women : " + str(totalLiterateWomen))

totalIlliterateMen = totalMen - totalLiterateMen
print("Total illiterate men : " + str(totalIlliterateMen))

totalIlliterateWomen = totalWomen - totalLiterateWomen
print("Total illiterate women : " + str(totalIlliterateWomen))
