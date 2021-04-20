#Generate searchlist json file with category and term keys

import json

with open('dmsne-all-data.json') as f1:
  mainData = json.load(f1)


product_keys = mainData.keys()

print(product_keys)
product_details = []
for key in product_keys:
  # print(key)
  # print("\n")
  product = key
  #print(product)

  for i in range(1, len(mainData[product])):
    print(mainData[product][i]["name"])
    keys = {}
    #print("Appending")
    keys["category"] = product
    keys["term"] = mainData[product][i]["name"]
    product_details.append(keys)


print(product_details)

json_object = json.dumps(product_details, indent = 4)
with open("searchlist.json", "w") as outfile:
    outfile.write(json_object)
# f = open("dmseMODIFIED.json", "a")
# f.write(str(mainData))
# f.close()


# for key in mainData.keys():

#     print(mainData[key])
#     print("\n")



# for key in mainData.keys():
#     print(type(key))
#     print("\n")
