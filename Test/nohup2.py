
def writer_file(path,data):
    with open(path,'w',encoding='utf-8') as f:
        for lines in data:
            f.write(lines)
        print('gogogoogog')
        # f.write(str(data))
        # f.writable(data)


def main():
    with open('nohup.out','r',encoding='utf-8') as f:
        data = []
        start = '1514358801'
        for each_line in f:
            line = each_line.split('.')
            end_time = int(start)+60
            if start <= line[0] <= str(end_time):
                data.append(each_line)
            else:
                if each_line == '\n':
                    continue
                writer_file(start+'.txt',data)
                data = []
                start = line[0]
                print(start)
        writer_file(start + '.txt', data)



if __name__ == '__main__':
    main()



















