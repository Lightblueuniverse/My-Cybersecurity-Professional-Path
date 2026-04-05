# User Configuration Manager

This project is a user settings manager developed in Python. The tool allows users to manage personal preferences (such as themes, languages, and notifications) using dictionaries and tuples, while applying validations to ensure data integrity.

## 🚀 Features

* **Settings CRUD:** Complete functionality to Create, Read, Update, and Delete user settings.
* **Data Normalization:** Implementation of lowercase conversion (`.lower()`) to prevent duplicates caused by capitalization differences.
* **Error Handling:** Informative messages provided when a setting already exists or when attempting to modify a non-existent entry.
* **Formatted Visualization:** Clean, capitalized output of current configurations to enhance user experience.

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Data Structures:**
    * **Dictionaries:** For efficient storage and lookups.
    * **Tuples:** For structured parameter passing.

## 📂 Code Structure

The system is built around four core functions:

1.  **`add_setting(dict, tuple)`**: Unpacks a tuple and adds a new setting after verifying it doesn't already exist.
2.  **`update_setting(dict, tuple)`**: Modifies the value of an existing key.
3.  **`delete_setting(dict, key)`**: Safely removes an entry from the dictionary.
4.  **`view_settings(dict)`**: Iterates through the structure and returns a human-readable summary.

---

Developed as a practical implementation of Python data structures.
