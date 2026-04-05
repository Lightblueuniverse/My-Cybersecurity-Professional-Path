# Function to add a new setting to the dictionary
def add_setting(set_dictionary, set_tuple):
    # Unpack the tuple into key and value
    key, value = set_tuple

    # Convert both to lowercase for consistency
    key = key.lower()
    value = value.lower()

    # Check if the key already exists
    if key in set_dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    # Add the new configuration to the dictionary
    set_dictionary[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


# Function to update an existing setting
def update_setting(set_dictionary, set_tuple):
    # Unpack the tuple
    key, value = set_tuple

    # Convert key and value to lowercase
    key = key.lower()
    value = value.lower()

    # Verify if the setting exists
    if key in set_dictionary:
        # Update the setting value
        set_dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
   
    # If the setting does not exist
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


# Function to delete a setting
def delete_setting(set_dictionary, key):
    # Convert the key to lowercase
    key = key.lower()

    # Check if the key exists in the dictionary
    if key in set_dictionary:
        # Delete the setting
        del set_dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    
    # If the key is not in the dictionary
    return "Setting not found!"


# Function to display all settings
def view_settings(set_dictionary):
    # If the dictionary is empty
    if not set_dictionary:
        return "No settings available."
    
    # Create a list to store the output lines
    lines = ["Current User Settings:"]
    
    # Iterate through the dictionary and add each setting to the list
    for key, value in set_dictionary.items():
        lines.append(f"{key.capitalize()}: {value}")
    
    # Return the result as a single string with line breaks
    return "\n".join(lines) + "\n"

# Test dictionary with initial settings
test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}

# Function Testing:
# Add a new setting
print(add_setting(test_settings, ("Language", "Spanish")))

# Update an existing setting
print(update_setting(test_settings, ("Theme", "Light")))

# Delete a setting
print(delete_setting(test_settings, "Volume"))

# View all settings
print(view_settings(test_settings))                       

# Repeat tests to verify error messages (already exists / not found)
print(add_setting(test_settings, ("Language", "Spanish")))
print(update_setting(test_settings, ("Theme", "Light")))
print(delete_setting(test_settings, "Volume"))
print(view_settings(test_settings))
