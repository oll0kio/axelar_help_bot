from aiogram import types

from keyboards.inline.menu_keyboards import menu_keyboard, menu_cd, info_keyboard
from loader import dp


async def list_menu(callback: types.CallbackQuery, lang, **kwargs):
    markup = await menu_keyboard(lang)
    if lang == "ru":
        text = ("<b>Основное меню</b>\n"
                "Осмотрись, здесь ты найдёшь много полезной информации по замечательному проекту Axelar.\n\n"
                "(на данный момент информация добавляется)\n\n"
                "Разработчик бота: ollokio#7327")
    else:
        text = ("<b>Main menu</b>\n"
                "Look around, here you will find a lot of useful information about the wonderful Axelar project.\n\n"
                "(information is currently being added)\n\n"
                "Bot Developer: ollokio#7327")
    await callback.message.edit_text(text, reply_markup=markup)


async def show_info(callback: types.CallbackQuery, info, lang):
    markup = info_keyboard(lang)
    if lang == "ru":
        match info:
            case "motivation":
                text = ('<b>Мотивация для создания Axelar</b>\n'
                        'Команда Акселар увидела большую проблему для системы, которая, будет становиться все более '
                        'актуальной в последствии. В частности, тенденцию к тому, что для разработчиков создавалось '
                        'все больше и больше быстрых и безопасных цепочек, и хотя некоторые разработчики хотели бы '
                        'делать что-то на основе этих платформ… Они ещё и хотели бы получить доступ к ликвидности с '
                        'возможностью компоновки других существующих экосистем, таких как Bitcoin и Ethereum. '
                        'Потребность в масштабируемой межсетевой связи будет только расти по мере того, '
                        'как развивается человечество. Поэтому Сергей Горбунов и соучредитель Georgios решили начать '
                        'новое предприятие для решения этой проблемы.')
            case "trouble":
                text = ('<b>Какие проблемы решает Axelar?</b>\n'
                        'Мы определенно входим в мир мультисетей, поэтому видим, что сетей становится всё больше, '
                        'а стоимость запуска новой понижается. В этом мире мобильность активов и обмен информацией '
                        'между сетями становятся все более важными. На чем Axelar сосредоточен, так это на создании '
                        'децентрализованного стека для решения этой проблемы и соединения различных разнородных '
                        'блокчейнов, которые говорят на разных языках, имеют разные правила консенсуса и поддерживают '
                        'разные языки смарт-контрактов. Акселар создает единую децентрализованную сеть и стек '
                        'протоколов для подключения и объединения различных приложений и платформ во всех этих '
                        'экосистемах.')
            case "usage":
                text = ('<b>Варианты использования сети Axelar</b>\n'
                        'Некоторые первоначальные варианты использования связаны с передачей активов. Если вы '
                        'владеете активом в одной из существующих цепочек блоков, таких как Bitcoin или Ethereum, '
                        'и хотите использовать этот актив в приложении, построенном на одной из других блокчейнов, '
                        'то столкнетесь с сложностями. Часто приходится полагаться на централизованное решение. Но '
                        'Акселар создает сеть и приложения на ее основе, они позволят пользователям перемещать свои '
                        'активы в другой блокчейн. В дальнейшем используя их непосредственно в своих приложениях.\nВ '
                        'более общем плане Axelar Network позволить приложениям объединяться в произвольные цепочки. '
                        'Например, если вы хотите получить информацию о процентной ставке с одной платформы, '
                        'вы сможете выполнить общий запрос через SSL сеть и получить процентную ставку с другой '
                        'платформы для вашего приложения.')

    else:
        match info:
            case "motivation":
                text = ('<b>Motivation for creating Axelar</b>\n'
                        'The Axelar team saw a big problem for the system, which will become more and more relevant in the '
                        'future. In particular, the trend towards more and more fast and secure chains for '
                        'developers, and while some developers would like to build on these platforms… They also want '
                        'to access liquidity with the ability to link other existing ecosystems , such as Bitcoin and '
                        'Ethereum. The need for scalable interconnection will only grow as humanity evolves. '
                        'Therefore, Sergey Gorbunov and co-founder Georgios decided to start a new venture to solve '
                        'this problem.')
            case "trouble":
                text = ('<b>What problems does Axelar solve?</b>\n'
                        'We are definitely entering the world of multi-networks, so we see more and more networks, '
                        'and the cost of launching a new one is going down. In this world, the mobility of assets and '
                        'the exchange of information between networks are becoming increasingly important. What '
                        'Axelar is focusing on is building a decentralized stack to solve this problem and connecting '
                        'different heterogeneous blockchains that speak different languages, have different consensus '
                        'rules, and support different smart contract languages. Axelar creates a single decentralized '
                        'network and protocol stack to connect and connect different applications and platforms '
                        'across all these ecosystems.')
            case "usage":
                text = ('<b>Use cases for the Axelar network</b>\n'
                        'Some initial use cases are related to the transfer of assets. If you own an asset on one of '
                        'the existing blockchains, such as Bitcoin or Ethereum, and want to use that asset in an '
                        'application built on one of the other blockchains, then you will run into difficulties. '
                        'Often you have to rely on a centralized solution. But Akselar is building the network and '
                        'applications based on it, they will allow users to move their assets to another blockchain. '
                        'In the future, using them directly in their applications.\nMore generally, Axelar Network '
                        'will allow applications to join in arbitrary chains. For example, if you want to get '
                        'interest rate information from one platform, you can make a general query over the SSL '
                        'network and get the interest rate from another platform for your application.')

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
