from classes import *
def test_open_exhibition():
    # Create a museum
    louvre = Museum("Louvre", "Abu Dhabi")

    # Create an exhibition
    impressionist_exhibition = Exhibition("Impressionist Art Exhibition", "3 months", "Exhibition Hall")

    # Open the exhibition at the museum
    louvre.open_exhibition(impressionist_exhibition)

    # Retrieve the newly opened exhibition
    opened_exhibition = louvre.get_exhibitions()[-1]  # Assuming the latest exhibition is the one just opened

    # Print information about the newly opened exhibition
    print("New Exhibition Opened:")
    print("Name:", opened_exhibition.get_name())
    print("Duration:", opened_exhibition.get_duration())
    print("Location:", opened_exhibition.get_location())



if __name__ == "__main__":
    test_open_exhibition()
    print("Test case passed: New exhibition at the museum.")
