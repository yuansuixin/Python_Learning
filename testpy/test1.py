

'''

题目内容：

某些英语单词的字母经过重新排列后，能获得另外一个单词，如可以将“cinema”转换成另一个单词“iceman”。编写程序，将词表中由相同字母组成的单词聚成一类，并按照单词个数由多到少的顺序输出各类中的全部单词（每类占一行，单词按字典序由小到大排列，之间用空格分隔），若每类中单词个数相同，则按每类中第一个单词的字典序由大到小输出各个类别。

输入格式:

按字典序由小到大输入若干个单词，每个单词占一行。

输出格式：

并按照单词个数由多到少的顺序输出各类中的全部单词（每类占一行，单词按字典序由小到大排列，之间用空格分隔），若每类中单词个数相同，则按每类中第一个单词的字典序由大到小输出各个类别。



输入样例：

cinema

iceman

maps

spam


输出样例：

maps spam

cinema iceman

'''

def main():
    # words = input('请输入四个单词：以空格分隔')
    words = 'cinema iceman maps spam'
    words = words.split(' ')
    print(words)
    d = {}
    for each in words:
        L = sorted(each,key=str.lower)
        d[each] = L
    print(d)

    a = d.values()
    # 对于value进行去重的操作
    b = []
    for each in a:
        if each not in b:
            b.append(each)
    print(b)


    for i in b:
        for key,value in d.items():
            if value==i:
                print(key,end=' ')
        print()
















if __name__ == '__main__':
    main()