def add_setting(dictionary, key_value_pair):
    key, value = key_value_pair
    key = key.lower()
    value = value.lower()

    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dictionary, key_value_pair):
    key, value = key_value_pair
    key = key.lower()
    value = value.lower()

    if key in dictionary:
        dictionary.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(dictionary, key):
    key = key.lower()

    if key in dictionary:
        dictionary.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(dictionary):
    if not dictionary:
        return "No settings available."
    else:
        key_value = "Current User Settings:\n"

        for key, value in dictionary.items():
            key = key.capitalize()
            key_value += f"{key}: {value}\n"

        return key_value


# --------------------------------
# TESTING
# --------------------------------

test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}


print("===== ADD SETTING =====")

print(add_setting(test_settings, ("volume", "high")))

print(add_setting(test_settings, ("THEME", "light")))


print("\n===== UPDATE SETTING =====")

print(update_setting(test_settings, ("THEME", "light")))

print(update_setting(test_settings, ("timezone", "utc")))


print("\n===== DELETE SETTING =====")

print(delete_setting(test_settings, "LANGUAGE"))

print(delete_setting(test_settings, "username"))


print("\n===== VIEW SETTINGS =====")

print(view_settings(test_settings))


print("\n===== EMPTY SETTINGS =====")

empty_settings = {}

print(view_settings(empty_settings))


print("\n===== FINAL DICTIONARY =====")

print(test_settings)