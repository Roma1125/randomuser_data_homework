import json

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    r=[]
    
    for i in range(len(data['results'])):
        new_dict = {}
        first_name = data['results'][i]['name']['first']
        last_name = data['results'][i]['name']['last']
        phone_number = data['results'][i]['phone']        
        
        new_dict['first_name'] = first_name
        new_dict['last_name'] = last_name
        new_dict['phone_number'] = phone_number
        r.append(new_dict)
    return r





d=open('aaa.json', encoding='utf8').read()
dd=json.loads(d)
print(get_users_data(dd))