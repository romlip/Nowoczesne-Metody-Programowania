old.par <- par(mfrow=c(2,2))

#########################################################
# Efekt Kerra
# 
# Ÿród³o: https://www.sciencedirect.com/topics/physics-and-astronomy/kerr-effect
# dane zosta³y sczytane z rysunku 5.3 przy pomocy Czytacza Wykresów (zad. 5 z Narzêdzi Programistycznych)
#########################################################

x_kerr <- c(40.54, 79.05,119.6, 156.1, 196.6, 243.2, 271.6, 310.1, 346.6, 387.2)
y_kerr <- c(0.02828, 0.07407, 0.1212, 0.1306, 0.1468, 0.1630, 0.1643, 0.1603, 0.1616, 0.1643)
plot(x_kerr,y_kerr, main = "Efekt Kerra", xlab = "Gruboœæ warstwy (Co11/Cu31)n na Cu(111) [A]", ylab="Eliptycznoœæ [mrad]")

model_kerr <- nls(y_kerr ~ a*exp(b*x_kerr) +c, start = list(a = -0.2, b = -0.001, c = 0.2))
new.data <- data.frame(x_kerr = seq(min(x_kerr),max(x_kerr),len = 100))
lines(new.data$x,predict(model_kerr,newdata = new.data))

cat(
    "Efekt Kerra:\n",
    "Równanie: ", as.character(formula(model_kerr)), "\n",
    "Wspó³czynniki:", 
    "\n\ta: ", coefficients(model_kerr)[1],
    "\n\tb: ", coefficients(model_kerr)[2],
    "\n\tc: ", coefficients(model_kerr)[3])

################################
# Miêdzynarodowa krzywa czu³oœci oka
# 
# Ÿród³o: Optoelektronika, Bernard Ziêtek, Uniwersytet Miko³aja Kopernika, Toruñ 2005, str. 598
################################

dlugosc_fali <- seq(380, 820, 20)
czulosc_oka <- c(2e-4, 2.8e-3, 1.75e-2, 3.79e-2, 6.e-2, 1.3902e-1,3.23e-1, 7.1e-1, 9.54e-1, 9.95e-1,8.7e-1, 6.5e-1, 3.81e-1, 1.75e-1,6.1e-2, 1.7e-2, 4.102e-3, 1.047e-3, 2.492e-4, 6.0e-5, 1.4989e-5, 3.7028e-6, 9.1029e-7)
plot(dlugosc_fali, czulosc_oka, main = "Miêdzynarodowa krzywa czu³oœci oka", xlab = "D³ugoœæ fali œwiat³a [nm]", ylab="Czu³oœæ V")

model_oko <- nls(czulosc_oka ~ exp(-((dlugosc_fali-u)^2)/sigma), start = list(u = 570, sigma = 100))
new.data <- data.frame(dlugosc_fali = seq(min(dlugosc_fali),max(dlugosc_fali),len = 100))
lines(new.data$dlugosc_fali,predict(model_oko,newdata = new.data))

cat("\n\n#####################################\n")
cat(
  "\nKrzywa czu³oœci oka:\n",
  "Równanie: ", as.character(formula(model_oko)), "\n",
  "Wspó³czynniki:", 
  "\n\tu: ", coefficients(model_oko)[1],
  "\n\tsigma: ", coefficients(model_oko)[2])

################################
# Wspó³czynnik strat mocy wi¹zki laserowej dla ró¿nego stopnia obciêcia
# 
# Ÿród³o: Optyka Laserów, Romuald JóŸwicki, Wydawnictwo Naukowo-Techniczne, Warszawa 1981, Tablica 5.2, str. 165
# trochê oszukane, bo podane w ksi¹¿ce wartoœci s¹ wartoœciami teoretycznymi wynikaj¹cymi ze wzoru w³aœnie, przy
# czym w wartoœciach ksi¹¿kowych dla S wkrad³a siê chyba literówka - powinno byæ 1.1 zamiast 11.1
################################

beta <- c(2.5, 2.0, 1.5, 1.0, 0.75, 0.5, 0.25)
S <- c(4e-4, 0.034, 11.1, 13.5, 32.5, 60.7, 88.3) # dane w procentach
plot(beta,S, main = "Straty mocy wi¹zki laserowej", xlab = "Stopieñ obciêcia wi¹zki dla ró¿nego stopnia obciêcia", ylab="Straty mocy [%]")

model_strat <- nls(S ~ 100 * exp(a*beta^2), start = list( a =-1))
new.data <- data.frame(beta = seq(min(beta),max(beta),len = 100))
lines(new.data$beta,predict(model_strat,newdata = new.data))

cat("\n\n#####################################\n")
cat(
  "\nStraty wi¹zki:\n",
  "Równanie: ", as.character(formula(model_strat)), "\n",
  "Wspó³czynnik:", 
  "\n\ta: ", coefficients(model_strat)[1])


################################
#===============================
################################
# beta <- c(1.9, 2.1, 2.3, 2.5, 2.8, 3.1, 3.6, 4.2, 5.0)
# S <- c(6.5, 6.81, 7.14, 7.50, 7.76, 8.0, 8.35, 8.85, 9.5)
# plot(beta,S)
# 
# model_strat <- nls(S ~ a* exp(b*beta) + c, start = list(a=-1, b = -0.2, c = 0.2))
# new.data <- data.frame(beta = seq(min(beta),max(beta),len = 100))
# lines(new.data$beta,predict(model_strat,newdata = new.data))
#################################

par(old.par)