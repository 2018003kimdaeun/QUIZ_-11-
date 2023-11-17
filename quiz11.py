class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

selected_beverage = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")

if selected_beverage in ["커피", "녹차", "아이스티"]:
    quantity = int(input("수량을 입력하세요: "))

    if selected_beverage == "커피":
        total_price = Coffee.calculate(quantity)
    elif selected_beverage == "녹차":
        total_price = GreenTea.calculate(quantity)
    elif selected_beverage == "아이스티":
        total_price = IceTea.calculate(quantity)

    print(f"{selected_beverage} {quantity}잔의 가격은 {total_price}원입니다.")
else:
    print("잘못된 음료입니다.")
