class pos:
    def __init__(self):
        self.product=[]
        self.customer=[]
        self.invoice=[]
        self.payment_history=[]

    def product_mgt(id,name,unit_price,qty):
        self.product.append({"id":id,"name":name,"unit_price":unit_price,"quantity":qty})
        return (f"product id {id}, {name}")
    
    def customer_mgt(cusid,gender,cusname,loyalty_pt,promotion,contactNo)
        self.customer.append({"id": cusid, "gender": gender, "name": cusname, "loyalty_points": loyalty_pt, "promotions": promotion, "contact_no": contactNo})
        return (f"customer id {cusid}, {cusname}")
    
#product input
id=input("Enter product id: ")
if id.isdigit():
    id=int(id)
name = input("Enter product name: ")
unit_price=input("Enter unit price")
if unit_price.replace(".","").isdigit():
    unit_price=float(unit_price)
qty=input("Enter quantity: ")
if qty.isdigit():
    qty=int(qty)

#customer input
cusid=input("Enter customer id: ")
if cusid.isdigit():
    cusid=int(cusid)
gender = input("Enter your gender: ")
cusname = input("Enter customer name: ")
loyalty_pt=input("Enter loyalty points: ")
if loyalty_pt.isdigit():
    loyalty_pt=int(loyalty_pt)
promotion=input("Enter promotion: ")
contactNo=input("Enter contact no: ")