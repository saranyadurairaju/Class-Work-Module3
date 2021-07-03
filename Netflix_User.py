import csv
import os

# Prompt user for video lookup
video_user = input("What show or movie are you looking for? ")

# Set path for file
file_to_open = os.path.join("Resources","netflix_ratings.csv")

# User Video detail
video_detail = []
#video_list = []
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
            video_detail.append([row[0],row[1],row[5]])
            #video_detail.append(row[1])
            #video_detail.append(row[5])
            #video_list.append(video_detail)
            video_found = True
            #print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])
    #Print video details or display Not found
    if video_found:
        print(video_detail)
    else:
        print("User video not found")
    for e in video_detail:
        if int(e[2]) > 70:
            print("Good Movie")
        else:
            print("Ok to watch once")
