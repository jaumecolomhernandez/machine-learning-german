import ClassApp
import ClassDatabase

if __name__ == "__main__":
    
    #location of the csv file and the database
    csv_url = "data.csv"
    db_url = "data.db"

    #Create an app a db and an UI object
    db = ClassDatabase.Database(csv_url, db_url)
    UI = "UI"
    app = ClassApp.App(db, UI)
    
    app.start_game()


