
import re

def main():
    with open('items.txt','r',encoding='utf-8') as f:
        g_page_config = re.search(r'g_page_config = (.*?);\n',f.read())
        with open('g_page_config.txt','w',encoding='utf-8') as file:
            file.write(g_page_config.group(1))


if __name__ == '__main__':
    main()















