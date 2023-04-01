import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import pandas as pd

class application:
    def __init__(self):
        self.firstPageCreator()
    
    #method which creates first page in the window
    def firstPageCreator(self):
        #getting data to the dataframe
        df = pd.read_csv("IMDB_TOP_1000_Clean.csv")

        #creating global directorList and inserting in it all the directors and "None"
        global directorList
        directorList = df.Director.values.tolist()
        directorList = list(set(directorList))
        directorList.insert(0, "None")

        #creating global actorList and inserting in it all the actors and "None"
        actor1List = df.Star1.values.tolist()
        actor2List = df.Star2.values.tolist()
        actor3List = df.Star3.values.tolist()
        global actorList
        actorList = actor1List + actor2List + actor3List
        actorList = list(set(actorList))
        actorList.insert(0, "None")

        #creating global genreList and inserting in it all the genres and "None"
        global genreList
        genreList = []
        genreBadList = df.Genre.tolist()

        #for loop to split all the genres, because one movie can have few genres
        for i in range(0, len(genreBadList) - 1):
            listSeparated = []
            listSeparated = genreBadList[i].split(", ")
            genreList += listSeparated
        genreList = list(set(genreList))
        genreList.insert(0, "None")

        #creating window
        self.root = ctk.CTk()
        self.root.title("Movie predictor")
        self.root.geometry("600x600")

        #creating first page
        self.firstPage = ctk.CTkFrame(self.root)

        #text before choosing director
        self.directorLabel = ctk.CTkLabel(self.firstPage, text="Choose director you want in your movie")
        self.directorLabel.pack()

        #creating dropdown menu for directors
        selDirector = ctk.StringVar()
        self.directorMenu = ctk.CTkComboBox(self.firstPage, values=directorList, variable=selDirector)
        self.directorMenu.pack()
        self.directorMenu.set("None")

        #checking if user types anything in the directorMenu and calling updateDirector method if he did
        selDirector.trace("w", self.updateDirector)

        #shows number of directors found
        self.directorResult = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(directorList)))
        self.directorResult.pack()

        #text before choosing first actor
        self.actor1Label = ctk.CTkLabel(self.firstPage, text="Choose first actor in your movie")
        self.actor1Label.pack()

        #creating dropdown menu for first actor
        selActor1 = ctk.StringVar()
        self.actor1Menu = ctk.CTkComboBox(self.firstPage, values=actorList, variable=selActor1)
        self.actor1Menu.pack()
        self.actor1Menu.set("None")

        #checking if user types anything in the actor1Menu and calling updateActor1 method if he did
        selActor1.trace("w", self.updateActor1)

        #shows number of first actors found
        self.actor1Result = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(actorList)))
        self.actor1Result.pack()

        #text before choosing second actor
        self.actor2Label = ctk.CTkLabel(self.firstPage, text="Choose second actor in your movie")
        self.actor2Label.pack()

        #creating dropdown menu for second actor
        selActor2 = ctk.StringVar()
        self.actor2Menu = ctk.CTkComboBox(self.firstPage, values=actorList, variable=selActor2)
        self.actor2Menu.pack()
        self.actor2Menu.set("None")

        #checking if user types anything in the actor2Menu and calling updateActor2 method if he did
        selActor2.trace("w", self.updateActor2)

        #shows number of second actor found
        self.actor2Result = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(actorList)))
        self.actor2Result.pack()

        #text before choosing third actor
        self.actor3Label = ctk.CTkLabel(self.firstPage, text="Choose third actor in your movie")
        self.actor3Label.pack()

        #creating dropdown menu for third actor
        selActor3 = ctk.StringVar()
        self.actor3Menu = ctk.CTkComboBox(self.firstPage, values=actorList, variable=selActor3)
        self.actor3Menu.pack()
        self.actor3Menu.set("None")

        #checking if user types anything in the actor3Menu and calling updateActor3 method if he did
        selActor3.trace("w", self.updateActor3)

        #shows number of third actor found
        self.actor3Result = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(actorList)))
        self.actor3Result.pack()

        #text before choosing genre
        self.genreLabel = ctk.CTkLabel(self.firstPage, text="Choose genre of your movie")
        self.genreLabel.pack()

        #creating dropdown menu for genre
        selGenre = ctk.StringVar()
        self.genreMenu = ctk.CTkComboBox(self.firstPage, values=genreList, variable=selGenre)
        self.genreMenu.pack()
        self.genreMenu.set("None")

        #checking if user types anything in the genreMenu and calling updateGenre method if he did
        selGenre.trace("w", self.updateGenre)

        #shows number of genres found
        self.genreResult = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(genreList)))
        self.genreResult.pack()

        #text before typing budget
        self.budgetLabel = ctk.CTkLabel(self.firstPage, text="Type what budget do you have for your movie")
        self.budgetLabel.pack()

        #creating textbox for budget
        self.budgetText = ctk.CTkTextbox(self.firstPage, height=1, font=("Arial", 13))
        self.budgetText.pack()

        #creating button, which creates second page
        self.nextPageButton = ctk.CTkButton(self.firstPage, text="Continue", command=self.secondPage)
        self.nextPageButton.pack(pady=10)

        self.firstPage.pack()

        self.root.mainloop()

    #method that creates second page
    def secondPageCreator(self):
        #creating second page
        self.secondPage = ctk.CTkFrame(self.root)


        self.secondPage.pack()

    #method that creates new listDirectorNew list and gets all values from directorList that have string which user typed
    def updateDirector(self, *args):
        listDirectorNew = []
        for i in directorList:
            if self.directorMenu.get().lower() in i.lower():
                listDirectorNew.append(i)
        self.directorMenu.configure(values=listDirectorNew)
        self.directorResult.configure(text="Number of records: " + str(len(listDirectorNew)))

    #method that creates new listActorNew list and gets all values from ActorList that have string which user typed
    def updateActor1(self, *args):
        listActorNew = []
        for i in actorList:
            if self.actor1Menu.get().lower() in i.lower():
                listActorNew.append(i)
        self.actor1Menu.configure(values=listActorNew)
        self.actor1Result.configure(text="Number of records: " + str(len(listActorNew)))

    #method that creates new listActorNew list and gets all values from ActorList that have string which user typed
    def updateActor2(self, *args):
        listActorNew = []
        for i in actorList:
            if self.actor2Menu.get().lower() in i.lower():
                listActorNew.append(i)
        self.actor2Menu.configure(values=listActorNew)
        self.actor2Result.configure(text="Number of records: " + str(len(listActorNew)))
    
    #method that creates new listActorNew list and gets all values from ActorList that have string which user typed
    def updateActor3(self, *args):
        listActorNew = []
        for i in actorList:
            if self.actor3Menu.get().lower() in i.lower():
                listActorNew.append(i)
        self.actor3Menu.configure(values=listActorNew)
        self.actor3Result.configure(text="Number of records: " + str(len(listActorNew)))
    
    #method that creates new listGenreNew list and gets all values from genreList that have string which user typed
    def updateGenre(self, *args):
        listGenreNew = []
        for i in genreList:
            if self.genreMenu.get().lower() in i.lower():
                listGenreNew.append(i)
        self.genreMenu.configure(values=listGenreNew)
        self.genreResult.configure(text="Number of records: " + str(len(listGenreNew)))
    
    #method that checks if user gave all information and then destroys first page and creates second page
    def secondPage(self):
        if self.directorMenu.get().strip() != "" and self.directorMenu.get().strip() != "None" and self.actor1Menu.get().strip() != "" and self.actor1Menu.get().strip() != "None" and self.actor2Menu.get().strip() != "" and self.actor2Menu.get().strip() != "None" and self.actor3Menu.get().strip() != "" and self.actor3Menu.get().strip() != "None" and self.genreMenu.get().strip() != "" and self.genreMenu.get().strip() != "None" and self.budgetText.get("1.0", "end").strip() != "":
            try:
                self.firstPage.destroy()
                self.secondPageCreator()
            except:
                CTkMessagebox(title="Error!", message="There was an error! Please try again!")
        else:
            CTkMessagebox(title="Error!", message="You didn't insert enough information!")
        
    
        

application()