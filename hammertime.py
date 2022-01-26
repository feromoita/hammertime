from telethon import TelegramClient, events
from py3cw.request import Py3CW

## TELEGRAM CONFIG ## https://my.telegram.org/apps
api_id = ''
api_hash = ''

## 3COMMAS CONFIG ##
commas_key = ''  # INSERT 3COMMAS API KEY HERE IN THE QUOTES
commas_secret = ''  # INSERT 3COMMAS API SECRET HERE IN THE QUOTES

long_bot_ids = {
    'BINANCEUS':
        [],  # INSERT COMMA SEPERATED LIST OF ALL OF YOUR LONG BOTS, NO QUOTES
    'BINANCE':
        [],
    'KUCOIN':
        []
}

short_bot_ids = {
    'BINANCEUS':
        [],  # INSERT COMMA SEPERATED LIST OF ALL OF YOUR SHORT BOTS, NO QUOTES
    'BINANCE':
        [],
    'KUCOIN':
        []
}

##################


########## NO TOUCHY ##########
p3cw = Py3CW(key=commas_key, secret=commas_secret)
client = TelegramClient('anon', api_id, api_hash)


def parse_tg(raw_text):
    return raw_text.split('\n')


def trigger_3c(text_lines):
    # Make sure the message is a signal
    if len(text_lines) == 4:
        pair = text_lines[2].replace('#', '')
        # Choose long/short bot dict
        bot_dict = long_bot_ids if text_lines[3] == 'LONG' else short_bot_ids
        # Loop through all of the bot ids for the exchange that got a signal
        for bot_id in bot_dict[text_lines[1]]:
            error, data = p3cw.request(
                entity="bots",
                action="start_new_deal",
                action_id=f"{bot_id}",
                payload={  # type: ignore
                    "bot_id": f"{bot_id}",
                    "pair": f"{pair}",
                },
            )


@client.on(events.NewMessage(chats="Hammer Time"))
async def my_event_handler(event):
    trigger_3c(parse_tg(event.raw_text))


async def main():
    print('Refreshing cache...')
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
    print('\n*** ITS HAMMER TIME ***')


with client:
    client.loop.run_until_complete(main())

client.start()
client.run_until_disconnected()
