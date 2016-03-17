## CustomerEvaluationSystem

###Function name:
	
	- customer evaluation system

###Author:
	 - xuxx

###Main function:
	 - This function is used to statistic and analysis of  hotels' reviews. 
	 The statistic and analysis are based on the keywords which users input. 
	 According to the keywords this function can returnthe statistic result 
	 to the users.
	 - In order to provide the users more accurate results, we provide some
	 basic search pattern to help the users to search, of course, 
	 this is model is transparent to users.

###Input and Output:
	 - input:
	 ["This is the key words you want to analysis" [,begin_time, end_time]], 
	 time formate shoud be YYYY-MM-DD
	 - output:
	 pie chart and abar chart about the result.
	 - Note:
	I have put the picture to explain this part, you can find it in the doc.

###How To Run :
	 - cd the ReviewsAnalysis in the cmd env of windows.
	 - Enter "python main.py".
	 - According to the prompt, you should enter a keyword.
	 - Then you get the result.

###Manifest:
	 - csvFile.py is used to read the csv file and store the records in a list.
	 and provide a function to general some sample to do the test.
	 - Pattern.py is used to define a list of  semantic associated keywords.
	 - TimeConversion.py is used to convert the date and timestamp.
	 - WordCount.py is used to statistic the data whitch provied to plot.
	 - ShowDate.py is used to plot the data.
	 - ShowApp.py is used to cout the records in text fram.
	 - main.py is used to run this model. 
###Note:
	 - In this function the design of CSV file is like this:
	 [Id, reviews, rates, timeStamp]
	 - The environment of the model is Windows with 64bit and the version
	 of python is python2.7. 
	 - If you want to run this function, you have to install some
	 packages of python2.7. Based on your system, if your system is 64bit,
	 should chosen the 64bit version to install, if your system is 32bit,
	 should chosen the 32bit version to install.
	 - Packages: scipy, numpy, matplotlib. I will provide the 64bit soft
	 for you to install, you can find them in the doc, I also provide the
	 pip for you to install the *.whl file.
