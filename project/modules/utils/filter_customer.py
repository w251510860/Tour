def filter_css(index):
    if index == 1:
        return "input_name"
    else:
        return "input_pwd"


def filter_input_type(index):
    if index == 1:
        return "text"
    else:
        return "password"


def filter_user_css(index):
    if (index % 2) == 0:
        return "all_users_li"
    else:
        return "all_users_li_other"
