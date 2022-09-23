import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from collect_info import my_data

with open('token.txt') as file:
    vk_api_token = file.read()

authorization = vk_api.VkApi(token=vk_api_token)
longpoll = VkLongPoll(authorization)


def write_message(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text
        sender = event.user_id
        if received_message == 'Привет':
            write_message(sender, 'Добрый день!')
        elif received_message == 'Мой id':
            write_message(sender, sender)
        elif received_message == 'Мои параметры':
            write_message(sender, my_data.get_user_data(sender))
        elif received_message == 'Пока':
            write_message(sender, 'Ciao!')
        else:
            write_message(sender, 'Моя твоя не понимать!((')

