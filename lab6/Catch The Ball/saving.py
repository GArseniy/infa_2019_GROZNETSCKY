import scores


def saver(result, name):
    f = open("data.txt", mode='r', encoding='utf-8')
    fiction = f.readline()[0:-1]
    if result < int(fiction):
        f.close()
        
    else:
        for i in range(2):
            fiction = f.readline()[0:-1]
        if result < int(fiction):
            f.close()
            reserve = open("reserve.txt", mode='r', encoding='utf-8')
            with open("data.txt", 'w', encoding='utf-8') as f:
                f.write(str(result) + '\n')
                f.write(name + '\n')
                for i in range(2):
                    fiction = reserve.readline()
                for i in range(4):
                    f.write(reserve.readline())
            reserve.close()
            f = open("data.txt", mode='r', encoding='utf-8')
            with open("reserve.txt", 'w', encoding='utf-8') as reserve:
                for i in range(6):
                    reserve.write(f.readline())
            f.close()

        else:
            for i in range(2):
                fiction = f.readline()[0:-1]
            if result < int(fiction):
                f.close()
                reserve = open("reserve.txt", mode='r', encoding='utf-8')
                with open("data.txt", 'w', encoding='utf-8') as f:
                    for i in range(2):
                        fiction = reserve.readline()
                    for i in range(2):
                        f.write(reserve.readline())
                    f.write(str(result) + '\n')
                    f.write(name + '\n')
                    for i in range(2):
                        f.write(reserve.readline())
                reserve.close()
                f = open("data.txt", mode='r', encoding='utf-8')
                with open("reserve.txt", 'w', encoding='utf-8') as reserve:
                    for i in range(6):
                        reserve.write(f.readline())
                f.close()

            else:
                f.close()
                reserve = open("reserve.txt", mode='r', encoding='utf-8')
                with open("data.txt", 'w', encoding='utf-8') as f:
                    for i in range(2):
                        fiction = reserve.readline()
                    for i in range(4):
                        f.write(reserve.readline())
                    f.write(str(result) + '\n')
                    f.write(name + '\n')
                reserve.close()
                f = open("data.txt", mode='r', encoding='utf-8')
                with open("reserve.txt", 'w', encoding='utf-8') as reserve:
                    for i in range(6):
                        reserve.write(f.readline())
                f.close()
