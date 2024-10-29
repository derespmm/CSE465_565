/* 
  Homework#4

  Add your name here: Matt DeRespinis

  You are free to create as many classes within the Hw4.cs file or across 
  multiple files as you need. However, ensure that the Hw4.cs file is the 
  only one that contains a Main method. This method should be within a 
  class named hw4. This specific setup is crucial because your instructor 
  will use the hw4 class to execute and evaluate your work.
  */
// BONUS POINT:
// => Used Pointers from lines 10 to 15 <=
// => Used Pointers from lines 40 to 63 <=


using System;
using System.Collections.Generic;
using System.IO;

public class Hw4
{
    public static void Main(string[] args)
    {
        // Capture the start time
        // Must be the first line of this method
        DateTime startTime = DateTime.Now; // Do not change
        // ============================
        // Do not add or change anything above, inside the 
        // Main method
        // ============================
        List<Zipcode> zipcodes = Zipcode.readZipCodes("zipcodes.txt"); // getting all zipcode objects
        string[] cities = File.ReadAllLines("cities.txt"); // getting all city names
        string[] states = File.ReadAllLines("states.txt"); // getting all state names
        string[] lines = File.ReadAllLines("zips.txt"); // getting all zipcodes
        List<int> zips = new List<int>();
        for (int i = 0; i < lines.Length; i++)
        {
            zips.Add(int.Parse(lines[i]));
        }


        //Starting the first problem
        // Making a new hashset for every state in our states.txt file, and 
        // storing every one of its cities in the hashset. 
        Dictionary<string, HashSet<string>> citiesPerState = new Dictionary<string, HashSet<string>>();
        foreach (Zipcode zipcode in zipcodes)
        {
            if (!citiesPerState.ContainsKey(zipcode.State))
            {
                citiesPerState.Add(zipcode.State, new HashSet<string>());
            }
            citiesPerState[zipcode.State].Add(zipcode.City);
        }

        // making a hashset which is equal to the hashset associated with the first
        // state in the states list.
        // We can pick any hashset to start the intersect
        HashSet<string> commonCities = new HashSet<string>(citiesPerState[states[0]]);
        for (int i = 1; i < states.Length; i++)
        {
            commonCities.IntersectWith(citiesPerState[states[i]]);
        }

        List<string> commonCitiesList = new List<string>(commonCities);
        commonCitiesList.Sort();

        foreach (string city in commonCitiesList)
        {
            File.AppendAllText("CommonCityNames.txt", city + "\n");
        }


        // Starting second problem 
        foreach (int zip in zips)
        {
            for (int i = 0; i < zipcodes.Count; i++)
            {
                if (zip == zipcodes[i].ZipCode)
                {
                    File.AppendAllText("LatLon.txt", zipcodes[i].Lat + " " + zipcodes[i].Long + "\n");
                    break;
                }
            }
        }

        // Starting third problem
        Dictionary<string, SortedSet<string>> cityStates = new Dictionary<string, SortedSet<string>>();

        foreach (string city in cities)
        {
            SortedSet<string> statesForCity = new SortedSet<string>();

            foreach (Zipcode zipcode in zipcodes)
            {
                if (city.Trim().Equals(zipcode.City.Trim(), StringComparison.OrdinalIgnoreCase))
                {
                    statesForCity.Add(zipcode.State); 
                }
            }

            if (statesForCity.Count > 0)
            {
                cityStates[city] = statesForCity;
            }
        }

        
        foreach (var entry in cityStates)
        {
            File.AppendAllText("CityStates.txt", "");
            foreach (var state in entry.Value)
            {
                File.AppendAllText("CityStates.txt", $"{state} ");
            }
            File.AppendAllText("CityStates.txt", "\n"); 
        }






        // ============================
        // Do not add or change anything below, inside the 
        // Main method
        // ============================

        // Capture the end time
        DateTime endTime = DateTime.Now;  // Do not change

        // Calculate the elapsed time
        TimeSpan elapsedTime = endTime - startTime; // Do not change

        // Display the elapsed time in milliseconds
        Console.WriteLine($"Elapsed Time: {elapsedTime.TotalMilliseconds} ms");
    }
}
