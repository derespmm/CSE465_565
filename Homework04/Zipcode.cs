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
                RecordNumber = values.Length > 0 && int.TryParse(values[0], out int recordNumber) ? recordNumber : 0,
                ZipCode = values.Length > 1 && int.TryParse(values[1], out int zipCode) ? zipCode : 0,
                ZipCodeType = values.Length > 2 ? values[2] : "",
                City = values.Length > 3 ? values[3] : "",
                State = values.Length > 4 ? values[4] : "",
                LocationType = values.Length > 5 ? values[5] : "",
                Lat = values.Length > 6 && double.TryParse(values[6], out double lat) ? lat : 0.0,
                Long = values.Length > 7 && double.TryParse(values[7], out double lon) ? lon : 0.0,
                Xaxis = values.Length > 8 && double.TryParse(values[8], out double x) ? x : 0.0,
                Yaxis = values.Length > 9 && double.TryParse(values[9], out double y) ? y : 0.0,
                Zaxis = values.Length > 10 && double.TryParse(values[10], out double z) ? z : 0.0,
                WorldRegion = values.Length > 11 ? values[11] : "",
                Country = values.Length > 12 ? values[12] : "",
                LocationText = values.Length > 13 ? values[13] : "",
                Location = values.Length > 14 ? values[14] : "",
                Decommissioned = values.Length > 15 && bool.TryParse(values[15], out bool decommissioned) ? decommissioned : false,
                TaxReturnsFiled = values.Length > 16 && int.TryParse(values[16], out int taxReturns) ? taxReturns : 0,
                EstimatedPopulation = values.Length > 17 && int.TryParse(values[17], out int population) ? population : 0,
                TotalWages = values.Length > 18 && int.TryParse(values[18], out int wages) ? wages : 0,
            };
            zipcodes.Add(zipcode);
        }
        return zipcodes;
    }
}