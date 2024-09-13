import pandas as pd
from sklearn.metrics import pairwise_distances

# Load data
movies = pd.read_csv('movies.csv')
ratings_movies = pd.read_csv('ratings.csv')
books = pd.read_csv('books.csv')
ratings_books = pd.read_csv('bratings.csv')

# Create user-item matrices
def create_user_item_matrix(ratings, item_col):
    return ratings.pivot_table(index='userId', columns=item_col, values='rating', fill_value=0)

user_item_matrix_movies = create_user_item_matrix(ratings_movies, 'movieId')
user_item_matrix_books = create_user_item_matrix(ratings_books, 'bookId')

# Compute user similarity matrix
def compute_user_similarity(user_item_matrix):
    similarity = 1 - pairwise_distances(user_item_matrix, metric='cosine')
    return pd.DataFrame(similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

user_similarity_movies = compute_user_similarity(user_item_matrix_movies)
user_similarity_books = compute_user_similarity(user_item_matrix_books)

# Generic recommendation function
def get_recommendations(user_id, user_item_matrix, user_similarity_df, items_df, item_col, num_recommendations=5):
    user_ratings = user_item_matrix.loc[user_id]
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).drop(user_id)
    similar_users_ratings = user_item_matrix.loc[similar_users.index]
    
    # Compute weighted sum of ratings
    weighted_sum = (similar_users_ratings.T @ similar_users).sort_values(ascending=False)
    
    # Filter out already rated items
    already_rated_items = user_ratings[user_ratings > 0].index
    recommended_items = weighted_sum.drop(already_rated_items)
    
    # Get top recommendations
    top_recommendations = recommended_items.head(num_recommendations)
    top_titles = items_df[items_df[item_col].isin(top_recommendations.index)]['title']
    
    return top_titles

# Movie recommendations
def get_movie_recommendations(user_id, num_recommendations=5):
    return get_recommendations(
        user_id, user_item_matrix_movies, user_similarity_movies, movies, 'movieId', num_recommendations
    )

# Book recommendations
def get_book_recommendations(user_id, num_recommendations=5):
    return get_recommendations(
        user_id, user_item_matrix_books, user_similarity_books, books, 'bookId', num_recommendations
    )

# Main function
def main():
    user_id = int(input("Enter user ID: "))
    while True:
        choice = input("Enter 'M' for movie recommendations, 'B' for book recommendations, or 'Q' to quit: ").upper()
        if choice == 'M':
            recommendations = get_movie_recommendations(user_id)
            print(f"Movie Recommendations for User {user_id}:")
        elif choice == 'B':
            recommendations = get_book_recommendations(user_id)
            print(f"Book Recommendations for User {user_id}:")
        elif choice == 'Q':
            break  
        else:
            print("Invalid choice. Please enter 'M' for movie recommendations, 'B' for book recommendations, or 'Q' to quit.")

        for i, title in enumerate(recommendations, 1):
            print(f"{i}. {title}")

if __name__ == "__main__":
    main()
