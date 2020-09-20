# Matryca wykresów rozproszenia dla wybranych parametrów ksiê¿yców Jowisza:
# promieñ, pó³oœ wielka, albedo, inklinacja
# 
# Ÿród³o: https://nssdc.gsfc.nasa.gov/planetary/factsheet/joviansatfact.html
# Niestety widoczne znaczne ró¿nice wartoœci pomiêdzy 4-ema najwiêkszymi ksiê¿ycami, tzw. galileuszowymi, a pozosta³ymi
# w zwi¹zku z czym korelacje na wspólnym wykresie s¹ Ÿle widoczne

dane <- read.table("jovian_satellites3.txt", header=TRUE, colClasses=c("factor", "character", rep("numeric", 4)))
typ_ksiezyca <- c("red", "blue")
plot(dane[,3:6],  pch = 1, cex = 1, col=typ_ksiezyca[dane$type], upper.panel=NULL, main="Ksiê¿yce Jowisza")
legend("topright", title= "Legenda", legend=c("Ksiê¿yce Galileuszowe", "Mniejsze ksiê¿yce"), pch = 1, col=typ_ksiezyca, cex=1, inset = .2)