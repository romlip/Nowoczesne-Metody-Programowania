liczba_przedzialow <- 5
x <- read.table("wyniki.txt", colClasses=c("NULL", NA))
x <- x[!is.na(x)]
pdf(paste("wykres_", liczba_przedzialow, "_przedzialow", ".pdf", sep=""))
h <- hist(x, col="red", axes=FALSE, xlab="", ylab="Ilosc zliczen", breaks=seq(min(x), max(x), (max(x)-min(x))/liczba_przedzialow), main=paste("wartosc srednia = ", format(mean(x), digits=4),"\n", "odchylenie standadowe = ", format(sd(x), digits = 3)))
axis(1, at=as.integer(seq(min(x), max(x), (max(x)-min(x))/liczba_przedzialow)))
axis(2)
cat("Zliczenia w kolejnych przedzialach:\n", h$counts, "\n")
dev.off()
