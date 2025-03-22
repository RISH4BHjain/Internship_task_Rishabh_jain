news_feed = []


#adding news
def add_news():
    title = input("Enter News Title: ")
    details = input("Enter News details: ")
    photo_path = input("Enter Photo path or URL: ")
    
    news_feed.append({
        "title": title,
        "details": details,
        "photo": photo_path
    })
    print("News added successfully!\n")


#List news
def list_news():
    if not news_feed:
        print("No news available.\n")
    else:
        print("\nNews Feed:")
        for idx, news in enumerate(news_feed, 1):
            print(f"{idx}. Title: {news['title']}")
            print(f"   Details: {news['details']}")
            print(f"   Photo: {news['photo']}\n")


#choices to select (user options)
def main():
    while True:
        print("Select your choice:")
        print("1. Add news details")
        print("2. List news")
        print("3. Exit app")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_news()
        elif choice == "2":
            list_news()

#exiting the app (break)            
        elif choice == "3":
            print("Exiting application... Goodbye!!")
            break
        else:
            print("Invalid choice, please try again.\n")


main()

