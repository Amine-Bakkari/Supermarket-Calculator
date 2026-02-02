from customtkinter import *
from sqlite3 import *

yc = 0
ArticleVerification = str()
PriceToShow = 0
PriceWithoutTVAToShow = 0
TVAToShow = 0


Main = CTk()
Main.geometry("400x500")
Main.title("Calculateur De Prix")
Main.resizable(False, False)

EntryFrame = CTkFrame(Main, width=370, height=100)
EntryFrame.place(x=15, y=10)

ArticleEntry = CTkEntry(EntryFrame, width=200, placeholder_text="Entrer L'Article")
ArticleEntry.place(x=45, y=10)

NombreArticle = CTkEntry(EntryFrame, width=70, placeholder_text="Combien")
NombreArticle.place(x=255, y=10)

def CalculatingHandling():
    global yc, PriceToShow, PriceWithoutTVAToShow, TVAToShow, ArticleVerification
    ArticleName = ArticleEntry.get()
    try: 
        ArticleNumber = int(NombreArticle.get())
    except ValueError:
        ArticleNumber = 1
    
    DBFile = connect(r"C:\Users\Abdelaziz\OneDrive\Desktop\Rayane-Haouzi-Abdelaziz-Amine-Bakkari-Martil\ArticlesDataBase.db")
    cursor = DBFile.cursor()
    DataBase = cursor.execute("SELECT * FROM articles")
    for article in DataBase:
        if article[0] == ArticleName:
            ArticleVerification = article[0]
            PriceToShow += article[1] * ArticleNumber
            PriceWithoutTVAToShow += article[2] * ArticleNumber
            TVAToShow += article[3] * ArticleNumber
            ResultOfTotal.configure(text=PriceToShow)
            ResultOfTotalPricesWithoutTVA.configure(text=round(PriceWithoutTVAToShow, 4))
            ResultOfTotalTVA.configure(text=round(TVAToShow, 4))
            if ArticleNumber > 1:
                CTkLabel(ArticleNameFrame, text=(f"{ArticleNumber}x {article[0]}")).place(x=10, y=yc)
            else:
                CTkLabel(ArticleNameFrame, text=article[0]).place(x=10, y=yc)
            
            CTkLabel(ArticlePriceFrame, text=round(article[2]*ArticleNumber, 4)).place(x=30, y=yc)
            CTkLabel(ArticleTVAFrame, text=round(article[3]*ArticleNumber, 4)).place(x=30, y=yc)
            yc += 20
    if not ArticleVerification:
        ErrorLabel.configure(text="L'article n'est pas trouvé")
    DBFile.commit()
    DBFile.close()

def key(event):
    event = event.char
    if event == "\r":
        CalculatingHandling()


Main.bind("<Key>", key)


ArticleSubmitButton = CTkButton(EntryFrame, text="Submit", width=60, command=CalculatingHandling)
ArticleSubmitButton.place(x=155, y=60)

ErrorLabel = CTkLabel(EntryFrame, text="", text_color="red", font=("Arial", 12))
ErrorLabel.place(x=230, y=60)

CalculatingFrame = CTkFrame(Main, width=370, height=330)
CalculatingFrame.place(x=15, y=120)

ArticleName = CTkLabel(CalculatingFrame, text="Article:", font=("Arial", 11))
ArticleName.place(x=70, y=0)

ArticlePrice = CTkLabel(CalculatingFrame, text="Prix Sans TVA:", font=("Arial", 11))
ArticlePrice.place(x=195, y=0)

ArticleTVA = CTkLabel(CalculatingFrame, text="TVA:", font=("Arial", 11))
ArticleTVA.place(x=305, y=0)


ArticleNameFrame = CTkFrame(CalculatingFrame, width=170, height=300)
ArticleNameFrame.place(x=10, y=20)

ArticlePriceFrame = CTkFrame(CalculatingFrame, width=80, height=300)
ArticlePriceFrame.place(x=190, y=20)

ArticleTVAFrame = CTkFrame(CalculatingFrame, width=80, height=300)
ArticleTVAFrame.place(x=280, y=20)

TotalPriceFrame = CTkFrame(Main, width=370, height=30)
TotalPriceFrame.place(x=15, y=460)

TotalPriceLabel = CTkLabel(TotalPriceFrame, text="Total:")
TotalPriceLabel.place(x=10, y=2)

ResultOfTotal = CTkLabel(TotalPriceFrame, text=PriceToShow)
ResultOfTotal.place(x=100, y=2)
DhsLabel = CTkLabel(TotalPriceFrame, text="Dhs")
DhsLabel.place(x=150, y=2)

ResultOfTotalPricesWithoutTVA = CTkLabel(TotalPriceFrame, text=PriceWithoutTVAToShow)
ResultOfTotalPricesWithoutTVA.place(x=210, y=2)
DhsLabel2 = CTkLabel(TotalPriceFrame, text="Dhs")
DhsLabel2.place(x=245, y=2)

ResultOfTotalTVA = CTkLabel(TotalPriceFrame, text=TVAToShow)
ResultOfTotalTVA.place(x=310, y=2)
DhsLabel3 = CTkLabel(TotalPriceFrame, text="Dhs")
DhsLabel3.place(x=335, y=2)

Main.mainloop()