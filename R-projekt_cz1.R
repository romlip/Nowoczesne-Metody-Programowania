library(gsloid)
library(ggplot2)
names(lisiecki2005)
head(lisiecki2005)

#####################################################################################
# Ramka danych zawiera poziomy stosunku izotopów tlenu O18 i O16 w okresie pliocen-plejstocen.
# Ze strefy bentalnej wód pobiera siê "stack" osadów i mierzy poziomy izotopów w ka¿dej z warstw.
# Na poziomy wp³ywa bezpoœrednio iloœæ opadów atmosferycznych w danym okresie, a te z kolei zale¿¹ od temperatury.
# Jest to wiêc poœrednia metoda pomiaru temperatury Ziemi. (tak to rozumiem)

pdf("cz1_d18O.pdf")
ggplot(data=lisiecki2005, aes(Time,d18O)) +
  #geom_point() +
  geom_line() +
  scale_x_continuous(name="Lata w tys.", limits=c(0, max(lisiecki2005$Time))) +
  scale_y_reverse(name=bquote(delta^18*O)) +
  ggtitle("Globalne poziomy d18O w pliocenie i plejstocenie") +
  theme_bw()
dev.off()