from config import token
from aiogram import Bot, Dispatcher, executor, types
from crypto import Scraper
from aiogram.dispatcher.filters import Text


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ["BTC", "BNB", "ADA",
                     "DOGE", "ETH", "LTC",
                     "XMR", "CAKE", "SHIB",
                     "SOL", "TRX", "XRP"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer(f"Bot successfully started...\n",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals='BTC'))
async def coin_1(message: types.Message):
    bitcoin = Scraper('bitcoin')
    bitcoin.scraper()
    bitcoin.output()

    with open('file.txt', 'r') as file:
        btc = file.read()
        file.close()

    await message.answer(btc)


@dp.message_handler(Text(equals='BNB'))
async def coin_2(message: types.Message):
    bnb_coin = Scraper('bnb')
    bnb_coin.scraper()
    bnb_coin.output()

    with open('file.txt', 'r') as file:
        bnb = file.read()
        file.close()

    await message.answer(bnb)


@dp.message_handler(Text(equals='ADA'))
async def coin_3(message: types.Message):
    cardano = Scraper('cardano')
    cardano.scraper()
    cardano.output()

    with open('file.txt', 'r') as file:
        ada = file.read()
        file.close()

    await message.answer(ada)


@dp.message_handler(Text(equals='DOGE'))
async def coin_4(message: types.Message):
    dogecoin = Scraper('dogecoin')
    dogecoin.scraper()
    dogecoin.output()

    with open('file.txt', 'r') as file:
        doge = file.read()
        file.close()

    await message.answer(doge)


@dp.message_handler(Text(equals='ETH'))
async def coin_5(message: types.Message):
    ethereum = Scraper('ethereum')
    ethereum.scraper()
    ethereum.output()

    with open('file.txt', 'r') as file:
        eth = file.read()
        file.close()

    await message.answer(eth)


@dp.message_handler(Text(equals='LTC'))
async def coin_6(message: types.Message):
    litecoin = Scraper('litecoin')
    litecoin.scraper()
    litecoin.output()

    with open('file.txt', 'r') as file:
        ltc = file.read()
        file.close()

    await message.answer(ltc)


@dp.message_handler(Text(equals='XMR'))
async def coin_7(message: types.Message):
    monero = Scraper('monero')
    monero.scraper()
    monero.output()

    with open('file.txt', 'r') as file:
        xmr = file.read()
        file.close()

    await message.answer(xmr)


@dp.message_handler(Text(equals='CAKE'))
async def coin_8(message: types.Message):
    pancakeswap = Scraper('pancakeswap')
    pancakeswap.scraper()
    pancakeswap.output()

    with open('file.txt', 'r') as file:
        cake = file.read()
        file.close()

    await message.answer(cake)


@dp.message_handler(Text(equals='SHIB'))
async def coin_9(message: types.Message):
    shiba_inu = Scraper('shiba-inu')
    shiba_inu.scraper()
    shiba_inu.output()

    with open('file.txt', 'r') as file:
        shib = file.read()
        file.close()

    await message.answer(shib)


@dp.message_handler(Text(equals='SOL'))
async def coin_10(message: types.Message):
    solana = Scraper('solana')
    solana.scraper()
    solana.output()

    with open('file.txt', 'r') as file:
        sol = file.read()
        file.close()

    await message.answer(sol)


@dp.message_handler(Text(equals='TRX'))
async def coin_11(message: types.Message):
    tron = Scraper('tron')
    tron.scraper()
    tron.output()

    with open('file.txt', 'r') as file:
        trx = file.read()
        file.close()

    await message.answer(trx)


@dp.message_handler(Text(equals='XRP'))
async def coin_12(message: types.Message):
    xrp_coin = Scraper('xrp')
    xrp_coin.scraper()
    xrp_coin.output()

    with open('file.txt', 'r') as file:
        xrp = file.read()
        file.close()

    await message.answer(xrp)


if __name__ == '__main__':
    executor.start_polling(dp)
