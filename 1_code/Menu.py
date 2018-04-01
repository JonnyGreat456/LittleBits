# -*- coding: utf-8 -*-
from flask import Flask, render_template
menu={}
itemList=[]
class IngredientItem:
	name=""
	Quantity=0
	Measure=""
	#measure lbs weight and gallons in fluids
	def __init__(self,name,Quantity,Measure):
		self.name=name
		self.Quantity=Quantity
		self.Measure=Measure

	def displayItem(self):
		print(self.name,self.Quantity,self.Measure)


class MenuItem:
	name=""
	price=0.00
	ratings=[]
	ingredients=[]
	menuItem=[]

	def __init__(self,name,price,ratings,ingredients):
		round(price,2)
		self.name=name
		self.price=price
		self.ratings=ratings
		self.ingredients=ingredients
	def addRating(self,rating):
		self.ratings.append(rating)
	

def addIngredientItem(name,quantity,unitOfMeasure):
	if quantity<0 or name=="" or unitOfMeasure=="" or name==None or unitOfMeasure==None:
		print("invalid inputted values")
		return False
	temp=[]
	temp.append(name)
	temp.append(quantity)
	temp.append(unitOfMeasure)
	ingredients.append(temp)
	return True

#sample menu created
# menu{ "Entrees" : [MenuItem]} #MenuItem will contain
Entrees={
	"Pizza" : [12.00,[4.0,3.9,3.8,4.1],[]],
	"Penne Vodka" : [16.49,[5.0,4.9],[]],
	"Eggplant Parm" : [11.99,[3.0,2.9],[]]
}
Appetizer={
	"Calamari" : [12.00,[4.1,3.3,3.2,4.1],[]],
	"Bruschetta" : [7.99,[None],[]],
	"Tortellini" : [8.50,[4.2,4.0,2.8,2.9],[]]
}
Dessert={
	"Tiramisu" : [6.50,[4.0,4.9,3.9,4.1],[]],
	"Gelato" : [5.00,[4.5,3.9,4.8,4.6],[]],
}

def addMenuItem(category,itemName,itemPrice,ingredientName,ingredientQuantity,unitOfMeasurement): #add item to menu given what category it falls under, name,price of food, and ingridient attributes
	if category==None or itemName=="" or itemPrice==None or itemName==None or ingredientName=="" or ingredientQuantity<0 or unitOfMeasurement=="":
 		print("All fields do not have values inputted")
 		return False
	elif itemPrice<0:
 		print("price is less than 0.00")
 		return False

	round(itemPrice,2)
	ratings=[]
	ingredients=[]	#list of ingredients
	ingredients.append(ingredientName)
	ingredients.append(ingredientQuantity)
	ingredients.append(unitOfMeasurement)	
	temp_list=[]
	temp_list.append(itemName)
	temp_list.append(itemPrice)
	temp_list.append(ratings)
	temp_list.append(ingredients)
	#ingredients=[]
	#print(category,itemName,price)
	menuItem=temp_list
	itemList.append(menuItem)
	menu[category]=itemList	
	#menuItem.append(MenuItem(itemName,itemPrice)) #empty list of ratings
	print(itemName,"has been added")
	return True

def deleteMenuItem(category,itemName):#delete item from menu
	if category==None or itemName==None:
	 	print("All fields do not have values inputted")
	 	return False
	if category in menu.keys():
		for item in menu[category]:
			if item[0]==itemName:
				menu[category].remove(item)
				print(itemName, "deleted")
				return True
	else:			
		print(category,"does not exist")
		return False
	print(itemName, "does not exist in",category, "category")
	return False

def editPrice(category,itemName,itemPrice): #edit price of menu item
	round(itemPrice,2)
	if category==None or itemName==None or itemPrice==None:
	 	print("All fields do not have values inputted")
 		return False
	elif itemPrice<0:
 		print("price is less than 0.00")
 		return False
	if category in menu.keys():
		for item in menu[category]:
			if item[0]==itemName:
				item[1]=itemPrice
				print(itemName,"price changed")
				return True
	else:			
		print(category,"does not exist")
		return False
	print(itemName,"does not exist in",category,"category")
	return False	

