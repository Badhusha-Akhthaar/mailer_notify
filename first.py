from urllib.request import urlopen
import urllib
import requests
import cssutils
import sys
from bs4 import BeautifulSoup
import pyrebase
config = {
    "apiKey": "xxxxxxxxxxxxxxxxxxxxx",
    "authDomain": "xxxxx.firebaseapp.com",
    "databaseURL": "https://xxxx.firebaseio.com",
    "projectId": "xxxxx",
    "storageBucket": "xxxxx.appspot.com",
    "messagingSenderId": "998321xxxxx"
  }
firebase=pyrebase.initialize_app(config)
db=firebase.database()
class FoodFetch:
    global soup
    global title
    url_main=input("Paste Url Here..")
    if "www.allrecipes.com" not in url_main:
        sys.exit("Not a valid URL...")
    source=requests.get(url_main).text
    soup=BeautifulSoup(source,'lxml')
    title=soup.find('h1',{"class":"recipe-summary__h1"}).text ##This gets the title of recipe
    data={"dishName": title}
    db.child('users').child(title).set(data)
    def ingredient(self):
        contents=soup.find_all('ul',{"class":"dropdownwrapper"})
        for content in contents:
            lsts=content.find_all('li',{"class":"checkList__line"})
            for lst in lsts:
                try:
                    itm=lst.find('span',{"class":"recipe-ingred_txt added"}).text
                    ing={"ingredient": itm}
                    db.child("users").child(title).child("ingredients").push(ing)
                except AttributeError:
                    continue

    def making(self):
        tils=soup.find('ol',{"class":"list-numbers recipe-directions__list"})
        liss=tils.find_all('li',{"class":"step"})
        for li in liss:
            span=li.find('span',{"class":"recipe-directions__list--item"}).text
            steps={"steps": span}
            db.child("users").child(title).child("method").push(steps)


    def img_ret(self):
        img_item=soup.find('ul',{"class":"photo-strip__items"})
        img_lis=img_item.find('li')
        img_a=img_lis.img['src']
        imgs_url={"imgUrl": img_a}
        db.child("users").child(title).child("image").push(imgs_url)
        print("Done")

sc_obj=FoodFetch()
sc_obj.ingredient()
sc_obj.making()
sc_obj.img_ret()
