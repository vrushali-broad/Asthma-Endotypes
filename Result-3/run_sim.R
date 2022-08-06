library(BoolNet)
setwd("/Users/vrushali/Documents/BoolNet/data/Paper1/Final\ Results/Paper_Code/Code/RUDRA/Result3")

print('RUles1')
network = loadNetwork('rules1.txt')
series = generateTimeSeries(network,350,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/overlap1.txt", sep="\t")

print('RUles2')
network = loadNetwork('rules2.txt')
series = generateTimeSeries(network,350,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/overlap2.txt", sep="\t")

print('RUles3')
network = loadNetwork('rules3.txt')
series = generateTimeSeries(network,350,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/overlap3.txt", sep="\t")
