#ADVENT OF CODE 2020 - DAY 3

def parse_data(filename):
    input_file = open(filename)
    data = input_file.readlines()
    input_file.close()
    line_length = len(data[0])-1
    for i in range(len(data)):
        data[i] = data[i][0:-1]
    return data, line_length


def move_position(position,slope,line_length):
    position = ( ((position[0] + slope[0]) % line_length), ((position[1] + slope[1])) )
    return position


def navigate(data_set,position,slope,line_length):
    trees = 0
    while position[1]+slope[1] < len(data_set):
        position = move_position(position,slope,line_length)
        line = data_set[position[1]]
        value = line[position[0]]
        if value == "#":
            trees += 1
        #print(position,value)
    return trees


def multiply_list(list):
    result = 1
    for n in list:
        result = result * n
    return result


def main():
 topography, line_length = parse_data(r'day03-input.txt')
 test_number = int(input("how many slopes do you want to test?: "))
 result_list = []
 for n in range(test_number):
    position = (0, 0)
    print("\nfor slope", n+1)
    slope_x = int(input("enter x: "))
    slope_y = int(input("enter y: "))
    slope = (slope_x, slope_y)
    trees = navigate(topography,position,slope,line_length)
    #print("\n", trees, "trees encountered")
    result_list.append(trees)
 print("\nthe sum of all results is: ", sum(result_list))
 print("the product of all results is: ", multiply_list(result_list))


if __name__ == "__main__":
    main()