import locale
import platform
import pandas as pd

from pathlib import Path

if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')
else:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Seek Amazon CSV file and load to a Pandas dataframe
def seek_sheet():

    print("Welcome to the Amazon data analysis program!\n")
    while True:
        try:

            archive = Path(f"bestsellers with categories.csv")
            
            # Verify if the file exists in the current directory
            if not Path(archive).is_file():
                print(f"File '{archive}' not found. Please try again.")
                continue
            
            # Read the spreadsheet using Pandas
            df_base = pd.read_csv(archive, encoding = "UTF-8", sep = ",")
            print(f"File '{archive}' loaded successfully!")
            
            return df_base
        
        # Return error message if the file cannot be read
        except Exception as e:
            print(f"An error occurred while trying to read the file: {e}. Please try again.")

# Program boot message
def __initialyze():
    print(f"""--------------- Amazon Data Analysis ------------------

        Analysis of data from the best-selling books on Amazon
        Author - Paulo Izidoro
        Data -  {pd.Timestamp.now()}\n\n""")
    
# Look for the 20 books with most reviews
def __most_reviews(amazon_sheet):
    print("\n20 books with most reviews:")
    return(print(amazon_sheet[["Name", "Author", "Reviews", "Year", "Genre", "User Rating"]].drop_duplicates(subset=["Name", "Author"]).sort_values(by="Reviews", ascending=False).head(20).reset_index(drop=False)))

# Look for the top 10 authors with the most books    
def __prolific_authors(amazon_sheet):
    print("\n10 most prolific authors:")
    return(print(amazon_sheet[["Author", "Name"]].drop_duplicates(subset=["Name", "Author"]).groupby("Author")["Name"].count().sort_values(ascending=False).head(10).reset_index(drop=False)))

# Look for the top 25 books with best ratings
def __most_reviewed_books(amazon_sheet):
    print("\n25 books with best reviews:")    
    return(print(amazon_sheet[["Name", "Author", "Reviews", "Year", "Genre", "User Rating"]].groupby("Name")["User Rating"].mean().sort_values(ascending=False).head(25).reset_index(drop=False)))

# Look for the top 10 authors with best ratings
def __best_rated_authors(amazon_sheet):
    print("\n10 authors with the best ratings:")
    return(print(amazon_sheet.drop_duplicates(subset=["Name", "Author"]).groupby(["Author"])["User Rating"].mean().sort_values(ascending=False).head(10).reset_index(drop=False)))

# Start program
__initialyze()

amazon_sheet = seek_sheet()

__most_reviews(amazon_sheet)
__prolific_authors(amazon_sheet)
__most_reviewed_books(amazon_sheet)
__best_rated_authors(amazon_sheet)

print("\n\n--------------- End Program ------------------")
