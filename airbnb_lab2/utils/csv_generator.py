import csv, os, random
from datetime import date, timedelta

def generate_csv(n=1000):
    os.makedirs('data', exist_ok=True)

    # Users
    with open('data/users.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name','email','password'])
        writer.writeheader()
        for i in range(n):
            writer.writerow({'name':f'User{i}','email':f'user{i}@example.com','password':'123456'})

    # Housing
    with open('data/housing.csv','w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['address','price','rooms'])
        writer.writeheader()
        for i in range(n):
            writer.writerow({'address':f'Address{i}','price':random.randint(20,500),'rooms':random.randint(1,5)})

    # Bookings
    with open('data/bookings.csv','w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['user_id','housing_id','status'])
        writer.writeheader()
        for i in range(n):
            writer.writerow({'user_id':random.randint(1,n),'housing_id':random.randint(1,n),'status':'pending'})

    # Payments
    with open('data/payments.csv','w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['booking_id','amount','status'])
        writer.writeheader()
        for i in range(n):
            writer.writerow({'booking_id':random.randint(1,n),'amount':random.randint(50,1000),'status':'unpaid'})

if __name__ == "__main__":
    generate_csv()
    print("CSV файли згенеровані у папці data/")