class Store:
    total_goods_sold = 0

    def __init__(self, name, num_goods_sold):
        self.name = name
        self.num_goods_sold = num_goods_sold
        Store.total_goods_sold += num_goods_sold

    #increase the amount of goods by specified value or by default = 1
    def increase_sales(self, number_goods = 1):
        self.num_goods_sold += number_goods
        Store.total_goods_sold += number_goods
        #return self.num_goods_sold

    #print the number of sold goods in the store
    def print_goods_sold(self):
        print(f'{self.name} - {self.num_goods_sold} goods sold')

    #print the total number of sold goods in all stores
    def print_total():
        print(f'Total sales in all stores - {Store.total_goods_sold}')



store1 = Store('shop1', 10)
store2 = Store('shop2', 12)

store1.increase_sales(8)
store1.increase_sales()
store2.increase_sales(10)
#print(store1.increase_sales())
store1.print_goods_sold()
store2.print_goods_sold()
print()
Store.print_total()