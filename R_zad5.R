pt1 <- PeriodicTable:::periodicTable
pt1 <- na.omit(pt1[,c("numb","name","symb","isotopes")])
pt1 <- pt1[order(pt1[,"isotopes"], decreasing=FALSE),]
write.table(pt1, "pt1.txt")

pt2 <- PeriodicTable:::periodicTable
pt2 <- na.omit(pt2[,c("numb","name","symb","isotopes","type","density")])
pt2 <- pt2[order(pt2[,"density"], decreasing=TRUE),]
write.table(pt2, "pt2.txt")