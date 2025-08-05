users = ["Toxir", "Sobir"]
print(users[0])

# --------------


def say_hello(name: str) -> str:
    return f"Assalomu alaykum {name}"


print(say_hello("Toxir"))


# -------------


class Car:
    def __init__(self, model: str, brand: str, price: int, color: str):
        self.model = model
        self.brand = brand
        self.price = price
        self.color = color

    def to_dict(self) -> dict:
        return self.__dict__


print("Bu faylda ish tugadi!!!")