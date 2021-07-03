import csv
import os

# Prompt user for video lookup
video_user = input("What show or movie are you looking for? ")

# Set path for file
file_to_open = os.path.join("Resources","netflix_ratings.csv")

# User Video detail
video_detail = []
video_found = False

# Open the CSV
with open(file_to_open) as netflix_data:
    file_reader = csv.reader(netflix_data)

    # Read the header row.
    headers = next(file_reader)

    # Loop through looking for the video.
    for row in file_reader:
        if video_user == row[0]:
            #video_title = row[0]
            video_detail.append(row[0])
            video_detail.append(row[1])
            video_detail.append(row[6])
            video_found = True
            break
    #Print video details or display Not found
    if video_found:
        print(video_detail)
    else:
        print("User video not found")
    