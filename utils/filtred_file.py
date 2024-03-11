def get_filtered(list_with_dict):
    """
    :param list_with_dict: Содержит список со словарями, содержащими информацию о банковских операциях
    :return: список, содержащий только успешные операции, а также он уже отсортирован по дате/времени
    """
    list_new = []
    for dictionary in list_with_dict:
        if dictionary and dictionary['state'] == 'EXECUTED':
            list_new.append(dictionary)
    get_list = sorted(list_new, key=lambda x: x['date'])
    return get_list
