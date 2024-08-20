# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

#give background information to viewers
print("Senegal is the western most country in the Africa continent. Its national language is French. It is also known as the 'Gateway To Africa'. \n")
print("Women make up half of the population, so you would expect them to make up half of the workforce...right?\n")
print("That unfortunately is not the case in the Senegal. But at least all employed women are paid...?\n\nYou might be surprised to know that not all employed women get paid.")
input("\nPress enter/return to continue\n")
print("While exploring the Women's Well-being dataset, I found that from 1995 to 2005 there was a consistent percent of employed women earning money. That percentage rose steadily from 2006 to 2012. Then after the percent of paid working women has flcutauted anywhere from 12.5% to 14%\n")
print("Based on these findings, my proposed research question is:\nWhy are very few women employed and paid in Senegal? What can be done to give women money for the work they provide?")



# Print out the number of rows and columns
# print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

oneCountryBooleanList = lwd["country_name"]=="Senegal"

oneCountryData = lwd.loc[oneCountryBooleanList]

# oneCountryBooleanList = lwd["country_name"]=="Senegal"
# oneCountryData = lwd.loc[oneCountryBooleanList]

# # Add Step 4 code here:
# plt.scatter(x="year",y="HD_women_size_mean",data=oneCountryData)

# create a scatter plot
# plt.scatter(lwd["year"],lwd["WK_working_paid_p"],color="red")
plt.scatter(x="year",y="HD_women_size_mean",data=oneCountryData,color="pink")

# add a title to the plot
plt.title("Women who were paid and employed for the past 12 months in Senegal(%)")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women who are working and are paid (%)")

# show the plot
plt.ylim(12,15)
plt.show()
