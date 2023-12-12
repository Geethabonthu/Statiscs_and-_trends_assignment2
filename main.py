"""
@author: Geetha
"""

"""Importing libraries"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
from scipy.stats import kurtosis

def transposingData(file_path):
    """
        Transpose the 'Country Name' and 'Time' columns in a DataFrame.

        Parameters:
        - file_path (str): The path to the CSV file containing the data.

        Returns:
        - tuple: A tuple containing two DataFrames - the original DataFrame and
        the transposed DataFrame.
    """
    df = pd.read_csv(file_path)
    df_org = df.copy()
    df[['Country Name' , 'Time']] = df[['Time' , 'Country Name']]
    df_transposed = df.rename(columns = {'Country Name': 'Time' ,
                                         'Time': 'Country Name'})
    return df_org , df_transposed


def plot_histogram(data , skew_column_name , skewness):
    """
        Plot a histogram of a specified column in a DataFrame.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing the data to be plotted.
        - skew_column_name (str): The name of the column for which the
        histogram will be plotted.
        - skewness (float): The skewness value of the specified column.

        Returns:
        - None: The function displays the histogram using Matplotlib but
        does not return any value.
    """
    plt.figure(figsize = (8 , 6))
    plt.hist(data[skew_column_name].dropna() , bins = 30 , color = 'blue' ,
             edgecolor = 'black' , alpha = 0.7)
    plt.title(f'Histogram of {skew_column_name} with Skewness {skewness:.2f}')
    plt.xlabel(skew_column_name)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


def piePlot(sizes , labels , title):
    """
        Plot a pie chart using specified sizes and labels.

        Parameters:
        - sizes (list or array-like): The sizes of the sectors in the pie chart.
        - labels (list of str): The labels for each sector in the pie chart.
        - title (str): The title of the pie chart.

        Returns:
        - None: The function displays the pie chart using Matplotlib but does
         not return any value.
    """

    plt.pie(sizes , labels = labels , autopct = '%1.1f%%' , startangle = 90)
    plt.title(title , fontsize = 20)
    # Show the plot
    plt.show()


def barPlot(barposition1 , barposition2 , data1 , data2 , bar_width ,
            title , label1 , label2):
    """
        Plot a grouped bar chart with two sets of data.

        Parameters:
        - barposition1 (array-like): The x-coordinates of the bars for
        the first set of data.
        - barposition2 (array-like): The x-coordinates of the bars for
        the second set of data.
        - data1 (array-like): The y-values for the first set of data.
        - data2 (array-like): The y-values for the second set of data.
        - bar_width (float): The width of the bars in the bar chart.
        - title (str): The title of the bar chart.
        - label1 (str): The label for the first set of data.
        - label2 (str): The label for the second set of data.

        Returns:
        - None: The function displays the grouped bar chart using
        Matplotlib but does not return any value.
    """
    plt.figure(figsize = (12 , 8))
    plt.bar(barposition1 , data1 , width = bar_width ,
            label = label1 , color = 'blue')
    plt.bar(barposition2 , data2 , width = bar_width ,
            label = label2 , color = 'red')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title(title , fontsize = 20)

    # Adding legend
    plt.legend()

    # Display a grid
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()


def linePlot(data):
    """
        Plot a line chart showing the trend of high-technology exports
         for selected countries over the years.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing the data to be
         plotted. It should have columns 'Country Name',
          'Time', and 'High-technology exports (% of manufactured
          exports) [TX.VAL.TECH.MF.ZS]'.

        Returns:
        - None: The function displays the line chart using Matplotlib
        but does not return any value.
    """
    for country in ['India' , 'United States' , 'United Kingdom' ,
                    'United Arab Emirates' , 'Germany']:
        country_data = data[data['Country Name'] == country]
        plt.plot(country_data['Time'] ,
                 country_data['High-technology exports (% of manufactured exports) '
                              '[TX.VAL.TECH.MF.ZS]'] , label = country)

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('High-technology exports')
    plt.title('High-technology exports Over the Years' , fontsize = 20)

    # Adding legend
    plt.legend()

    # Display a grid
    plt.grid(True)
    plt.show()


def linePlot2(data):
    """
        Plot a line chart showing the trend of scientific and technical
        journal articles for selected countries over the years.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing the data to be
        plotted. It should have columns 'Country Name',
          'Time', and 'Scientific and technical journal articles [IP.JRN.ARTC.SC]'.

        Returns:
        - None: The function displays the line chart using Matplotlib but does not
         return any value.
    """
    for country in ['Canada' , 'Qatar' , 'Saudi Arabia' , 'Switzerland' , 'Germany']:
        country_data = data[data['Country Name'] == country]
        plt.plot(country_data['Time'] ,
                 country_data['Scientific and technical journal articles [IP.JRN.ARTC.SC]'] ,
                 label = country)
    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Scientific and technical journal articles')
    plt.title('Scientific and technical journal articles Over the Years' , fontsize = 20)
    # Adding legend
    plt.legend()
    # Display a grid
    plt.grid(True)
    plt.show()


"""TASK 1"""
year_as_column , country_as_column = transposingData('data.csv')
print("Country as column")
print(country_as_column.head())
print("Year as column")
print(year_as_column.head())


"TASk 2"
"STATISTICAL METHODS"
"METHOD 1"
"DESCRIBES"
print("DESCRIBES METHOD")
country_as_column['High-technology exports (% of manufactured exports) ' \
                  '[TX.VAL.TECH.MF.ZS]'] = \
    pd.to_numeric(country_as_column['High-technology exports (% of manufactured exports)'
                                    ' [TX.VAL.TECH.MF.ZS]'] ,
                                             errors = 'coerce')
describes = country_as_column['High-technology exports (% of manufactured exports)' \
                              ' [TX.VAL.TECH.MF.ZS]'].describe()
print(describes)

"METHOD 2"
country_as_column['Research and development expenditure (% of GDP) [GB.XPD.RSDV.GD.ZS]'] = \
    pd.to_numeric(country_as_column['Research and development expenditure (% of GDP) [GB.XPD.RSDV.GD.ZS]'] ,
                                             errors = 'coerce')
skewness = skew(country_as_column['Research and development expenditure (% of GDP) '
                                  '[GB.XPD.RSDV.GD.ZS]'].dropna())
print("Skewness for Research and development expenditure (% of GDP) [GB.XPD.RSDV.GD.ZS]"
      , skewness)


plot_histogram(country_as_column,
               'Research and development expenditure (% of GDP) [GB.XPD.RSDV.GD.ZS]' , skewness)

"METHOD 3"
country_as_column['Researchers in R&D (per million people) [SP.POP.SCIE.RD.P6]'] = \
    pd.to_numeric(country_as_column['Researchers in R&D (per million people) [SP.POP.SCIE.RD.P6]'] ,
                                             errors = 'coerce')
kurtosis_value = kurtosis(
    country_as_column['Researchers in R&D (per million people) [SP.POP.SCIE.RD.P6]'].dropna() ,
    fisher=False)
print("Kurtosis:" , kurtosis_value)

#plots

#Pie graph
country_as_column['Research and development expenditure (% of GDP) [GB.XPD.RSDV.GD.ZS]'] \
    = pd.to_numeric(country_as_column['Research and development expenditure (% of GDP) [GB.XPD.RSDV.GD.ZS]'],
                    errors = 'coerce')
# pie chart
piedata = country_as_column[(country_as_column['Time'] == '2018')]
title = 'Research and development expenditure (% of GDP)'
countrynames = []
sizes = []
for country in ['India' , 'United States' , 'United Kingdom' , 'United Arab Emirates' , 'Germany']:
    countrynames.append(country)
    country_data = piedata[piedata['Country Name'] == country]
    sizes.append(country_data['Research and development expenditure (% of GDP)'
                              ' [GB.XPD.RSDV.GD.ZS]'].values[0])
    # print(country_data['Agricultural land (% of land area)'].values)

piePlot(sizes , countrynames , title)

#Bar Graph
bar_width = 0.35
country_as_column['Patent applications, nonresidents [IP.PAT.NRES]'] = \
    pd.to_numeric(country_as_column['Patent applications, nonresidents [IP.PAT.NRES]'] , errors = 'coerce')
country_as_column['Patent applications, residents [IP.PAT.RESD]'] = \
    pd.to_numeric(country_as_column['Patent applications, residents [IP.PAT.RESD]'] , errors = 'coerce')
country_as_column['Time'] = pd.to_numeric(country_as_column['Time'] , errors = 'coerce')

bargraph_data = country_as_column[country_as_column['Country Name'] == 'United States']

bar_positions_nonresident = bargraph_data['Time'] - bar_width / 2
bar_positions_resident = bargraph_data['Time'] + bar_width / 2

data1 = bargraph_data['Patent applications, nonresidents [IP.PAT.NRES]']
data2 = bargraph_data['Patent applications, residents [IP.PAT.RESD]']
title = 'Patent applications , nonresidents vs residents'
label1= 'Patent applications , nonresidents'
label2 = 'Patent applications , residents [IP.PAT.RESD]'
barPlot(bar_positions_nonresident , bar_positions_resident , data1 , data2 , bar_width , title , label1 , label2)

#Line Graph
linePlot(country_as_column)

#Bar Graph
country_as_column['Time'] = pd.to_numeric(country_as_column['Time'] , errors = 'coerce')
country_as_column = country_as_column[(country_as_column['Time'] >= 2013)
                                      & (country_as_column['Time'] <= 2018)]
country_as_column['Researchers in R&D (per million people) [SP.POP.SCIE.RD.P6]'] \
    = pd.to_numeric(country_as_column['Researchers in R&D (per million people) [SP.POP.SCIE.RD.P6]']
                    ,errors = 'coerce')\
    .dropna()
country_as_column['Technicians in R&D (per million people) [SP.POP.TECH.RD.P6]'] \
    = pd.to_numeric(country_as_column['Technicians in R&D (per million people) [SP.POP.TECH.RD.P6]']
                    ,errors = 'coerce')\
    .dropna()
bar_positions_nonresident = country_as_column['Time'] - bar_width / 2
bar_positions_resident = country_as_column['Time'] + bar_width / 2

data1 = country_as_column['Researchers in R&D (per million people) [SP.POP.SCIE.RD.P6]']
data2 = country_as_column['Technicians in R&D (per million people) [SP.POP.TECH.RD.P6]']
title = 'Researchers in R&D vs Technicians in R&D'
label1 = 'Researchers in R&D'
label2 = 'Technicians in R&D'
barPlot(bar_positions_nonresident , bar_positions_resident , data1 , data2 ,
        bar_width , title , label1 , label2)

#Line Graph
linePlot2(country_as_column)



