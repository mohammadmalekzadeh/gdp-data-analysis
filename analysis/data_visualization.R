# install and active package
# install.packages("readxl")
library(readxl)

# read processed dataset
data <- read.csv("../dataset/gdp_processed_data.csv")

# Figure 1 — Distribution of Log GDP
hist(data[, 2], breaks = 30, probability = TRUE, col = "steelblue", border = "white",
     main = "Distribution of Log GDP", xlab = "Log GDP")
lines(density(data[, 2], na.rm = TRUE), lwd = 2)

# Figure 2 — Distribution of Log Population
hist(data[, 5], breaks = 30, probability = TRUE, col = "darkseagreen",
     border = "white", main = "Distribution of Log Population", xlab = "Log Population")
lines(density(data[, 5], na.rm = TRUE), lwd = 2)

# Figure 3 — Boxplot of GDP Growth
boxplot(data[, 4], col = "indianred", main = "Boxplot of GDP Growth Rates",
        ylab = "GDP Growth (%)", horizontal = TRUE)

# Figure 4 — Log GDP vs Log Population
plot(data[, 5], data[, 2], pch = 19, col = rgb(0.2, 0.4, 0.6, 0.6),
     xlab = "Log Population", ylab = "Log GDP", main = "Population vs GDP")
abline(lm(data[, 2] ~ data[, 5], data = data), lwd = 2)

# Figure 5 — GDP per Capita vs GDP Growth
plot(data[, 6], data[, 4], pch = 19, col = rgb(0.1, 0.5, 0.1, 0.6),
     xlab = "GDP per Capita (USD)", ylab = "GDP Growth (%)",
     main = "GDP per Capita vs Economic Growth")
abline(lm(data[, 4] ~ data[, 6], data = data), lwd = 2)

# Figure 6 — Log GDP vs Share of World GDP
plot(data[, 2], data[, 7], pch = 19, col = rgb(1, 0.6, 0.1, 0.6), xlab = "Log GDP",
     ylab = "Share of World GDP (%)", main = "GDP Size and Share of World GDP")

# Figure 7 — Top 10 Countries by GDP
top10 <- data[order(-data[, 2]), ][1:10, ]
barplot(top10[, 2], names.arg = top10[, 1], horiz = FALSE, las = 2, col = "steelblue",
        main = "Top 10 Countries by GDP", xlab = "Log GDP")

# Figure 8 - GDP Group Frequency
gdp_counts = table(data[, 3])
gdp_percent <- round(100 * gdp_counts / sum(gdp_counts), 1)
pie_labels <- paste0(names(gdp_counts), " (", gdp_percent, "%)")
colors <- c("Million"  = "#A6CEE3", "Billion"  = "#1F78B4", "Trillion" = "#B2DF8A")
pie(gdp_counts, labels = pie_labels, col = colors[names(gdp_counts)], border = "white",
    main = "Distribution of Countries by GDP Size Category")
