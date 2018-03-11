


def writer_file(path,data):
    with open(path,'w',encoding='utf-8') as f:
        for line in data:
            f.write(line)
        print('gogogoogog')


def main():
    with open('nohup(3).out','r',encoding='utf-8') as f:
        data = []
        start = f.readline().split('.')[0]
        for each_line in f:
            line = each_line.split('.')
            end_time = int(start) + 60
            if start <= line[0] <= str(end_time):
                data.append(each_line)
                # writer_file(start+'.txt',each_line)
            else:
                if each_line == '\n':
                    continue
                writer_file(start+'.txt',data)
                data=[]
                start = line[0]
        writer_file(start + '.txt', data)


if __name__ == '__main__':
    main()
