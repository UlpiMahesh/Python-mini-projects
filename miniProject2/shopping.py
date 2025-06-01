##################################################### Shopping cart mini project #######################################################


class Products:
    def __init__(self):
        self.available_products=['Laptop', 'Headphones', 'Samsungs22', 'Shirt', 'Pant', 'Apple', 'Banana', 'Papaya']
        self.prices = [40000,3000,82000,600,1200,50,10,60]
        self.cart={}


products = Products()
def addToCart():
    try:
        print(f'''Available products to Add to cart :
                         1. Laptop - 1N = 40000
                         2. Headphones - 1N = 3000
                         3. SamsungS22 - 1N = 82000
                         4. Shirt - 1N = 600
                         5. Pant - 1N = 1200
                         6. Apple - 1N = 50
                         7. Banana - 1N = 10
                         8. Papaya - 1N = 60''')
        product_choice=int(input('Enter the product number from above :'))
        assert product_choice>0 and product_choice <9, 'You have seleted an unavailable product. Please select available products only '
        product_selected = products.available_products[product_choice-1]
        if product_choice:
            quantity = int(input('Enter the product quantity:'))
            
        
        if product_choice<6:
            if product_choice==1 or product_choice==3:
                # 
                q = products.cart.get(product_selected,[0])[0]+quantity
                products.cart[product_selected]=[q,'Warrenty: 12 months',products.prices[product_choice-1]]
                print(f'Last added product to cart  {products.available_products[product_choice-1]} - ${products.prices[product_choice-1]}, {products.cart[product_selected][1]}, quantity - {quantity}')
                
            elif product_choice==2:
                q = products.cart.get(product_selected,[0])[0]+quantity
                products.cart[product_selected]=[q,'Warrenty: 6 months',products.prices[product_choice-1]]
                print(f'Last added product to cart  {products.available_products[product_choice-1]} - ${products.prices[product_choice-1]}, {products.cart[product_selected][1]}, quantity - {quantity}')
                
            else:
                q = products.cart.get(product_selected,[0])[0]+quantity
                
                products.cart[product_selected]=[q,products.prices[product_choice-1]]
                print(f'Last added product to cart  {products.available_products[product_choice-1]} - ${products.prices[product_choice-1]}, quantity - {quantity}')
                
        elif product_choice>=6:
            products.cart[product_selected]=[products.cart.get(product_selected,0) + quantity,'Expiry Date: 2024-04-30',products.prices[product_choice-1]]
            print(f'Last added product to cart  {products.available_products[product_choice-1]} - ${products.prices[product_choice-1]}, {products.cart[product_selected][1]}, quantity - {quantity}')
            
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(e)


def removeItem():
    try:
        choice = input('Enter the product name you want to remove: ')
        if products.cart.get(choice,'na')!='na':
            products.cart.pop(choice)
            print(f'{choice} removed from the cart')
        else:
            print('Item is not avaiable in cart')
    except Exception as e:
        print(e)

     
def viewCart():
    if products.cart=={}:
        print('Cart is empty please add items to cart to view cart.')
    else:
        try:
            print(f'Items in your cart:')
            for k,v in products.cart.items():
                print(f'{k} -  ${v[-1]},{v[1]}, x {v[0]} ')
        except Exception as e:
            print(e)


def updateProduct():
    viewCart()
    choice=input('Enter name of the product you want to update: ')
    if products.cart.get(choice,'na') !='na':
        quantity = int(input('Enter new quantity: '))
        product = products.cart.get(choice)
        product[0]=quantity
        products.cart[choice]=product
        print(f'Quantity of {choice} updated to {quantity}')
    else:
        print(f'{choice} not avaiable in your cart. do you want to add product to cart: yes/no')
        n_choice = input().lower()
        assert n_choice=='yes' or n_choice=='no', 'invalid choice'
        if n_choice=='yes':
            addToCart()
import re
def placeOrder():
    try:
        if len(products.cart)==0:
            print('No items added to cart. Please add items to cart to place order.')
        else:
            name = input('Enter your name: ')
            match = re.match(r'[A-Za-z]*_?\s?[A-Za-z]*',name)
            if match:
                phone = input('Enter your phone number')
                match = re.match(r'\d{10}',phone)
                if match:
                    file = input('Enter the filename for the invoice (e.g., invoice): ')
                    file_path = file+'.txt'
                    with open(file_path,'w') as myfile:
                        for k,v in products.cart.items():
                            cont ='product: ' +k+' Quantity: '+str(v[0])+' '+v[1]+' Total price: '+ str(v[-1]*v[0])
                            myfile.write(cont)
                            
                        
                            
                        # [3, 'Warrenty: 12 months', 82000]
                    print(f'Placing an order\nInvoice generated and saved to {file}.txt\nCart cleared.')
                    clearCart()

            else:
                print('invalid name!\nPlease enter your name only and alphabets and can use one underscore inbetween if required.')
                placeOrder()
                
    except Exception as e:
        print(e)
    

def clearCart():
    try:
        if len(products.cart)==0:
            print('Cart is already empty.')
        else:
            products.cart.clear()
    except Exception as e:
        print(e)
        

if __name__ == '__main__':
    try:
    
        while True:
            print('''-----------------------> Start the shopping <---------------------
                         1. Add item to cart
                         2. Remove item from cart
                         3. View cart
                         4. Update item quantity
                         5. Clear cart
                         6. Place order
                         7. Exit''')
            choice = int(input('Enter your choice:'))
            assert choice<=7 and choice>0, 'You have selected an invalid choice.\nCart is cleared please try again with avaliable options.'
            if choice==1:
                addToCart()
            elif choice==2:
                removeItem()
            elif choice==3:
                viewCart()
            elif choice==4:
                updateProduct()
            elif choice==5:
                clearCart()
            elif choice==6:
                placeOrder()
            elif choice==7:
                print('Logging off thank you. Visit Again!')
                break
            
    except AssertionError as e:
        print(str(e))
        
    