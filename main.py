def p1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто с 10:00')

    newRestaurant = Restaurant(input('Введите название ресторана: '), input('Введите тип кухни: '))
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    print('\n')


def p3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто!')

        def write_rating(self):
            print(f'Бывший рейтинг: {self.rating}')
            self.rating = input('Обновлённое значение: ')
            print(f'Обновлено: {self.rating}')

    newRestaurant = Restaurant('Невский Берег', 'русская', '5')
    newRestaurant.write_rating()


p1()
p3()