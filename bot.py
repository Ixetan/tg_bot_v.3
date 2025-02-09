import asyncio
from aiogram import F, Bot, Dispatcher
from aiogram.filters.command import Command
from dotenv import dotenv_values

from menu import meal_container
from keyboards import menu_keybord

config = dotenv_values()

bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message, state): 
    await message.reply("Здраствуйте!", 
                        reply_markup=menu_keybord(meals_list=meal_container.get_all_name_names)
                        )

#    await state.set_state(OrderStates.choosing_meal)
#    await state.set_date({"total":0})

@dp.callback_query(F.data.startswith('meal_'))
async def test_callback(callback):
    date = callback.date.split('_')[-1]
    meal = meal_container.get_meal_by_id(int(date))
    await callback.message.reply(f'Вы заказали: {meal.name}')

async def main():
    await dp.start_polling(bot)
    
asyncio.run(main())