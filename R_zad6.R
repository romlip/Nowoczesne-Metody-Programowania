library(wbstats)
library(ggplot2)

pdf("populacja_swiata.pdf")
popwld <- wb(country="WLD", indicator="SP.POP.TOTL", startdate=1968, enddate=2018)
ggplot(data=popwld, aes(as.numeric(date),value/1e9)) +
  geom_point() +
  geom_line() +
  scale_x_continuous(name="Lata", limits=c(1968, 2018), breaks=seq(1968, 2018, 10)) +
  scale_y_continuous(name="Populacja, mld") +
  ggtitle("Populacja swiata w latach 1968-2018")
dev.off()

pdf("populacja_Polski.pdf")
poppl <- wb(country="PL", indicator="SP.POP.TOTL", startdate=1968, enddate=2018)
ggplot(data=poppl, aes(as.numeric(date),value/1e6)) +
  geom_point() +
  geom_line() +
  scale_x_continuous(name="Lata", limits=c(1968, 2018), breaks=seq(1968, 2018, 10)) +
  scale_y_continuous(name="Populacja, mln") +
  ggtitle("Populacja Polski w latach 1968-2018")
dev.off()
