library(BoolNet)
setwd("Result1-2")

##############################################################
############ Run Simulation (Basal State) ####################
##############################################################
network = loadNetwork('input_rules/1.basal_rules.txt')
series = generateTimeSeries(network,350,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/basal.txt", sep="\t")

#########################################################################
##################### Run Simulation  ###################################
## Change input stimulants to generate Table S2 
## Stimulant_I ---> Stimulant TH2 (assign 0, tmp (0.5), 1)
## Stimulant_II --->  Stimulant TH17 (assign 0, tmp (0.5), 1)
## Stilumant_III --->  Stimulant TH1 (assign 0, tmp (0.5), 1)
## Run following commands for each combination of input stimulants
#########################################################################
network = loadNetwork('input_rules/2.rules.txt')
series = generateTimeSeries(network,350,800,type = "asynchronous",noiseLevel = 0)
write.table(series, "Output/Minimal.txt", sep="\t")

#####################################################################
################ Supplementary Figure S4) ###########################
######## Find Attractors (only for toy example ######################
#####################################################################
network = loadNetwork('net_wo_motif.txt') 
attr <- getAttractors(network, method="random", startStates=100)
plotAttractors(attr)
