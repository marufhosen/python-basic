from calculation import calculation_method  # import from module
import json

property_list = [
    {
        "title": "single_family_residence",
        "liv_area": 1050,
        "bedrooms": 1,
        "bathrooms": 1,
        "sqft_living": 1000,
        "sqft_lot": 1000,
        "floors": 1,
    },
    {
        "title": "vacant_land",
        "liv_area": 1050,
        "bedrooms": 1,
        "bathrooms": 1,
        "sqft_living": 1000,
        "sqft_lot": 1000,
        "floors": 1,
    },

]

# Encode a pthon dictionary as JSON string using json.dumps()
# Convert a JSON string back to a dictionary
data = json.loads(json.dumps(property_list))

for property in data:
    print(property)
    if property["title"] == "vacant_land":
        print(property["title"])
    else:
        print("No vacant land")


# print("res " + str(calculation_method(5, 10)))
