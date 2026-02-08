class pos:
    def __init__(self):
        self.product=[]
        self.customer=[]
        self.invoice=[]
        self.payment_history=[]

    def product_mgt(self,id,name,unit_price,qty):
        self.product.append({"id":id,"name":name,"unit_price":unit_price,"quantity":qty})
        return (f"product id {id}, {name}")
    
    def customer_mgt(self,cusid,gender,cusname,loyalty_pt,promotion,contactNo):
        self.customer.append({"id": cusid, "gender": gender, "name": cusname, "loyalty_points": loyalty_pt, "promotions": promotion, "contact_no": contactNo})
        return (f"customer id {cusid}, {cusname}")
    
    def invoice_mgt(self,invoiceNo,cusid,datePurchased,amt,totalPrice):
        self.invoice.append({"invoiceNo":invoiceNo,"customer_id":cusid,"date":datePurchased,"amount":amt,"total_price":totalPrice})
        return (f"invoice {invoiceNo} created")
    
    def pmt_mgt(self,cusid,invoiceNo):
        self.payment_history.append({"customer_id":cusid,"invoiceNo":invoiceNo})
        return (f"payment recorded for {invoiceNo}")
    
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