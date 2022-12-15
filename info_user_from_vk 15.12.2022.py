import vk_api, requests, json
import pprint

API_URL = 'https://api.vk.com/method/'
user_token = ''


class VK:
    def get_info(self, user_ids):
        method = 'users.get'
        url = self.API_URL + method
        params = {
            'user_ids': user_ids,
            'access_token': self.user_token,
            'fields': 'screen_name, city, bdate, sex, screen_name',
            'v': '5.131'
        }
        res = requests.get(url, params=params)
        response = res.json().get("response")
        return response


    def search_users(self, sex, age_at, age_to, city):
        all_persons = []
        idnum = []
        link_profile = 'https://vk.com/id'
        vk_ = vk_api.VkApi(token=user_token)
        response = vk_.method('users.search',
                              {'sort': 1,
                               'sex': sex,
                               'status': 1,
                               'age_from': age_at,
                               'age_to': age_to,
                               'has_photo': 1,
                               'album_id': 'profile',
                               'count': 25,
                               'online': 1,
                               'hometown': city
                               })
        for element in response['items']:
            person = [
                element['first_name'],
                element['last_name'],
                link_profile + str(element['id']),
                element['id']
            ]
            person_id = [
                element['id']
            ]
            all_persons.append(person)
            idnum.append(person_id)
        for i in idnum:
            self.get_vk_photo(i, user_token)

        return all_persons, idnum, i

sex = int(input('введите пол \n 1 - женский, \n 2 - мужской: '))
age_at = int(input("возраст от "))
age_to = int(input("возраст до "))
city = input("город: ")
find_people = VK.search_users(sex, age_at, age_to, city)
print(f'запрос поиска людей в возрасте от {age_at} до {age_to} лет из города {city}\nрезультат: {find_people}')
VK.search_users(sex, age_at, age_to, city)

