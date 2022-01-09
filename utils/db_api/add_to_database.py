import asyncio

from utils.db_api.database import create_db
from utils.db_api.db_commands import add_service


async def add_services():
    await add_service(name="Huobi",
                      category_name="Биржи", category_code="Stock",
                      photo="-",
                      link="https://www.huobi.com/ru-ru/topic/double-invite/register/?invite_code=2yzb3223&name=Balder&avatar=3",
                      short_description="абузим прайм пулы",
                      description="Тут советики, как регать, нытьё, что выбить норм рефку надо долбить поддержку")
    await add_service(name="FTX",
                      category_name="Биржи", category_code="Stock",
                      photo="-",
                      link="https://ftx.com/#a=64884075",
                      short_description="вроде комса на вывод меньше",
                      description="Надо самому узнать, как выводить без комсы, а то я так и не понял")
    await add_service(name="KuCoin",
                      category_name="Биржи", category_code="Stock",
                      photo="-",
                      link="https://www.kucoin.com/land/register/r/r3KQ7DC",
                      short_description="что оно тут делает?",
                      description="Мало ли кому пригодится")
    await add_service(name="Biswap",
                      category_name="Биржи", category_code="Stock",
                      photo="-",
                      link="https://biswap.org/?ref=c5b0edcb3bf1030a7c3e",
                      short_description="серп не одобряет",
                      description="Рефка норм, лучше не найдёте")
    await add_service(name="ProxyLine",
                      category_name="Прокси", category_code="Proxy",
                      photo="-",
                      link="https://proxyline.net?ref=89625",
                      short_description="серп одобряет",
                      description="Пусто, не юзал")
    await add_service(name="ProxySeller",
                      category_name="Прокси", category_code="Proxy",
                      photo="-",
                      link="https://proxy-seller.ru/?partner=N8M41FdJAPxV0A",
                      short_description="максимка одобряет",
                      description="Пусто, не юзал")
    await add_service(name="WebShare",
                      category_name="Прокси", category_code="Proxy",
                      photo="-",
                      link="https://www.webshare.io/?referral_code=il8nnqkd0w7t",
                      short_description="инфа из чатика",
                      description="Пусто, не юзал")
    await add_service(name="Dolphin",
                      category_name="Антики", category_code="AntiB",
                      photo="-",
                      link="https://anty.dolphin.ru.com/a/61655",
                      short_description="люблю дельфинов",
                      description="Красивый дизайн")
    await add_service(name="AdsPower",
                      category_name="Антики", category_code="AntiB",
                      photo="-",
                      link="https://anty.dolphin.ru.com/a/61655",
                      short_description="максимка одобряет",
                      description="Не крсивый дизайн, но максимка говорит топ")
    await add_service(name="Дешёвые дискорды",
                      category_name="Купить аккаунты", category_code="Accs",
                      photo="-",
                      link="http://saimedo.ru/ru/?cat=19152",
                      short_description="сайт 2007ого",
                      description="7/12 улетело на вериф телефона, но реально дешево")
    await add_service(name="Пожилые твиттеры",
                      category_name="Купить аккаунты", category_code="Accs",
                      photo="-",
                      link="https://trust-accs.ru/",
                      short_description="из чатика",
                      description="Пусто, не юзал")
    await add_service(name="SocPuplic",
                      category_name="Сервисы абузера", category_code="AbuzS",
                      photo="-",
                      link="https://www.youtube.com/",
                      short_description="меня забанило",
                      description="Поставлю норм ссылки")
    await add_service(name="!OneDash!",
                      category_name="Сервисы абузера", category_code="AbuzS",
                      photo="-",
                      link="https://ds-onedash.ru/r/960fa2",
                      short_description="ставить аккуратно",
                      description="ГАЙД НА ПЕСОЧНИЦУ https://remontka.pro/sandbox-windows-10/")
    await add_service(name="SMS-activate",
                      category_name="Сервисы абузера", category_code="AbuzS",
                      photo="-",
                      link="https://sms-activate.org/?ref=1744428",
                      short_description="популярно",
                      description="тут рефочка есть))")
    await add_service(name="CheapSMS",
                      category_name="Сервисы абузера", category_code="AbuzS",
                      photo="-",
                      link="https://cheapsms.ru/#",
                      short_description="мне понравился",
                      description="Норм")



