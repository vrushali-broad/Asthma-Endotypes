rm(list=ls())
library("Biobase")
library(limma)

## Load expression data
exprs <- read.table("transcriptomics.tsv",sep="\t",header=TRUE,stringsAsFactors=F,row.names=1,as.is=TRUE,check.names=FALSE)

## select genes of interest
goi = c('ANPEP','ARG1','ARG2','CCR1','CCR2','CCR3','CCR4','CCR6','CCR7','CCR8','CCR9','CCR10','CCRK','CCRL1','CCRL2','CCRN4L','CD4','CD8A','CD8B','CD19','CD22','CD33','CD44','CD81','CDH1','CEBPA','CLC','CR1','CSF1','CSF1R','CSF2','CSF2RB','CSF3','CSF3R','CXCL1','CXCL2','CXCL3','CXCL5','CXCL6','CXCL9','CXCL10','CXCL11','CXCL12','CXCL13','CXCL14','CXCL16','CXCL17','CXCR1','CXCR3','CXCR4','CXCR5','CXCR6','CXCR7','CYSLTR1','CYSLTR2','EBF1','EMR1','ENPP3','EPCAM','EPX','FCER1A','FCER1G','FCER2','FCGR3A','FCGR3B','FOXP3','FUT4','GATA1','GATA2','GATA3','GPR44','GZMA','GZMB','GZMH','GZMK','GZMM','HRH1','HRH2','HRH3','HRH4','IFNAR1','IFNAR2','IFNG','IFNGR1','IFNGR2','IKZF1','IL1A','IL1B','IL1F5','IL1F6','IL1F7','IL1F8','IL1F9','IL1F10','IL1R1','IL1R2','IL1RAP','IL1RAPL1','IL1RAPL2','IL1RL1','IL1RL2','IL1RN','IL2','IL2RA','IL2RB','IL2RG','IL3','IL3RA','IL4','IL4I1','IL4R','IL5','IL5RA','IL6','IL6R','IL6ST','IL7','IL7R','IL8','IL8RB','IL8RBP','IL9','IL9R','IL10','IL10RA','IL10RB','IL11','IL11RA','IL12A','IL12B','IL12RB1','IL12RB2','IL13','IL13RA1','IL13RA2','IL15','IL15RA','IL16','IL17A','IL17B','IL17C','IL17D','IL17F','IL17RA','IL17RB','IL17RC','IL17RD','IL17RE','IL17REL','IL18','IL18BP','IL18R1','IL18RAP','IL19','IL20','IL20RA','IL20RB','IL21','IL21R','IL22','IL22RA1','IL22RA2','IL23A','IL23R','IL24','IL25','IL26','IL27','IL27RA','IL28A','IL28B','IL28RA','IL29','IL31','IL31RA','IL32','IL33','IL34','IRF2','IRF3','IRF5','IRF8','ITGA2','ITGAM','KARS','KIT','LAMP1','LAMP3','LTA','LY6G6D','PAX5','PI4K2A','PRG2','RNASE2','RNASE3','RORA','RORC','RUNX1','RUNX1T1','RUNX2','RUNX3','SIGLEC8','STAT1','STAT2','STAT3','STAT4','STAT5A','STAT5B','STAT6','TBX21','TCF3','TFE3','TGFA','TGFB1','TGFB1I1','TGFB2','TGFB3','TGFBI','TGFBR1','TGFBR2','TGFBR3','TGFBRAP1','TNF')
exprs <- exprs[goi,]


exprs <- data.matrix(exprs)

## Load meta data
pData <- read.table("neu_meta.tsv",sep="\t",header=TRUE,stringsAsFactors=F,row.names=1,as.is=TRUE,check.names=FALSE)
intersec = intersect(row.names(pData),colnames(exprs))
exprs <- exprs[,intersec]
pData<-pData[intersec,]


phenoData <- new("AnnotatedDataFrame",data=pData)
all(rownames(pData)==colnames(exprs))

minimalSet <- ExpressionSet(assayData=exprs, phenoData=phenoData)


age <- phenoData$age
gender <- phenoData$gender

tmp <- phenoData$neu
grp_num <- 'Cluster 1' ## Change this per group

tmp[tmp==grp_num] <- 'Grp_asthma'
tmp[!tmp=='Grp_asthma'] <- 'Control'
groups <- tmp

## Declare design matrix
design <- model.matrix(~1+groups+gender+age)

## Fit model to data
fit <- lmFit(minimalSet, design)
fit <- eBayes(fit)

dt <- decideTests(fit)
summary(dt)
colnames(fit)

res <-topTable(fit, coef='groupsGrp_asthma', number=Inf, sort.by='p')

## Use this for Cluster 1
tmp1 <- head(res, 91)
fcvals_up <- tmp1[tmp1['logFC']>=0,]
order1 <- fcvals_up[order(-fcvals_up$logFC),]
write.table(fcvals_up, file="DE_Cluster1.txt", row.names = TRUE, col.names = TRUE, sep="\t")

## Use this for Cluster 2
tmp2 <- head(res, 62)
fcvals_up <- tmp2[tmp2['logFC']>=0,]
write.table(fcvals_up, file="DE_Cluster2.txt", row.names = TRUE, col.names = TRUE, sep="\t")

## Use this for Cluster 3
tmp3 <- head(res, 100)
fcvals_up <- tmp3[tmp3['logFC']>=0,]
write.table(fcvals_up, file="DE_Cluster3.txt", row.names = TRUE, col.names = TRUE, sep="\t")

