single_sample_size <- 100000
coupons <- 60

dat <- numeric(single_sample_size * coupons)
for (i in 0:(coupons-1)) {
    df <- data.frame(rgeom(single_sample_size, (coupons-i)/coupons))
    df <- df + 1
    dat[((i*single_sample_size)+1):((i+1)*single_sample_size)] <- df$rgeom.single_sample_size...coupons...i..coupons.
}

groupnum <- rep(1:coupons, each = single_sample_size)

df <- data.frame(matrix(dat, ncol = length(unique(groupnum))))
colnames(df) <- unique(groupnum)
rownames(df) <- 1:single_sample_size
df$sum <- rowSums(df)

#print(head(df_new))
data = df[,'sum']
hist(data, breaks = coupons, xlab = 'Total Tries', ylab = 'Frequency',
     main = paste("Tries to get" , coupons, "Coupons"), xlim = c(0,range(data)[2]))
print(summary(data))
print(sum((function (x) 1/x) (1:coupons))*coupons)