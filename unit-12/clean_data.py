
# Create two strings with extra whitespace and inconsistent capitalisation
first_string = "   rOsHeEdAh dHiKrUlLa   "
second_string = "   PHARMACY student at oau   "

# Print original strings
print("Original first string:", first_string)
print("Original second string:", second_string)

# Clean the strings
cleaned_first = first_string.strip().title()
cleaned_second = second_string.strip().lower()

# Use replace()
cleaned_second = cleaned_second.replace("oau", "obafemi awolowo university")

# Print cleaned strings
print("Cleaned first string:", cleaned_first)
print("Cleaned second string:", cleaned_second)

