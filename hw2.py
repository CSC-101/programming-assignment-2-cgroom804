from operator import index
from typing import Optional

import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: data.Point, p2: data.Point) -> data.Rectangle: #arguments p1 & p2 are expected to take the values of class Point, and the function is expected to return a Rectangle object
    if p1.x <= p2.x: #finds the smallest and largest x co-ordinate, and assigns them to their corresponding point
        tl_x = p1.x
        br_x = p2.x
    else:
        tl_x = p2.x
        br_x = p1.x
    if p1.y <= p2.y: #finds the smallest and largest y co-ordinate, and assigns them to their corresponding point
        tl_y = p2.y
        br_y = p1.y
    else:
        tl_y = p1.y
        br_y = p2.y

    top_left = data.Point(tl_x, tl_y) #takes the lowest x and highest y co-ordinates to create the top left point
    bottom_right = data.Point(br_x, br_y) #takes the highest x and lowest y co-ordinates to create the top bottom right
    return data.Rectangle(top_left, bottom_right) #creates a Rectangle object from the top_left and bottom_right points

# Part 2
def shorter_duration_than(t1: data.Duration, t2: data.Duration) -> bool:
    #arguments t1 and t2 are expected to take the values of the class Duration, and the function is expected to return a bool
    if t1.minutes == t2.minutes: #if t1's minutes are less than t2's or if they are equal but t1's seconds are less than
        # t2's, then it returns True, otherwise False
        if t1.seconds < t2.seconds:
            return True
        else:
            return False
    elif t1.minutes < t2.minutes:
        return True
    else:
        return False

# Part 3
def song_shorter_than(songs:list[data.Song], time: data.Duration) -> list[data.Song]:
    #argument songs is expected to be a list that takes the values of the class Song while the argument
    #time is expected to be a list that takes on the value of the class Duration, and the function is
    #expected to return a list that takes the values of the class Song
    song_list =[] #creates an empty list for the songs under the desired time
    for i in songs: #repeats for all songs in the songs list
        if shorter_duration_than(i.duration, time) is True: #tests each song if it's shorter than the requirement
            song_list.append(i) #adds it to the song_list if it's true
    return song_list #returns song_list

# Part 4
def running_time(songs: list[data.Song], nums: list[int]) -> data.Duration:
    # argument songs is expected to be a list that takes the values of the class Song while the argument
    # nums is expected to be a list of integers, and the function is
    # expected to return an instanced object of the class Duration
    seconds = 0 #creates the variable seconds
    minutes = 0 #creates the variable minutes

    for num in nums: #repeats for every number in the list nums
        song_time = songs[num].duration #the variable song time will be assigned the length of the song selected
        if song_time.seconds >= 0 and song_time.minutes >= 0: #if the song is within the range
            seconds += song_time.seconds #add its seconds to the total of seconds
            minutes += song_time.minutes #add its minutes to the total of seconds
    return data.Duration(minutes + seconds // 60, seconds % 60) #create an instance of the class Duration for the total length of the songs

# Part 5
def validate_route(links: list[list[str]], path: list[str]) -> bool:
    # argument links is expected to be a list of lists that take on the values of a string while the argument
    # path is expected to be a list of strings, and the function is expected to return a bool
    if len(path) == 1 or len(path) == 0: #paths of 0 or 1 are valid, therefore True
        return True

    for n in range(len(path) - 1): #repeats for the total strings in path
        link1 = [path[n], path[n + 1]] #creates a variable for the required link between two locations
        link2 = [path[n+1], path[n]] #creates a variable for the opposite

        if link1 in links or link2 in links: #if either of the variables are in the list of links
            return True #returns true
        else:
            return False #otherwise, returns false

# Part 6
def longest_repetition(nums: list[int]) -> Optional[int]:
    #the argument nums is expected to take on the value of a list containing integers
    longest = 1 #creates a variable for the longest length of repeating numbers
    index = 0 #the index at the beginning of the repeating numbers

    for i in range(len(nums) - 1): #repeats for all the numbers in the list
        new_index = i #creates a new index for every iteration
        new_length = 1 #creates a new length for every iteration
        while i + 1 < len(nums) and nums[i] == nums[i + 1]: #while there's still a follow-up number in the list, and it is the same as the current number:
            new_length += 1 #add 1 to new length
            i += 1 #move on to the next number in the list
        if new_length > longest: #if the new_length is longer than the current longest length, than replace longest and index
            longest = new_length
            index = new_index
    return index #returns the index at which the longest repetition of numbers begins