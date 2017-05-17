### Airfinity Testing

This is a program designed to read data from various .csv sheets, join
the data with an events.db csv sheet, and write the joined output out to
a new set of csv sheets set up by event_name and date.
The code was written by Fernando Pombeiro: fernpombeiro@yahoo.com

## Running

To run the code you first have to activate the environment by entering the
following:
```python

source airfinity_env/bin/activate
```

*Congrats*- you are now up and running in the environment. Now- to ensure that
you have the correct packages installed please run the following:

```python
pip install -r requirements.txt
```

*This will install the necessary packages into the environment*

Now you are ready to go. The program was written in python3 so run the
following command to run the program:

```python
python3 airfinity_coding_answer.py
```

This should automatically populate the necessary csvs.

*Please note that you cannot change the names of the directories (like the _DataEngineeringExercise_ directory)
or you will break the package*

_I have written a total of Five Tests which can be run with the following command_

```python
python3 test_airfinity_answer.py
```

*Enjoy!*