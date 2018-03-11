
import requests
import re
import json


def get_space_end(level):
    return '  ' * level + '-'


def get_space_expand(level):
    return '  ' * level + '+'


# 获取字典的层数,使用递归
def find_keys(targets, level):
    keys = iter(targets)  # 迭代器
    for each in keys:
        if type(targets[each]) is not dict:  # 值为字典就继续，不是字典就打印键
            print(get_space_end(level) + each)
        else:
            next_level = level + 1
            print(get_space_expand(level) + each)
            find_keys(targets[each], next_level)


def main():
    with open('items.txt', 'r', encoding='utf-8') as f:
        g_page_config = re.search(r'g_page_config = (.*?);\n', f.read())
        # print(g_page_config)
        # print(g_page_config.group(1))
        page_config_json = json.loads(g_page_config.group(1))
        find_keys(page_config_json, 1)


if __name__ == '__main__':
    main()
