import requests
import math
import tokens

def main():
    
    # Get desired number of movies to display
    number = get_number_movies()

    # Getting title key word question
    title_search = input("\nWhat movie title would like to search for? ")

    # Making call to our api with number of pages 
    titles = api_call(number, title_search)

    # Print number of pages (take each title in titles from beginning up until number)
    for title in titles[:number]:

        # Making sure it isn't final message
        if not ("There are only " and "movies that fit the criteria...") in title:
            # Printing index ot title, then title
            print("\n", titles.index(title)+1, ". ", title, sep = "")
        else:
            print("\n", title, sep="")


    # Choosing which movie (based on index)
    movie_choice = chose_movie(len(titles))

    print("\n", titles[movie_choice-1], ' ?\n' , sep="")
    


# Defininng the API call function with input number of pages
def api_call(n_movies, title):

    # Get headers 
    headers = {
        "accept": "application/json", 
        "Authorization": tokens.api_key    
        }

    # Setting amount of pages required (since 20 movies per page and round up to have next page even if all not necessary)
    pages = math.ceil(n_movies / 20)

    # Endpoint setting
    url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page="

    # Initiate movies list and n_call
    movies = []
    n_call = 1

    # Making the calls range from 1 (since can't use pages 0), to pages+1 since no 0 to equilibrate
    while True:

        # Adding the number of the page to the URL for each run 
        url_final = url + str(n_call)

        # Making the API call
        response = requests.get(url_final, headers=headers).json()

        # Taking a look at structure to build functions if function not called in main (this script)
        # import json
        # print(json.dumps(response, indent=4))

            # Isolating the element each results under the key results 
        for result in response["results"]:
                
            # Condition is title not already in list
            if str(result["original_title"]) not in movies :

                # Appending the titles in each result
                movies.append(str(result["original_title"]))

                # Condition if number of movies in list is not already equal to max
                if len(movies) == n_movies:
                    return movies


        # Condition if page of results isn't equal to or above max number of pages
        if response["page"] >= response["total_pages"]:
                    
            # Then add an element saying sorry we only have X elements
            movies.append(f"There are only {len(movies)} movies that fit the criteria...")
            return movies

        # n_call is for looping and changing 
        n_call += 1


# Function to get initial length of list
def get_number_movies():

    # Making an infinite loop to force integer
    while True:
        
        # Asking number of pages to choose from
        number_movies = input("\nHow many movies would you like to see in our list? ")
        
        # Error handling in case converting to int is issue due to number containing text (eg insert "asdf")
        try:
            number_movies = int(number_movies)

        except ValueError:
            print("\nPlease insert a number")

        # Checking that number is above 1
        if type(number_movies) == int:
            if number_movies >= 1:
                return number_movies
            else:
                print("\nInsert a number at least equal to 1")


# Make function to chose movie
def chose_movie(max):

    # Making an infinite loop to force integer
    while True:
        
        # Asking number of pages to choose from
        number_movies = input("\nWhich number you be more interested in? ")
        
        # Error handling in case converting to int is issue due to number containing text (eg insert "asdf")
        try:
            number_movies = int(number_movies)

        except ValueError:
            print("\nPlease insert a number")

        # Checking that number is above 1
        if type(number_movies) == int:
            if number_movies >= 1 and number_movies <= max:
                return number_movies
            elif number_movies < 1:
                print("\nInsert a number at least equal to 1")
            else:
                print("\nPlease insert a number that is on the screen")




if __name__ == "__main__":
    main()