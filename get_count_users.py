

import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    d=open(data,  'r', encoding='utf8').read()
    dd=json.loads(d)

    return len(dd['results'])

print(get_count_users('aaa.json'))





    