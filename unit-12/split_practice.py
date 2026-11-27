
# Create a comma-separated string of African countries
countries = "Nigeria,Ghana,Kenya,South Africa,Egypt"

# Create a date string
date = "27/11/2026"

# Split the strings
country_list = countries.split(",")
date_parts = date.split("/")

# Print individual countries
print("African countries:")
print(country_list[0])
print(country_list[1])
print(country_list[2])
print(country_list[3])
print(country_list[4])

# Print individual date components using indexes
print("Date components:")
print("Day:", date_parts[0])
print("Month:", date_parts[1])
print("Year:", date_parts[2])

