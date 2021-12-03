#ADVENT OF CODE 2020 - DAY 1

def parse_data(filename):
    input_file = open(filename)
    data = input_file.readlines()
    input_file.close()
    for i in range(len(data)):
        data[i] = data[i][0:-1]
    return data


def try_sums(list):
    result_list = []
    for a in list:
        num1 = int(a)
        for b in list:
            num2 = int(b)
            for c in list:
                num3 = int(c)
                if (num1 == num2) or (num2 == num3) or (num1 == num3) or \
                    (num1 in result_list) or (num2 in result_list) or (num3 in result_list):
                    break
                if (num1 + num2 == 2020):
                    product2 = num1 * num2
                    print(num1, num2, end="")
                    print(" ... sum: 2020, product:", product2)
                    result_list.extend([num1,num2])
                    break
                if (num1 + num2 + num3 == 2020):
                    product3 = num1 * num2 * num3
                    print(num1, num2, num3, end="")
                    print(" ... sum: 2020, product:", product3)
                    result_list.extend([num1,num2,num3])
                    break
    return product2, product3


def main():
 report = parse_data(r'day01-input.txt')
 try_sums(report)

if __name__ == "__main__":
    main()