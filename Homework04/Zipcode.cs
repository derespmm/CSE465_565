using System;
using System.Collections.Generic;
using System.IO;

public class Zipcode 
{
    public int RecordNumber { get; set; }
    public int ZipCode { get; set; }
    public string ZipCodeType { get; set; }
    public string City { get; set; }
    public string State { get; set; }
    public string LocationType { get; set; }
    public double Lat { get; set; }
    public double Long { get; set; }
    public double Xaxis { get; set; }
    public double Yaxis { get; set; }
    public double Zaxis { get; set; }
    public string WorldRegion { get; set; }
    public string Country { get; set; }
    public string LocationText { get; set; }
    public string Location { get; set; }
    public bool Decommissioned { get; set; }
    public int TaxReturnsFiled { get; set; }
    public int EstimatedPopulation { get; set; }
    public int TotalWages { get; set; }

    public static List<Zipcode> readZipCodes(string file) 
    {
        List<Zipcode> zipcodes = new List<Zipcode>();
        string[] lines = File.ReadAllLines(file);
        foreach (string line in lines) 
        {
            string[] values = line.Split('\t');
            Zipcode zipcode = new Zipcode 
            {
                RecordNumber = int.Parse(values[0]),
                ZipCode = int.Parse(values[1]),
                ZipCodeType = values[2],
                City = values[3],
                State = values[4],
                LocationType = values[5],
                Lat = double.Parse(values[6]),
                Long = double.Parse(values[7]),
                Xaxis = double.Parse(values[8]),
                Yaxis = double.Parse(values[9]),
                Zaxis = double.Parse(values[10]),
                WorldRegion = values[11],
                Country = values[12],
                LocationText = values[13],
                Location = values[14],
                Decommissioned = bool.Parse(values[15]),
                TaxReturnsFiled = int.Parse(values[16]),
                EstimatedPopulation = int.Parse(values[17]),
                TotalWages = int.Parse(values[18]),
            };
            zipcodes.Add(zipcode);
        }
        return zipcodes;
    }
}