# Q.10. Consider the following list of movies. For each movie it also shows list of ratings. Write a
# Python program to convert it in such a way that it stores all this data in one dictionary, then use
# the dictionary to print the average rating for each movie, rounded to one decimal.
# movies = ["Where Eagle’s Dare", "Enter the Dragon", "Iron Fist", "Fist of Fury"]
# dare_ratings = [ 9, 10, 9.5, 8.5, 3, 7.5, 8] for the movie “Where Eagle’s Dare”
# dragon_ratings = [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ] for the movie “Enter the Dragon”
# fist_ratings = [ 7, 6, 5 ] for the movie “Iron Fist”
# fury_ratings = [ 6, 5, 6, 6 ] for the movie “Fist of Fury”
# Output:
# Average ratings of the movie “Where Eagle’s Dare” is 7.9
# Average ratings of the movie “Enter the Dragon” is 6.9
# Average ratings of the movie “Iron Fist” is 6
# Average ratings of the movie “Fist of Fury” is 5.8

Movies = ["Where Eagle's Dare", "Enter the Dragon", "Iron Fist", "Fist of Fury"]
dare_rating = [9, 10, 9.5, 8.5, 3, 7.5, 8]
dragon_rating = [10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9]
fist_rating = [7, 6, 5]
fury_rating = [6, 5, 6, 6]
my_dictionary = {}
my_dictionary.update({Movies[0] : dare_rating})
my_dictionary.update({Movies[1] : dragon_rating})
my_dictionary.update({Movies[2] : fist_rating})
my_dictionary.update({Movies[3] : fury_rating})
for i in my_dictionary :
    temp_list = []
    rating = 0
    for j in my_dictionary[i] :
        temp_list.append(j)
        rating = sum(temp_list) / len(temp_list)
    print("Average ratings of the movie", '"', i, '" is', '%.1f'%rating)