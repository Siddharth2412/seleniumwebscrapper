import pandas as pd
from productScrapper import Product
import csv


column_names = ["Brand", "Name"]
df = pd.read_csv("data.csv", names=column_names)
brand = list(df["Brand"])[1:]
name = list(df["Name"])[1:]
products = []
for i in range(len(brand)):
    p = Product(brand[i], name[i])
    p.getdata()
    products.append(p)
f = open('output.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(["Brand", "Name", "Price", "Delivery time", "Needle size", "Composition"])
temp = []
for p in products:
    temp.append([p.brand, p.name, p.price, p.delivery_time, p.needle_size, p.composition])
writer.writerows(temp)
f.close()