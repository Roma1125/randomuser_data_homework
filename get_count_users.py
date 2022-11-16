

import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    
    return len(data['results'])
d=open('randomuser_data.json',  'r', encoding='utf8').read()
dd=json.loads(d)
  
       
print(get_count_users(dd)) 

  



    
