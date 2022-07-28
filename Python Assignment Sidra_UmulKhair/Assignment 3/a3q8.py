Grades=[8,9,7,6,8,5,9,8.2,5.9,4.9,3,7]
print("Number of items in list :", len(Grades))
print("Maximum values in list :", max(Grades))

def cal_average(Grades):
    sum=0
    for t in Grades:
        sum=sum+t
    avg = sum/len(Grades)
    return avg
print("Average value of the given list :",cal_average(Grades))
