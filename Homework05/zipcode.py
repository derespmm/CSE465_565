

class Zipcode:
    def __init__(self, record_number=None, zipcode=None, zipcode_type=None, city=None, state=None,
                 location_type=None, lat=None, long=None, xaxis=None, yaxis=None, zaxis=None,
                 world_region=None, country=None, location_text=None, location=None, decommissioned=None,
                 tax_returns_filed=None, estimated_population=None, total_wages=None, notes=None):
        self.record_number = record_number
        self.zipcode = zipcode
        self.zipcode_type = zipcode_type
        self.city = city
        self.state = state
        self.location_type = location_type
        self.lat = lat
        self.long = long
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.zaxis = zaxis
        self.world_region = world_region
        self.country = country
        self.location_text = location_text
        self.location = location
        self.decommissioned = decommissioned
        self.tax_returns_filed = tax_returns_filed
        self.estimated_population = estimated_population
        self.total_wages = total_wages
        self.notes = notes

    def __repr__(self):
        return f"Zipcode({self.zipcode})"

    def read_zipcodes(file_path):
        zipcodes = []
        with open(file_path, 'r') as file:
            headers = file.readline().strip().split('\t')

            for line in file:
                values = line.strip().split('\t')
                values = [val if val != '' else None for val in values]
                zipcode_data = dict(zip(headers, values))
            
                zipcode = Zipcode(
                    record_number=zipcode_data.get("RecordNumber"),
                    zipcode=zipcode_data.get("Zipcode"),
                    zipcode_type=zipcode_data.get("ZipCodeType"),
                    city=zipcode_data.get("City"),
                    state=zipcode_data.get("State"),
                    location_type=zipcode_data.get("LocationType"),
                    lat=float(zipcode_data["Lat"]) if zipcode_data.get("Lat") else None,
                    long=float(zipcode_data["Long"]) if zipcode_data.get("Long") else None,
                    xaxis=float(zipcode_data["Xaxis"]) if zipcode_data.get("Xaxis") else None,
                    yaxis=float(zipcode_data["Yaxis"]) if zipcode_data.get("Yaxis") else None,
                    zaxis=float(zipcode_data["Zaxis"]) if zipcode_data.get("Zaxis") else None,
                    world_region=zipcode_data.get("WorldRegion"),
                    country=zipcode_data.get("Country"),
                    location_text=zipcode_data.get("LocationText"),
                    location=zipcode_data.get("Location"),
                    decommissioned=zipcode_data.get("Decommisioned") == 'true',
                    tax_returns_filed=int(zipcode_data["TaxReturnsFiled"]) if zipcode_data.get("TaxReturnsFiled") else None,
                    estimated_population=int(zipcode_data["EstimatedPopulation"]) if zipcode_data.get("EstimatedPopulation") else None,
                    total_wages=float(zipcode_data["TotalWages"]) if zipcode_data.get("TotalWages") else None,
                    notes=zipcode_data.get("Notes")
                )
                zipcodes.append(zipcode)
        return zipcodes
