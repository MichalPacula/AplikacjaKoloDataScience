import customtkinter as ctk
import pandas as pd

class application:
    def __init__(self):
        self.firstWindow()
    
    def firstWindow(self):
        df = pd.read_csv("IMDB_TOP_1000_Clean.csv")
        directorList = df.Director.values.tolist()
        global directorSet
        directorSet = set(directorList)
        actor1List = df.Star1.values.tolist()
        actor2List = df.Star2.values.tolist()
        actor3List = df.Star3.values.tolist()
        actorList = actor1List + actor2List + actor3List
        global actorSet
        actorSet = set(actorList)

        global genreList
        genreList = ["None", "action", "comedy", "fantasy"]
        #creating window
        self.root = ctk.CTk()
        self.root.title("Movie predictor")
        self.root.geometry("500x500")

        #creating first page
        self.firstPage = ctk.CTkFrame(self.root)

        #text before choosing director
        self.directorLabel = ctk.CTkLabel(self.firstPage, text="Choose director you want in your movie")
        self.directorLabel.pack()

        #creating dropdown menu for directors
        selDirector = ctk.StringVar()
        self.directorMenu = ctk.CTkComboBox(self.firstPage, values=directorSet, variable=selDirector)
        self.directorMenu.pack()
        selDirector.trace("w", self.updateDirector)

        #shows number of directors found
        self.directorResult = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(directorSet)))
        self.directorResult.pack()

        #text before choosing first actor
        self.actor1Label = ctk.CTkLabel(self.firstPage, text="Choose first actor in your movie")
        self.actor1Label.pack()

        #creating dropdown menu for first actor
        selActor1 = ctk.StringVar()
        self.actor1Menu = ctk.CTkComboBox(self.firstPage, values=actorSet, variable=selActor1)
        self.actor1Menu.pack()
        selActor1.trace("w", self.updateActor1)

        #shows number of first actors found
        self.actor1Result = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(actorSet)))
        self.actor1Result.pack()

        #text before choosing second actor
        self.actor2Label = ctk.CTkLabel(self.firstPage, text="Choose second actor in your movie")
        self.actor2Label.pack()

        #creating dropdown menu for second actor
        selActor2 = ctk.StringVar()
        self.actor2Menu = ctk.CTkComboBox(self.firstPage, values=actorSet, variable=selActor2)
        self.actor2Menu.pack()
        selActor2.trace("w", self.updateActor2)

        #shows number of second actor found
        self.actor2Result = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(actorSet)))
        self.actor2Result.pack()

        #text before choosing third actor
        self.actor3Label = ctk.CTkLabel(self.firstPage, text="Choose third actor in your movie")
        self.actor3Label.pack()

        #creating dropdown menu for third actor
        selActor3 = ctk.StringVar()
        self.actor3Menu = ctk.CTkComboBox(self.firstPage, values=actorSet, variable=selActor3)
        self.actor3Menu.pack()
        selActor3.trace("w", self.updateActor3)

        #shows number of third actor found
        self.actor3Result = ctk.CTkLabel(self.firstPage, text="Number of records: " + str(len(actorSet)))
        self.actor3Result.pack()

        #text before choosing genre
        self.genreLabel = ctk.CTkLabel(self.firstPage, text="Choose genre of your movie")
        self.genreLabel.pack()

        #creating dropdown menu for genre
        selGenre = ctk.StringVar()
        self.genreMenu = ctk.CTkComboBox(self.firstPage, values=genreList, variable=selGenre)
        self.genreMenu.pack()
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

        self.firstPage.pack()

        self.root.mainloop()

    def updateDirector(self, *args):
        listDirectorNew = []
        for i in directorSet:
            if self.directorMenu.get() in i:
                listDirectorNew.append(i)
        self.directorMenu.configure(values=listDirectorNew)
        self.directorResult.configure(text="Number of records: " + str(len(listDirectorNew)))

    def updateActor1(self, *args):
        listActorNew = []
        for i in actorSet:
            if self.actor1Menu.get() in i:
                listActorNew.append(i)
        self.actor1Menu.configure(values=listActorNew)
        self.actor1Result.configure(text="Number of records: " + str(len(listActorNew)))

    def updateActor2(self, *args):
        listActorNew = []
        for i in actorSet:
            if self.actor2Menu.get() in i:
                listActorNew.append(i)
        self.actor2Menu.configure(values=listActorNew)
        self.actor2Result.configure(text="Number of records: " + str(len(listActorNew)))
    
    def updateActor3(self, *args):
        listActorNew = []
        for i in actorSet:
            if self.actor3Menu.get() in i:
                listActorNew.append(i)
        self.actor3Menu.configure(values=listActorNew)
        self.actor3Result.configure(text="Number of records: " + str(len(listActorNew)))
    
    def updateGenre(self, *args):
        listGenreNew = []
        for i in genreList:
            if self.genreMenu.get() in i:
                listGenreNew.append(i)
        self.genreMenu.configure(values=listGenreNew)
        self.genreResult.configure(text="Number of records: " + str(len(listGenreNew)))
    
        

application()