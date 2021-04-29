# ADDITest

This is the technical test of python developer vacancy at ADDI.

## Requirements

- Python 3.8 or greater
- Pipenv (Python package manager): To install just run `pip3 install pipenv`

## Run the python app

To run the python app just follow the next steps:

1. Clone the repository and get inside the root directory
2. Activate the python virtualenv with `pipenv shell`
3. Install the required packages with `pipenv install`
4. Run the app with `python main.py`
5. Run `python -m unittest` to run the unit tests

Then the python application will run in the CLI.

## Assumptions

The assumptions taken for the technical test development were related to the external systems requests (the first two validations), for both I toke a simple approach to make that those requests returns the values `successful` or `failure` in a random way per request, so there is no logical process that validates one or more of the person data, instead any call will return a random state.

Another assumption taken was about the fake latency that the application should introduce per request. In this case I developed a simple `LatencySimulator` class in which based on bytes quantity and a fake bandwidth value, with this value the application makes a simple calculation of the latency. Both values are random integers, for bytes quantity integers between 1024 and 2048 "bytes" and for the bandwidth value a value between 10 and 500 "Mb". This values could change class definition.

Finally for the internal qualification system, the class allows to define the range of the qualification and the minimum required score to pass. In that way is possible to generate random scores with the given range and then evaluate that score with the minimum required score set.

## Decisions

The main decision taken for the test development is about the approach followed to run parallel tasks, because I design the application based in POO is not possible to implement the parallel processes with the package `multiprocessing`, because there is not a straightforward way to exchanges instanced objects between the main thread and the parallel processes, so the object attributes never be updated. By the other hand, using `Threads` is possible to achieve this because the threads shares the memory with the main thread, so any thread could access to the objects and modify their attributes.

## Improvements

- Make the application persistent and only kill the process when the user need it, instead of run the application for validate each person
- Adds a feature to read person information from a `.csv` file to avoid the manual process to insert the data and generate a report with the results for each person