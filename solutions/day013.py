def intersection(array1, array2):
    intersection = []
    for i in array1:
        if i in array2:
            intersection.append(i)
    return print(intersection)

def main():
    array1 = [2,4,6,8,0,12,34]
    array2 = [2,12,7,6,9,0]
    intersection(array1,array2)

if __name__=="__main__":
    main()
