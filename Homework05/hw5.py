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

    # STARTING PROBLEM 1 -------------------------------------------------------------
    # getting our states
    states = [line.strip() for line in open("states.txt") if line.strip()]

    # create a dictionary to put each state with a set
    citiesPerState = {}
    # for zipcode in zipcodes:
    #     if zipcode.state not in citiesPerState:
    #         citiesPerState[zipcode.state] = set()
    #     citiesPerState[zipcode.state].add(zipcode.city)

    
    for state in states:                                # loop through the states
        citiesPerState[state] = set()                   # create a set for each state
        for zipcode in zipcodes:                        # loop through the zipcodes
            if state == zipcode.state:                  # if the state is the same as the zipcode's state
                citiesPerState[state].add(zipcode.city) # add the zipcode's city to the set

    commonCities = citiesPerState[states[0]]                            # start the intersection with the first set
    for state in states[1:]:                                            # skip the first set and start looping
        commonCities = commonCities.intersection(citiesPerState[state]) # intersect each set with the first one

    # myFile = open("CommonCityNames.txt", "w")
    # for city in sorted(commonCities):
    #     myFile.write(city + "\n")
    # myFile.close()

    with open("CommonCityNames.txt", "w") as myFile:
        myFile.writelines(f"{city}\n" for city in sorted(commonCities))
    # ENDING PROBLEM 1 -------------------------------------------------------------


    # STARTING PROBLEM 2 ---------------------------------------------------------
    # getting our zipcodes
    zips = [line.strip() for line in open("zips.txt") if line.strip()]

    # create a set to put our latitudes and longitudes as tuples
    zipsSet = set()
    # for zipcode in zipcodes:
    #     for zip in zips:
    #         if zip == zipcode.zipcode:
    #             zipsSet.add((zipcode.lat, zipcode.long))

    for zipcode in zipcodes:                            # start looping through zipcodes
        if zipcode.zipcode in zips:                     # if the zipcode is in the zips list
            zipsSet.add((zipcode.lat, zipcode.long))    # add the zipcodes lat and lon to a set as a tuple
    
    with open("LatLon.txt", "w") as myFile:
        myFile.writelines([f"{lat} {lon}\n" for lat, lon in zipsSet])
    # ENDING PROBLEM 2 -----------------------------------------------------------


    # STARTING PROBLEM 3 ---------------------------------------------------------
    # get our cities
    cities = [line.strip().lower() for line in open("cities.txt") if line.strip()]

    # create a dictionary to store each city with a set
    statesPerCity = {}                                  # create our dictionary
    for city in cities:                                 # start looping through cities
        statesPerCity[city] = set()                     # create a set for every city                                        
        for zipcode in zipcodes:                        # start looping through zipcodes
            if zipcode.city.strip().lower() == city:    # if the zipcode's city is the same as current city
                statesPerCity[city].add(zipcode.state)  # add the zipcode's state to the corresponding city's set

    with open("CityStates.txt", "w") as myFile:
        for city in statesPerCity:
            states = " ".join(sorted(statesPerCity[city]))  # join the elements of the set with a space
            myFile.write(f"{states}\n")
    # ENDING PROBLEM 3 -----------------------------------------------------------
    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  
    

