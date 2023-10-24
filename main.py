# untuk membuat table
from tabulate import tabulate

# square root, untuk menghitung euclidean distance
from math import sqrt

class Membership:
    
    # inisialisasi data
    data = {
        "Sumbul" : "Platinum",
        "Ana" : "Gold",
        "Cahya" : "Platinum" 
    }
    
    # inisialisai attribute
    def __init__(self, username):
        self.username = username
        
    # method untuk menampilkan benefit membership
    def show_benefit(self):
        headers = ["Membership", "Discount", "Another Benefit"]
        
        table = [
            ["Platinum", "15%", "Benefit Gold + Silver + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
            ["Silver", "8%", "Voucher Makanan"]
        ]
        
        print("Benefit Tier Membership PacCommerce")
        print("")
        print(tabulate(table, headers = headers, tablefmt = "github"))
        
    # method untuk menampilkan requirements membership
    def show_requirements(self):
        headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]

        table = [
            ["Platinum", "8", "15"],
            ["Gold", "6", "10"],
            ["Silver", "5", "7"]
        ]
        
        print("Requirement Benefit Tier Membership PacCommerce")
        print("")
        print(tabulate(table, headers = headers, tablefmt = "github"))
        
    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance
    def predict_membership(self, username, 
                           monthly_expense, 
                           monthly_income):
    
        res = []
        
        parameter_reference = [[8, 15], [6, 10], [5, 7]]
        
        for index, _ in enumerate (parameter_reference):
            euclidean_distance =  round(sqrt((monthly_expense - parameter_reference[index][0]) ** 2 + \
                                       (monthly_income -  parameter_reference[index][1]) ** 2), 2)
            res.append(euclidean_distance)
                                       
        res_dict = {
            "Platinum" : res[0],
            "Gold" : res[1],
            "Silver" : res[2],
        }
        
        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {res_dict}")
        
        for member, distance in res_dict.items():
            if distance == min(res):
                self.data[username] = member
                return member
    
    # method untuk menampilkan membership yang dimiliki
    # dari database yang dimiliki
    def show_membership(self, username):
        if username in self.data:
            return self.data.get(username)
    
    # method untuk menghitung final price berdasarkan membership
    def calculate_price(self, username, list_harga):
        try:
            if username in self.data:
                membership = self.data.get(username)
                
                if membership == "Platinum":
                    final_price = sum(list_harga) - (sum(list_harga) * 0.15)
                    return final_price
                
                elif membership == "Gold":
                    final_price = sum(list_harga) - (sum(list_harga) * 0.10)
                    return final_price
                
                elif membership == "Silver":
                    final_price = sum(list_harga) - (sum(list_harga) * 0.08)
                    return final_price
                
                else:
                    raise Exception("Membership tidak tersedia")
                    
            else:
                raise Exception("Username tidak ada di Database")
                
        except:
            raise Exception("Invalid Process")
        
new_instance = Membership(username = "Ghifari")

#new_instance.show_benefit()

#new_instance.show_requirements()
                
res_predict = new_instance.predict_membership(username = new_instance.username, 
                                  monthly_expense = 9,
                                  monthly_income = 12)

print(res_predict)

print(new_instance.data)

res_price = new_instance.calculate_price(username = new_instance.username,
                             list_harga = [150_000, 200_000, 400_000])

print(res_price)