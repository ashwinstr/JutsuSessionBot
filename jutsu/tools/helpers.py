
import asyncio

from typing import Union
from telegraph import Telegraph

from pyrogram import Client

tele_ = Telegraph()


async def conv(bot, chat_id: Union[int, str], msg_id: int, user_id: int):
    resp = None
    num = 1
    while True:
        await asyncio.sleep(1)
        msg_ = msg_id + num
        resp = await bot.get_messages(chat_id, msg_)
        if num >= 20:
            break
        if not resp.empty:
            break
        num += 1
    return resp


""" async def conv(bot, chat_id, msg_id, user_id):
    try:
        response = await asyncio.wait_for(converse(bot, chat_id, msg_id, user_id), timeout=15)
        return response
    except asyncio.TimeoutError:
        return "Timeout" """


def telegrapher(a_title: str, content: str) -> str:
    auth_name = tele_.create_account(short_name="Kakashi")
    resp = tele_.create_page(
        title=a_title,
        author_name=auth_name,
        author_url="https://t.me/xplugin",
        html_content=content,
    )
    link_ = resp["url"]
    return link_


def int_list(list_):
    intlist = []
    for one in list_:
        if one.isdigit():
            one = int(one)
        intlist.append(one)
    return intlist

async def username_list(list_):
    u_list = []
    for one in list_:
        u_list.append((await bot.get_users(one)).username)
    return u_list

