import csv
import random

import pandas as pd
from faker import Faker

fake = Faker()

# Possible values for our CSV data
locations = [ 'York', 'Leeds', 'Sheffield', 'Bradford', 'Huddersfield', 'Hull', 'Wakefield', 'Harrogate', 'Barnsley', 'Rotherham', 'Scarborough', 'Doncaster', 'Ripon', 'Halifax', 'Skipton', 'Beverley', 'Keighley', 'Batley', 'Dewsbury', 'Selby', 'Bridlington', 'Pudsey', 'Ilkley', 'Brighouse', 'Whitby', 'Castleford', 'Pontefract', 'Richmond', 'Goole', 'Otley', 'Wetherby', 'Malton', 'Hebden Bridge', 'Knaresborough', 'Northallerton', 'Thirsk', 'Settle', 'Todmorden', 'Bingley', 'Filey', 'Shipley', 'Ossett', 'Morley', 'Holmfirth', 'Penistone', 'Barnoldswick', 'Hawes', 'Masham', 'Knottingley', 'Hornsea']
asset_type = ['SPS', 'CSO', 'STW']
incident_types = ['Cat 1', 'Cat 2', 'Cat 3', 'Cat 4', 'No Pollution', 'Near Miss']
possible_causes = ['Equipment Malfunction', 'Overflow Due to Heavy Rain', 'Corroded Pipeline', 'Tanker Truck Accident', 'Construction Near Water Source', 'Human Error', 'Power Outage at Treatment Facility', 'N/A', 'NULL']

# File writing
with open('pollution_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Location', 'Incident Type', 'Estimated Volume (Liters)', 'Possible Cause'])

    for _ in range(10000):
        writer.writerow([
            fake.date_this_year(),
            random.choice(locations),
            random.choice(asset_type),
            random.choice(incident_types),
            random.choice(possible_causes)
        ])

print("CSV file generated!")