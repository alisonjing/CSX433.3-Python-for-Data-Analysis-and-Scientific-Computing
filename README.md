# CSX433.3-Python-for-Data-Analysis-and-Scientific-Computing
Python course

CSX433.3 Python for Data Analysis and Scientific Computing
CSX433.7 Machine Learning with Tensorflow

Final Project -- Bitcoin Cryptocurrency Price Prediction using RNN, LSTM with Tensorflow

Alison Jing Huang  -- jing01ucsb@gmail.com
Github: https://github.com/alisonjing

Elaine Phan  --  elainph@gmail.com
Github: https://github.com/ElainePhan


The purpose of this project is to create a basic economic prediction model to estimate the future trend of bitcoin. The presentation will include functions to input bitcoin purchases at different prices from hour to hour, day to day, month to month and year to year. The data is loaded in xlsx text file format with different parameters such as purchase dates, purchase prices, open prices, high prices, low prices, purchase volume, purchase volume from, purchase volume to, time series and percent changes of price during a period of time. 

We plan to analyze the bitcoin data looking at low and high prices per day, month, and year using NumPy arrays, Matplotlib, and Scipy. We will use these libraries to analyzed the data to train our models with analytical tools such as Linear Regression, Time Series, Machine Learning (Long Short Term Memory (LSTM)) and Tensorflow. We will test our models using these tools to make prediction for the future trends of bitcoin.

Data Source:
https://www.investing.com/crypto/bitcoin/historical-data
https://www.cryptodatadownload.com/index.html


Executive Summary:
Cryptocurrency is the new investment rave at the moment and currently we are curious about the how it works, how it is used and what is the investment opportunities involved in investing in this type of commodity. 
The purpose of this project is to create a basic economic prediction model to estimate the future trend of bitcoin. The presentation will include functions to input bitcoin purchases at different prices from hour to hour, day to day, month to month and year to year. The data is loaded in xlsx text and csv file format with different parameters such as purchase dates, purchase prices, open prices, high prices, low prices, purchase volume, purchase volume from, purchase volume to, time series and percent changes of price during a period of time.   	We plan to analyze the bitcoin data looking at low and highs prices per day, month, and year using NumPy arrays, Matplotlib, and Scipy. We will use these libraries to analyzed the data to train our models with analytical tools such as Linear Regression, Time Series, Machine Learning (Long Short Term Memory (LSTM)) and Tensorflow. We will test our models using these tools to make prediction for the future trends of bitcoin.

Analyzing and Data Wrangling: 

As we clean the data from our hour by hour, day to day, month to month, and year to year we removed commas, percent signs and manipulated the date to make the xslx and csv file more readable in Jupyter. When uploading the files into Jupyter we checked each data set and looked up the max and min values of the parameters. This data allowed us to find the date of these events and make meaningful graphs to visually plot the moving prices of the different cryptocurrencies to show the volatility and stabilities of the coins in a time series graph. 

We tested our data set in different plots such as line graph, box plot, pairplot, histograms, sma, cma, and heatmaps, ARIMA models. 

Environment used to Setup and run the Project:

The project is developed using the following environment:

Mac 
  	Python 3.6.2 Andaconda custom (64-bit) Jupyter Notebook environment (version 5.0.0)
	
Referencing packages
	numpy
	matplotlib 	2.1.0
	scipy 		0.19.1
	pandas  	0.20.3
	seaborn	0.8.0
	scikit learn	0.19.1
	keras		2.2.0
	plotly		2.6.0
	cufflinks   	0.13.0	
        tensorflow    1.15.0


Running the Project:	

Step  1
Load all the dataset in to jupyter. 
List of the dataset:

BitcoinHistoricalDataByDay.xlsx
BitcoinHistoricalDataByDay2010to2018.xlsx
BitcoinHistoricalDataByWeek.xlsx
BitcoinHistoricalDatabyMonth.xlsx
Coinbase_BTCUSD_1h.xlsx
Coinbase_ETHUSD_1h.csv
Coinbase_LTCUSD_1h.csv


Step 2
After loading the dataset
Run the jupyter note book titled
“Bitcoin_Python_part.ipynb”

Step 3 Run on Machine Learning part of the project
Run the jupyter notebook titled 

“Bitcoin_ML_LSTM_part.ipynb”
