import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    d=open(data, encoding='utf8').read()
    dd=json.loads(d)
    r=[]
    for i in range(len(dd['results'])):
        r.append(dd['results'][i]['email'])
    return r



print(get_email('randomuser_data.json'))