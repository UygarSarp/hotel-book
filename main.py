import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def name(self):
        ava = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        return ava

    def available(self):
        ava = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if ava == "yes":
            return True
        else:
            return False

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


class Ticket:
    def __init__(self, name, hotel_object):
        self.name = name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
Thank you for your reservation!
Here is your data:
Name: {self.name}
Hotel name: {self.hotel.name()}
"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def dogrula(self, exp, cvc, holder):
        dic = {"number": self.number, "expiration": exp, "cvc": cvc, "holder": holder}
        if dic in df_cards:
            return True


class Security(CreditCard):
    def check(self, password):
        ava = df_security.loc[df_security["number"] == self.number, "password"].squeeze()
        if ava == password:
            return True


class Spa(Ticket):
    def generate(self):
        content = f"""
    Thank you for SPA your reservation!
    Here is your data:
    Name: {self.name}
    Hotel name: {self.hotel.name()}
    """
        return print(content)


print(df)
hotel_i = input("Enter the hotel id: ")
hotel = Hotel(hotel_i)
if hotel.available():
    credit = input("Enter your credit card number ")
    credit_card = CreditCard(credit)
    cvc = input("Enter your cvc: ")
    exp = input("Enter your exp: ")
    hold = input("Enter card holders name: ")
    if credit_card.dogrula(exp, cvc, hold):
        password = input("Enter your password: ")
        sec = Security(credit)
        if sec.check(password):
            name = input("Enter your name: ")
            ticket = Ticket(name, hotel)
            hotel.book()
            print(ticket.generate())
        else:
            print("Your password is incorrect")
    else:
        print("Your card information is wrong.")
else:
    print("Hotel is not available.")

cvp = input("Do you want spa?")
if cvp == "yes":
    spa = Spa(name, hotel)
    spa.generate()
