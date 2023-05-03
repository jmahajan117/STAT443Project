winterdata = read.csv("/Users/andyb/Documents/STAT443Project/data/winterdata.csv")
#fit initial saturated linear regression model
full_model = lm(data = winterdata, Count ~ Hour + Temp + Humidity + Wind_speed + Visibility + Dew_Point + Solar_Radiation + Rainfall + Snowfall)
summary(full_model)
#Apply backwards stepwise regression
stepwise_model = lm(data = winterdata, Count ~ Hour + Humidity + Dew_Point + Rainfall + Snowfall + Holiday)
summary(stepwise_model)

#create plots
ggplot(data = winterdata, aes(x = Temp)) +
  geom_histogram(bins = 80, col = "black") + 
  labs(title="Distribution of Temperature", y="Count", x="Temperature (Degrees Celsius)")
ggplot(data = winterdata, aes(x = Humidity)) +
  geom_histogram(bins = 80, col = "black") + 
  labs(title="Distribution of Humidity", y="Count", x="Percentage Humidity")

#change date format
library(forecast)
library(lubridate)
bike = subset(winterdata, select = -c(Seasons, Functioning))
bike2 = bike[order(bike$Date, bike$Hour),]
bike2$Date <- as.Date(bike2$Date, format = "%d/%m/%Y", origin = "1/1/2018")
df <- bike2 %>% arrange(Date)

