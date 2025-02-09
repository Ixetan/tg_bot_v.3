from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from menu import meal_container

def menu_keybord(meals_list: list[str]):
    buillder = InlineKeyboardBuilder()

    for meal in meals_list:
        buillder.add(
            InlineKeyboardButton(text=meal, callable_data=f'meal_{meal_container.get_meal_by_name(meal).id}')
        )
    buillder.adjust(3)
    return buillder.as_markup()