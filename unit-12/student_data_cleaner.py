
# Simulate messy student registration data
name = "   rOsHeEdAh dHiKrUlLaH   "
email = "  ROSHEEDAH@GMAIL.COM  "
phone = "  0803-456-7890  "

# Clean the registration data using method chaining
clean_name = name.strip().title()
clean_email = email.strip().lower()
clean_phone = phone.strip().replace("-", "")

# Validate the cleaned data
valid_email = "@" in clean_email
valid_phone = len(clean_phone) == 11

# Print the cleaned student profile
print("STUDENT PROFILE")
print("--------------------")
print("Name:", clean_name)
print("Email:", clean_email)
print("Phone:", clean_phone)

print("--------------------")
print("Email valid:", valid_email)
print("Phone number valid:", valid_phone)

