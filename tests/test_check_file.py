from utils.check_file import print_correct


def test_check_source(list_with_dict):
    assert print_correct(list_with_dict[0]['from']) == "Maestro 1308 79** **** 7170"
    assert print_correct(list_with_dict[0]['to']) == "Счет **8612"
