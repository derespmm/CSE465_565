import time
from zipcode import Zipcode

"""
  Homework#5

  Add your name here: Matt DeRespinis

  You are free to create as many classes within the hw5.py file or across 
  multiple files as you need. However, ensure that the hw5.py file is the 
  only one that contains a __main__ method. This specific setup is crucial 
  because your instructor will run the hw5.py file to execute and evaluate 
  your work.

"""
"""
1- => Lambda was used in line/s: ............
2- => Filter or map was used in line/s: ...........
3- => yield was used in line/s: .........
"""

if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inisde the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    
    # getting our zipcodes
    zipcodes = Zipcode.read_zipcodes("zipcodes.txt")

    # STARTING PROBLEM 1
    myFile = open("states.txt", "r")
    states = myFile.readlines()
    myFile.close()

    citiesPerState = {}
    for zipcode in zipcodes:
        if zipcode.State not in citiesPerState:
            citiesPerState[zipcode.State] = set()
        citiesPerState[zipcode.State].add(zipcode.City)

    commonCities = citiesPerState[states[0]]
    for state in states[1:]:
        commonCities = commonCities.intersection(citiesPerState[state])

    


    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
    

