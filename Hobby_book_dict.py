# Info in Dictionaries
pet_dict = {"name": "Bob",
            "age": 5,
            "hobby": ["barking","playing","eating","running","sleeping"],
            "wake_up": {"mon": 7, "Tue": 6, "Wed": 9}
            }

##Print
print(f"Hello I am {pet_dict['name']} and I am a {pet_dict['age']} years old")
print(f"I have {len(pet_dict['hobby'])} hobbies")
print(f"One of my favorite hobby is {pet_dict['hobby'][1]}")
print(f"On Tuesday, I get up at {pet_dict['wake_up']['Tue']} AM.")
