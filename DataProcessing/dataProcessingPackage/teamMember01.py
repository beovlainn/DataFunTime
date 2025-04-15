# teamMember01.py

class teamMember01:
    def print_something_interesting(self, data):
        print("team member 01")
        brand_count = {}
        for row in data:
            brand = row["Brand"]
            brand_count[brand] = brand_count.get(brand, 0) + 1
        most_common_brand = max(brand_count, key=brand_count.get)
        print(f"The most common brand is {most_common_brand} with {brand_count[most_common_brand]} cars.")