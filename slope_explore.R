powers = 1:15
base = 2
slopes = numeric(length(powers))
for (power in powers){
    x = base^power
    y = numeric(x)
    for (coupons in 1:x){
        y[coupons] = sum((function (x) 1/x) (1:coupons))*coupons
    }
    plot(y,1:x,col = "black",main = "Coupon Number and Expected # of Tries", pch = 20,
         abline(lm(1:x~y),col="red",lwd=2),cex = 0.1,xlab = "Expected # of Tries",ylab = "Number of Coupons")
    
    len <- 1:length(y)
    relation <- lm(y~len)
    slopes[power] = relation$coefficients[2]
    print(paste("Current Progress:",power,"/",length(powers)))
}

for (i in head(powers,-1)){
    print(slopes[i+1]-slopes[i])
}


coupons = 1:30000
#y is expected number of draws to complete collection of x coupons
y = numeric(length(coupons))
for (coupon in coupons){
    y[coupon] = sum((function (x) 1/x) (1:coupon))*coupon}
m <- lm(y ~ coupons * log(coupons) + coupons)
coefs = summary(m)$coefficients[1:4]
cc = coupons
predictions = coefs[1] + coefs[4]*cc *log(cc) + coefs[2]*cc
plot(coupons,predictions)
plot(coupons,y-predictions)
