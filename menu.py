class Meal:
    def __init__(self, price: int,
                 ingredients: list[str],
                 name: str,
                 description: str):
        self.price = price
        self.ingredients = ingredients
        self.name = name
        self.description = description
    
    def __str__(self):
        result = f'Название: {self.name}\n'
        result += 'Ингредиенты:\n'
        for ingredient in self.ingredients:
            result += f'\t-{ingredient}\n'
        result += f'Цена: {self.price} рублей\n'
        result += f'Описание: {self.description}\n\n'
        return result
   
class MealContainer:
    def __init__(self, meals: list[Meal]):
        self.meals = meals

    def write_to_file(self):
        f = open('meals.txt', 'w+', encoding='utf-8')
        f.write('Блюда:\n')
        for meal in self.meals:
            f.write(str(meal))
        f.close()

kurica = Meal(price=300,
              ingredients=["Курица",
                           "Панировка",
                           "Специи"],
              name="Курица",
              description="Обычная курица, обжаренная в панировке.")

potato = Meal(price=200,
              ingredients=["Картошка",
                           "Масло",],
              name="Картошка",
              description="Обычная картошка, обжаренная в масле.")

sauce = Meal(price=50,
              ingredients=["Кетчуп"],
              name="Соус",
              description="Обычный кетчуп.")

meal_container = MealContainer(meals=[kurica, potato, sauce])
meal_container.write_to_file()