#This is a script that replaces the reviews of a product with my own reviews.

import json

with open('dmsne-json.json') as f1:
  mainData = json.load(f1)

with open('reviews.json') as f2:
  reviewDataSets = json.load(f2)


product_keys = mainData.keys()

for key in product_keys:
  # print(key)
  # print("\n")
  product = key
  product_details = []
  for i in mainData[product]:
    product_details.append(i)
  for i in range(1, len(product_details)):
    j = 0
    for i in range(1, len(product_details)):
      if(j == 3):
        j = 0
      product_details[i]["reviews"] = reviewDataSets[j]
      j = j+1
  




json_object = json.dumps(mainData, indent = 4)
with open("sample.json", "w") as outfile:
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
