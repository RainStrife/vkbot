import vk
import time
from settings import Data

session = vk.AuthSession(Data.app_id, Data.login, Data.password, 'messages')
vk_api = vk.API(session)
vk_api.access_token = Data.token

try:
    for friend in vk_api.friends.get():
        if vk_api.messages.getHistory(user_id=friend, count=1) != [0]:
            vk_api.messages.send(user_id=30078867, message='Test')
            time.sleep(1)
except Exception as e:
    print(e)  # TODO: капча.

