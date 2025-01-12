import json

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    r=[]
    for i in range(len(data['results'])):
        s={}
        if data['results'][i]['gender']=='male':
            s[data['results'][i]['gender'].title()]=1
        elif data['results'][i]['gender']=='female':
            s[data['results'][i]['gender'].title()]=0

        r.append(s)
    return r


d=open('randomuser_data.json', encoding='utf8').read()
dd=json.loads(d)
print(get_gender_users(dd))