def addRating(category,itemName): #give a menu item from a specific category a rating
	comma=","
	if category==None or itemName==None:
	 	print("All fields do not have values inputted")
 		return False
	if category in menu.keys():	
		rating=float(input("Enter a rating from 0 to 5: ")) #if running on Python 2.x.x then change input to raw_input
		if(rating<0 or rating> 5):
			while(rating<0 or rating>5):
				if(rating<0):
					print("invalid input")
					rating=float(input("Enter a rating from 0 to 5: ")) #if running on Python 2.x.x then change input to raw_input
				elif(rating>5):
					print("rating greater than maximum allowed number")
					rating=float(input("Enter a rating from 0 to 5: ")) #if running on Python 2.x.x then change input to raw_input
				else:
					break
		#add rating to corresponding food item

		rating=round(rating,1)
		rating=str(rating)		
		for item in menu[category]:
			if item[0]==itemName:
				item[2].append(rating)
				ratingList=comma.join(item[2])
				del item[2][:]
				item[2].append(ratingList)
				print("Thank you")
				return True
	else:
		print(category,"does not exist")
		return False
	print(itemName,"does not exist")
	return False
	
def AverageRating(category,itemName):#returns average of ratings for a given menu item
	if category==None or itemName==None:
	 	print("All fields do not have values inputted")
 		return False
	if category in menu.keys():	
		total=0 #Initialize total
		counter=0 #count how many ratings there are
		for item in menu[category]:
			if item[0]==itemName: #found the name that ratings will correspond to
				wordSplit=[]
				wordSplit=item[2][0].split(',')
				del item[2][:]
				item[2]=wordSplit
				for rating in item[2]:
					rating=float(rating)
					rating=round(rating,1)
					counter+=1
					total+=rating
				avgRating=total/counter
				avgRating=round(avgRating,1)
				return avgRating	
		print(itemName,"does not exist in",category)
		print("Therefore average can not be computed")
		return			
	print(category,"does not exist in the menu")
	print("Therefore average can not be computed")
	return

def createFirstMenuSection(category,itemName,price,ingredientName,QuantityofIngredient,unitOfMeasure): #initializes menu so use this when starting from empty menu{}
	if category==None or price<0 or itemName=="" or ingredientName=="" or QuantityofIngredient<0 or unitOfMeasure=="":
		print("error no category inputted or price is less an 0.00")
		return False
	elif price<0:
 		print("price is less than 0.00")
 		return False	
	round(price,2)
	menuItem=[]
	global ratings
	ingredients=[]
	ingredients.append(ingredientName)
	ingredients.append(QuantityofIngredient)
	ingredients.append(unitOfMeasure)
	menuItem=[]
	ratings=MenuItem.ratings
	ingredients=MenuItem.ingredients
	temp_list=[]
	temp_list.append(itemName)
	temp_list.append(price)
	temp_list.append(ratings)
	temp_list.append(ingredients)
	#ingredients=[]
	menuItem=temp_list
	itemList=[]
	itemList.append(menuItem)
	menu[category]=itemList
	print("Menu initalized use addMenuItem to add the rest of menu items and sections")
	return category

#use createFirstMenuSection with the right parameters
createFirstMenuSection("Soup","French Onion",8.50,"Yellow Onion",1,"lbs")
print("Menu",menu)
addRating("Soup","French Onion")
addRating("Soup","French Onion")
addRating("Soup","French Onion")
print("menu:",menu)
print(AverageRating("Soup","French Onion"))

# addMenuItem("Entrees","Chicken Nuggets",12.50,"Frozen Chicken Nuggets",2.0,"lbs")
# addMenuItem("Entrees","Penne Vodka",16.55,"Pasta",2,"lbs")
# addMenuItem("Entrees","Pizza",12.00,"Flour",1,"lbs")
# addMenuItem("Soup","New England Clam Chowder",7.50,"Clams",0.5,"lbs")
# deleteMenuItem("Soup","French Onion")
# editPrice("Entrees","Penne Vodka",12.49)
# print("Menu",menu) #to see edited price
# addRating("Entrees","Penne Vodka")
# print(menu['Entrees']) #to see inital rating inputted
# addRating("Entrees","Penne Vodka")
# addRating("Entrees","Pizza")
# addRating("Entrees","Chicken Parm")
# print("menu:",menu)
# print(AverageRating("Entrees","Penne Vodka"))
