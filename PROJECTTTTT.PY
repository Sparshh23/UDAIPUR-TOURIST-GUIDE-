
import time


places = {
    "City Palace": "A palace complex built over 400 years with impressive architecture and beautiful views of Lake Pichola.",
    "Lake Pichola": "A picturesque lake surrounded by hills and palaces. Boat rides available for visitors.",
    "Jagdish Temple": "A 17th-century Hindu temple with intricate carvings and stunning architecture.",
    "Fateh Sagar Lake": "A serene lake with three islands, perfect for boating and picnicking.",
    "Saheliyon Ki Bari": "A beautiful garden with fountains, lotus pools, and marble elephants.",
}


def display_places():
    print("\nPlaces to visit in Udaipur:")
    for place, description in places.items():
        print("- " + place + ": " + description)
    print()


display_places()

place = input("Enter the name of the place you want to visit: ")


if place in places:
    print("\nHere's some information about " + place + ":")
    print(places[place])
    print("\nEnjoy your visit to " + place + "!")
else:
    print("\nSorry, that place is not in the list. Please choose a place from the list.")
    display_places()

time.sleep(3)
print("\nThank you for using our tourist guide for Udaipur. Have a great day!")
