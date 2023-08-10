from api import PetFriends
from settings import *

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Кошак', animal_type='пуш', age='3', pet_photo='image/cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Кошарик", "кот", "3", "image/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Пушлан', animal_type='Котэ', age=7):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_add_new_pet_without_photo_with_valid_data(name='Кошак', animal_type='пуш', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


def test_add_photo(pet_photo='image/cat2.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    status, result = pf.add_photo(auth_key, pet_id, pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_change_photo(pet_photo='image/cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    old_photo = my_pets['pets'][0]['pet_photo']

    status, result = pf.add_photo(auth_key, pet_id, pet_photo)

    assert status == 200
    assert result['pet_photo'] != old_photo


def test_add_new_pet_without_name(name='', animal_type='кот', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert result['name'] == ''
        print('Баг! Добавлен питомец без имени.')
    else:
        assert status == 200
        print('Нельзя добавить питомца без имени.')


def test_add_new_pet_without_animal_type(name='Кошак', animal_type='', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert result['animal_type'] == ''
        print('Баг! Добавлен питомец без указания породы.')
    else:
        assert status == 200
        print('Нельзя добавить питомца без породы.')


def test_add_new_pet_without_age(name='Кошак', animal_type='кот', age=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert result['age'] == ''
        print('Баг! Добавлен питомец без указания возраста.')
    else:
        assert status == 200
        print('Нельзя добавить питомца без возраста.')


def test_add_new_pet_with_text_age(name='Кошак', animal_type='кот', age='пять'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert result['age'] == 'пять'
        print('Баг! Добавлен питомец с текстом в поле "возраст".')
    else:
        assert status == 200
        print('Нельзя добавить питомца без возраста.')


def test_add_new_pet_with_name_256_chars(
        name='sDv9WWAbbHMlaYsx0BkNrcAlOwB4oEyihoZUvNI9mpr6UdhCfBTfzQz5dME0CgpFzIjIbPIc9YuyABJRVl2DP6zpwj3tkHJYgW0pyaMkrYJ5bmplld3O2YVLbKDkYm620YoojPXUYZFHaHYb1YMomzbKZBnmeLq6TKxk7T3P6FeSLqHUHC5E4ov9y0aHXCVcjd4rnVi3uPsBdoCvmbFzWfYCPHRiE2by3ArsiggfLXvQUEe6CjKeBJuv3EZW3FzP',
        animal_type='кот', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert len(result['name']) == 256
        print('Баг! Добавлен питомец с очень длинным именем.')
    else:
        assert status == 200
        print('Нельзя добавить питомца с очень длинным именем.')


def test_add_new_pet_with_space_in_name(name=' ', animal_type='кот', age='5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert result['name'] == ' '
        print('Баг! Добавлен питомец с пробелом вместо имени.')
    else:
        assert status == 200
        print('Нельзя добавить питомца с пробелом вместо имени.')

def test_add_new_pet_with_special_chars_in_name(name='Кошак№%?!', animal_type='кот', age='5'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert result['name'] == 'Кошак№%?!'
        print('Баг! Добавлен питомец со спецсимволами в имени.')
    else:
        assert status == 200
        print('Нельзя добавить питомца со спецсимволами в имени.')

def test_add_new_pet_with_alternative_chars_in_name(name='☺☻♥♦♣♠•◘', animal_type='кот', age='5'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert result['name'] == '☺☻♥♦♣♠•◘'
        print('Баг! Добавлен питомец с альтернативными спецсимволами в имени.')
    else:
        assert status == 200
        print('Нельзя добавить питомца с альтернативными спецсимволами в имени.')

def test_add_new_pet_with_XSS_injection_in_name(name='<script>alert("Поле уязвимо!")</script>', animal_type='кот', age='5'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    if status == 200:
        assert status == 200
        assert result['name'] == '<script>alert("Поле уязвимо!")</script>'
        print('Баг! Добавлен питомец с XSS инъекцией в имени.')
    else:
        assert status == 200
        print('Нельзя добавить питомца с XSS инъекцией в имени.')