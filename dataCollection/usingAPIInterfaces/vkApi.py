import vk_api

vk_session = vk_api.VkApi('+222222222', 'password')
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))