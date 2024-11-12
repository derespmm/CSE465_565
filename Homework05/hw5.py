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
    states = [line.strip() for line in open("states.txt") if line.strip()]

    citiesPerState = {}
    # for zipcode in zipcodes:
    #     if zipcode.state not in citiesPerState:
    #         citiesPerState[zipcode.state] = set()
    #     citiesPerState[zipcode.state].add(zipcode.city)

    for state in states:
        citiesPerState[state] = set()
        for zipcode in zipcodes:
            if state == zipcode.state:
                citiesPerState[state].add(zipcode.city)

    commonCities = citiesPerState[states[0]]
    for state in states[1:]:
        commonCities = commonCities.intersection(citiesPerState[state])

    # myFile = open("CommonCityNames.txt", "w")
    # for city in sorted(commonCities):
    #     myFile.write(city + "\n")
    # myFile.close()

    with open("CommonCityNames.txt", "w") as myFile:
        myFile.writelines(f"{city}\n" for city in sorted(commonCities))
    # ENDING PROBLEM 1 -------------------------------------------------------------


    # STARTING PROBLEM 2 ---------------------------------------------------------
    zips = [line.strip() for line in open("zips.txt") if line.strip()]

    zipsSet = set()
    # for zipcode in zipcodes:
    #     for zip in zips:
    #         if zip == zipcode.zipcode:
    #             zipsSet.add((zipcode.lat, zipcode.long))

    for zipcode in zipcodes:
        if zipcode.zipcode in zips:
            zipsSet.add((zipcode.lat, zipcode.long))
    
    with open("LatLon.txt", "w") as myFile:
        myFile.writelines([f"{lat} {lon}\n" for lat, lon in zipsSet])
    # ENDING PROBLEM 2 -----------------------------------------------------------


    # STARTING PROBLEM 3 ---------------------------------------------------------
    cities = [line.strip().lower() for line in open("cities.txt") if line.strip()]

    statesPerCity = {}
    for city in cities:
        statesPerCity[city] = set()
        for zipcode in zipcodes:
            if zipcode.city.strip().lower() == city:
                statesPerCity[city].add(zipcode.state)

    with open("CityStates.txt", "w") as myFile:
        for city in statesPerCity:
            states = " ".join(sorted(statesPerCity[city]))
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
    

