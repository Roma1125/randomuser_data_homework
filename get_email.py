import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
 
    r=[]
    for i in range(len(data['results'])):
        r.append(data['results'][i]['email'])
    return r

d=open('randomuser_data.json', encoding='utf8').read()
dd=json.loads(d)

print(get_email(dd))
