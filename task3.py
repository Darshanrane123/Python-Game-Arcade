# Sample dataset of movies with their genres
movies = {
    'Movie1': {'Genre': ['Action' , 'Adventure'] , 'Rating': 4.5} ,
    'Movie2': {'Genre': ['Comedy' , 'Romance'] , 'Rating': 3.8} ,
    'Movie3': {'Genre': ['Drama' , 'Romance'] , 'Rating': 4.2} ,
    'Movie4': {'Genre': ['Action' , 'Sci-Fi'] , 'Rating': 4.0} ,
    'Movie5': {'Genre': ['Comedy' , 'Family'] , 'Rating': 3.9} ,
}


# Function to recommend movies to a user based on genre similarity
def recommend_movies(user_preference , movie , num_recommendations=3):
    # Step 1: Calculate similarity between user preferences and each movie
    recommendations = []
    for movie in movies:
        movie_genre = movies[movie]['Genre']
        similarity = len ( set ( user_preferences ).intersection ( movie_genre ) ) / float ( len ( user_preferences ) )
        recommendations.append ( (movie , similarity) )

    # Step 2: Sort movies by similarity
    recommendations = sorted ( recommendations , key = lambda x: x[1] , reverse = True )

    # Step 3: Get top recommendations
    top_recommendations = [movie for movie , _ in recommendations[:num_recommendations]]

    return top_recommendations


# Example usage
user_preferences = [input("Hello! Please Enter your preferences for Movies (eg,,Action, Adventure, etc ) :- ")]


recommended_movies = recommend_movies ( user_preferences , movies )
print ( f"Recommended movies based on user preferences: {recommended_movies}" )
