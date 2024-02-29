import requests
import csv

with open("my_file.csv","r")  as file :
    raw_data = file.readlines()[-1] 
    data = raw_data.split(",")
    id = int(data[0])


print("id",id)

while True:
    id += 1
    url = f"https://gplinks.in/track/data.php?request=getVisitor&vid={id}"
    print(id+1)
    respons = requests.get(url)
    data = respons.json()
    
    # Open the file in writing mode
    with open('my_file.csv', 'a', newline='') as f:

        # Create the writer with the dictionary keys as headers
        writer = csv.DictWriter(f, fieldnames=data.keys())

        # Write the header defined in the fieldnames argument
        #print(writer.writeheader())
        writer.writerow(data)
    #print(data.())