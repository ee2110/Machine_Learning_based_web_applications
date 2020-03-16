# Text Sentiment Classification

This product is a text sentiment analysis web application. The main function is to classify the sentiment of input words or sentence. The classification model is trained by Multinomial Naive Bayes algorithm with 1,600,000 sentences extracted from Tweets. The data set can be obtained from <a href="https://www.kaggle.com/kazanova/sentiment140">Kaggle</a>. <br>

The model still required a big step of improvements to achieve higher accuracy. <br>

# To run the web application in local

<ol>
<li>Download or clone the git repository</li><br>
  
```
$ git clone https://github.com/EeYeoKeat/Machine_Learning_based_web_applications.git
```

<li>Change directory to the local repository folder</li><br>

```
$ cd D:\GitHub\Machine_Learning_based_web_applications\Text_Sentiment_Analysis_Web
```

###### Perform following action to set up environment and install Flask with the packages. If you have activated environment and installed Flask and the dependencies, you may skipped and continue from step 8 to run application directly. Remember to activate the environment.

<li>Create and manage environment</li><br>

```
$ py -m venv env
```

<li>Activate the environment</li><br>

```
$ env\Scripts\activate
```

After that, you will noticed that environment activation done when indicated by (env) at beginning. Example as below.

```
(env) PS D:\GitHub\Machine_Learning_based_web_applications\Text_Sentiment_Analysis_Web>
```

<li>Install Flask using pip</li><br>

```
$ pip install flask
```

<li>Install Numpy Pandas Scikit-learn libraries</li><br>

```
$ pip install numpy pandas sklearn
```

<li>Set environment variable</li><br>

```
$ set FLASK_APP=app.py
```

<li>Run application</li><br>

```
$ flask run
```

At last step, to terminate application running, press `ctrl+c` and then deactivate the environment before `exit`.

```
$ deactivate
```


</ul>

# Layout

You may enter any sentence and click “CHECK" button.

<img src="https://github.com/EeYeoKeat/Machine_Learning_based_web_applications/blob/master/Text_Sentiment_Analysis_Web/img/page1.JPG">

# Some Results

For test if the model determine negative sentiment, a word "cry" was entered for testing. It classified it as negative sentiment.

<img src="https://github.com/EeYeoKeat/Machine_Learning_based_web_applications/blob/master/Text_Sentiment_Analysis_Web/img/negative.JPG">

For positive, a word "Happy" was entered and the result shows positive sentiment

<img src="https://github.com/EeYeoKeat/Machine_Learning_based_web_applications/blob/master/Text_Sentiment_Analysis_Web/img/positive.JPG">


# Dependencies
<ul>
<li>Flask</li>
<li>Numpy</li>
<li>Pandas</li>
<li>Scikit-learn</li>
<li>Materialize</li>
</ul>
