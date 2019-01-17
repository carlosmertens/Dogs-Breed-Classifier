# Sets pet_image variable to a filename
pet_image = "Boston_terrier_02259.jpg"

# Sets string to lower case letters
low_pet_image = pet_image.lower()
print(low_pet_image)

# Splits lower case string by _ to break into words
word_list_pet_image = low_pet_image.split("_")
print(word_list_pet_image)

# Create pet_name starting as empty string
pet_name = ""

# Loops to check if word in pet name is only
# alphabetic characters - if true append word
# to pet_name separated by trailing space
for word in word_list_pet_image:
    if word.isalpha():
        pet_name += word + " "
print(pet_name)

# Strip off starting/trailing whitespace characters
pet_name = pet_name.strip()

# Prints resulting pet_name
print("\nFilename=", pet_image, "   Label=", pet_name)
