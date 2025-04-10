# teamMember03.py
# Jacob Farrell

class teamMember03:
    def print_something_interesting(self, data):

        """
        Analyze car price data to find the brand with the highest average resale price.

        @param data: list of dictionaries with at least "Brand" and "Price" keys
        @return None
        """

        brand_totals = {}
        brand_counts = {}

        for row in data:
            brand = row["Brand"]
            price = float(row["Price"])

            if brand not in brand_totals:
                brand_totals[brand] = 0
                brand_counts[brand] = 0

            brand_totals[brand] += price
            brand_counts[brand] += 1

        brand_averages = {}
        for brand in brand_totals:
            brand_averages[brand] = brand_totals[brand] / brand_counts[brand]

        top_brand = max(brand_averages, key=brand_averages.get)
        top_price = brand_averages[top_brand]

        total_price = sum(float(row["Price"]) for row in data)
        overall_avg = total_price / len(data)

        print("team member 03 says:")
        print(f"{top_brand} has the highest average resale price at ${top_price:.2f}")
        print(f"The overall average is ${overall_avg:.2f}")

         