# Program to create a movie list from user input using list.append()

movies = []  # Empty list to store movie names

# Take movie names from the user
mov1 = input("Enter 1st movie name: ")
mov2 = input("Enter 2nd movie name: ")
mov3 = input("Enter 3rd movie name: ")

# Add each movie to the list using append()
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

# Display the final list of movies
print("movies =", movies)