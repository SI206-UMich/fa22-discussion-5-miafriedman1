import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == 'a' or i == 'A':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		print(self.items)
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = 0
		for x in self.items:
			if self.stock > max_stock:
				max_stock = self.stock
		return max_stock
		pass
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = 0
		for x in self.items:
			if self.price > max_price:
				max_price = self.get_max_price
		return max_price
		pass	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)
		self.warehouse1 = Warehouse([self.item1, self.item2, self.item3])

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("The dog jumped over the cat."), 1, "count_a 1 a")
		self.assertEqual(count_a("I love my mom."), 0, "count_a zero as")
		self.assertEqual(count_a("Anna Eagle is my best friend!"), 3, "count_a 3 as")
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.warehouse1.add_item(self.item4)
		self.assertEqual(len(self.warehouse1.items), 4, "testing add_item")
		self.warehouse1.add_item(self.item5)
		self.assertEqual(len(self.warehouse1.items), 5, "testing add_item")
		pass


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.assertEqual(self.get_max_stock(), 100, "testing get_max_stocks")
		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.assertEqual(self.get_max_price(), 6, "testing get_max_price")
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()