from aiogram import types

from keyboards.inline.menu_keyboards import menu_keyboard, menu_cd, info_keyboard
from loader import dp


async def list_menu(callback: types.CallbackQuery, lang, **kwargs):
    markup = await menu_keyboard(lang)
    if lang == "ru":
        text = "абоба"
    else:
        text = "aboba"
    await callback.message.edit_text(text, reply_markup=markup)


async def show_info(callback: types.CallbackQuery,info, lang):
    markup = info_keyboard(lang)
    if lang == "ru":
        match info:
            case "motivation":
                text = '''<b>Мотивация для создания Axelar</b>
                Команда Акселар увидела большую проблему для системы, которая, будет становиться все более актуальной в последствии. В частности, тенденцию к тому, что для разработчиков создавалось все больше и больше быстрых и безопасных цепочек, и хотя некоторые разработчики хотели бы делать что-то на основе этих платформ… Они ещё и хотели бы получить доступ к ликвидности с возможностью компоновки других существующих экосистем, таких как Bitcoin и Ethereum. Потребность в масштабируемой межсетевой связи будет только расти по мере того, как развивается человечество. Поэтому Сергей Горбунов и соучредитель Georgios решили начать новое предприятие для решения этой проблемы.
                '''
            case "trouble":
                text = '''<b>Какие проблемы решает Axelar?</b>
                Мы определенно входим в мир мультисетей, поэтому видим, что сетей становится всё больше, а стоимость запуска новой понижается. В этом мире мобильность активов и обмен информацией между сетями становятся все более важными.
На чем Axelar сосредоточен, так это на создании децентрализованного стека для решения этой проблемы и соединения различных разнородных блокчейнов, которые говорят на разных языках, имеют разные правила консенсуса и поддерживают разные языки смарт-контрактов. Акселар создает единую децентрализованную сеть и стек протоколов для подключения и объединения различных приложений и платформ во всех этих экосистемах.
                '''
    else:
        match info:
            case "motivation":
                text = '''<b>Motivation for creating Axelar</b>
                The Axelar team saw a big problem for the system, which will become more and more relevant in the future. In particular, the trend towards more and more fast and secure chains for developers, and while some developers would like to build on these platforms… They also want to access liquidity with the ability to link other existing ecosystems , such as Bitcoin and Ethereum. The need for scalable interconnection will only grow as humanity evolves. Therefore, Sergey Gorbunov and co-founder Georgios decided to start a new venture to solve this problem.
                        '''
            case "trouble":
                text = '''<b>What problems does Axelar solve?</b>
                We are definitely entering the world of multi-networks, so we see more and more networks, and the cost of launching a new one is going down. In this world, the mobility of assets and the exchange of information between networks are becoming increasingly important. What Axelar is focusing on is building a decentralized stack to solve this problem and connecting different heterogeneous blockchains that speak different languages, have different consensus rules, and support different smart contract languages. Axelar creates a single decentralized network and protocol stack to connect and connect different applications and platforms across all these ecosystems.
                        '''
    await callback.message.edit_text(text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    info = callback_data.get('info')
    lang = callback_data.get('lang')

    levels = {
        "0": list_menu,
        "1": show_info
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        info=info,
        lang=lang
    )
