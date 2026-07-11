import requests

def get_riddles():
    """Fetches a list of riddles from an external API."""
    response = requests.get("https://riddles-api.vercel.app/random")
    if response.status_code == 200:
        print(f"Riddles: ")
        return response.json()
    else:
        print("Failed to retrieve riddles. Please try again later.")

def main():
    """Main function to run the riddle fetching program."""
    print("Welcome to the Random Riddle Fetcher!")
    rid = get_riddles()

    while True:
        user_input = input("Would you like to fetch another riddle? (yes/no): ").strip().lower()
        if user_input == 'yes':
            print(rid)
        elif user_input == 'no':
            print("Thank you for using the Random Riddle Fetcher. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
if __name__ == "__main__":
    main()