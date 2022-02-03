## Welcome to the League of Legends Pro player predictor!

The contents of this project will be very simple, due to the fact that we won't be deploying this to the real world.

There is a file in here called 'notebooks', which contain the 4 notebooks that were used to develop the xgboost model.

To simplify things whilst also making this script useful, this will not be an end-to-end implementation of the four notebooks (i.e. from Riot API call all the way to prediction.)

Instead, we will save the test-data in a folder in this github repo (A big no-no, I know, I would love to use a data store e.g. some cloud object storage, but I feel making a model store and data store in the cloud and connecting would be overkill for the purposes of this project)

Since we will have a clean dataset and a trained model, the only thing we will have to do is decide how to serve this data. To keep sizes down in github, we'll take a sample of 10,000 rows of amateur players and use this for the demo.


We will use FastAPI with two endpoints:
- getPlayers (this will give a list of all the amateur players in our test set. It will be a simple get request with no request body)
- ProOrAmateur (the only output will be a string in the set {'We think this person has pro potential!', 'Ah, this player needs to keep training'}) 

You can check the APIs config by typing /docs# after your localhost if running this code.

To run: you will need uvicorn (python library), and to host locally just type:

*uvicorn main:app --host 0.0.0.0 --port 80*