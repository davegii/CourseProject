# CourseProject

**Group Presentation**
https://mediaspace.illinois.edu/media/t/1_zbw469gj

1. An overview of the function of the code (i.e., what it does and what it can be used for).

Our application takes in a sentence and returns the overall sentiment of it along with its categories. The categories are broken into three sections: negative, neutral, and positive. To obtain real-life sentences, our application is connected with the Twitter API and extracts tweets for us to analyze. 

2. Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement. 

In order to implement our project, we utilized Twitter’s API in order to access tweets for any topic we wanted to analyze. Right now our implementation is not able to handle emojis, so we have a function that works on cleaning up the text, in particular getting rid of emojis. The rest of the implementation in terms of analyzing tweets, runs through the twitter api function, .search_tweets. With this you are able to modify a few parameters to fine tune what you want to search for. The key parameters are the search word you are using, this changes the topic that you will get tweets about. The final key parameter is the count, this will change the amount of tweets that you will receive about that topic. Then the function will gather an overall sentiment of the tweets for that topic.

3. Detailed instructions on how to install and run a software, whichever is applicable.

Instructions:

* Download or clone repository and navigate to the folder
* Install the required imports through requirements.txt:
>pip install -r requirements.txt
* To run the tests, uncomment the bottom part of analysis.py and run:
>python analysis.py
* To run the twitter sentiment analysis, comment the bottom part of analysis.py if it was uncommented and run:
>python twitter.py
* (Optional) In twitter.py, you can edit the search_words variable in order to query results on different topics as well as change the count variable to output a different number of tweets


4. Brief description of contribution of each team member in case of a multi-person team. 


In terms of contributions, all team members conducted research into the different tools to utilize for our project. This process was lengthy and the quality of knowledge gained was valuable. Ron and Davy researched which libraries to use for sentiment analysis and the ideal thresholds and parameters for analysis. Tony and Pranith researched connecting to the Twitter API and resolving any dependency and Twitter version issues with our current application. 

Aside from research, the more individual work on the actual project was broken down as follows:

Everyone:
Explored and agreed on an overall algorithm for the project
Determined how to split up the different functionalities in code

Pranith: 
Worked w/ Tony on writing Twitter API calls
Fixed old library dependency issues
Tested sentiment analysis code
Planned the presentation

Tony: 
Worked w/ Pranith on writing Twitter API calls
Explored other routes for retrieving text data from Twitter to determine the most efficient
Tested different data structures to determine the most useful format

Davy: 
Worked w/ Ron on writing Sentiment Analysis code and testing
Determined thresholds
Managed video-editing and submissions

Ron: 
Worked w/ Davy on writing Sentiment Analysis code and testing
Determined best sentiment library
Created test datasets to compare quality of results

