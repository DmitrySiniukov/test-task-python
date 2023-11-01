## My solution for the python test task

### Pre-requisites:

- python version >= 3.8
- an environment managing system (venv, conda, etc)
- docker

### Installation
In a new python environment, please, run:
```
pip install -r requirements.txt
```

### Testing

#### Part 1
```
python part1.py
```
You should see the following output:
![Image #1](static/output1.png?raw=true "Output #1")
![Image #2](static/output2.png?raw=true "Output #2")

#### Part 2
In the current terminal window run:
```
docker run -d -p 6005:6379 --name redis_server redis:alpine3.17  redis-server --bind 0.0.0.0
export REDIS_PORT=6005
export STREAM_NAME=messages_stream
python part2_producer.py
```
In a new terminal (after activating your python environment), run:
```
python part2_consumer.py
```
You should see the following output:
![Image #3](static/output3.png?raw=true "Output #3")

Try entering sentences in the first terminal, and you should see them in the second one:
![Image #4](static/output4.png?raw=true "Output #4")

Press `ctrl+c` to exit.
#### part 3
Run:
```
python part3.py
```
You should see the following output:
![Image #5](static/output5.png?raw=true "Output #5")

Try entering some sentences, and see the output:
![Image #6](static/output6.png?raw=true "Output #6")

About the natural language processing model I used:
> I used a light version of the Bert model for natural language processing and text analysis.
> Since there is no specific directions on how the NER results are going to be used,
> I chose a simple generic model that works well enough for general text analysis.
> This model uses LSTM and recurrent layers, which allows to analyze a text sentence
> as a whole, and not taking into account only every specific word. This allows to
> infer entities that have not even been present in the initial dataset. Of course,
> it would be also possible to fine-tune this model on a more specific dataset,
> if there was a need in more customized and precise inferences.


#### part 4
Run the following command in the current terminal window:
```
python part4.py
```
Run the consumer from the part #2 in a separate terminal:
```
python part2_consumer.py
```
You should see the following output:
![Image #7](static/output7.png?raw=true "Output #7")

Try entering "analyze" in the first terminal. After that, input an arbitrary
text sentence, and see the output in the second terminal:
![Image #8](static/output8.png?raw=true "Output #8")


Press `ctrl+c` to exit.

#### Testing
Run the following command:
```
python -m unittest discover test
```

You should see the following output:
![Image #9](static/output9.png?raw=true "Output #9")
