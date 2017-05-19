import numpy as np

a = np.array([1, 2, 3, 4])
# Arithmetic operations between 2 NumPy a
b = np.array([1, 2, 1, 2])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

#result:
# [2 4 4 6]
# [0 0 2 2]
# [1 4 3 8]
# [ 1.  1.  3.  2.]
# [ 1  4  3 16]
# Arithmetic operations between a NumPy
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

# [3 4 5 6]
# [-1  0  1  2]
# [2 4 6 8]
# [0 1 1 2]
# [ 1  4  9 16]
# Logical operations with NumPy arrays

a = np.array([False, False, True, True])
b = np.array([False, True, True, False])

print(a & b)
print(a | b)
print(~a)

print(a & True)
print(a & False)

print(a | True)
print(a | False)

# Comparison operations between 2 NumPy Arrays

print("\nCompare in 2 numpy\n")

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

print("\nCal School Completin_\n")
# First 20 countries with school completion data
countries = np.array([
       'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria','Azerbaijan',
       'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
       'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
       'Cambodia', 'Cameroon', 'Cape Verde'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
    98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
    95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
    29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
     95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
     97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
    102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
     37.00692,   45.39401,   91.22084,   62.42028,   90.66958
])
#计算一个国家的整体教育普及率
def overall_completion_rate(female_comletion, male_completion):
    return ((female_comletion + male_completion)/2)

print(overall_completion_rate(female_completion,male_completion))

print("\nEmployee Vector Standardize Info_ Cal_\n")

employment = np.array([
    55.70000076,  51.40000153,  50.58776887,  75.69999695,
    58.40000153,  40.09999847,  61.59364590,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])


def standardize_date(values):
    standardize_values = (values - values.mean()) / values.std()
    return standardize_values

# print(standardize_date(test))

test = np.array([1,2,3,4])

print(test.mean())
print(test.std() ** 2)
print((1-2.5)**2 + (2-2.5)**2+ (3-2.5)**2 + (4-2.5)**2)

# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])


##cal 2 day NOT regstudent

def mean_time_for_paid_students(time_spent, days_to_cancel):
    print(time_spent[days_to_cancel >= 2]) ##
    return time_spent[days_to_cancel >= 2].mean()##


t1 = np.array([1,2,3,4])
t2 = np.array([1,2,8,4])

print(mean_time_for_paid_students(t1,  t2))
# Result shoe below
# [2 3 4]
# 3.0

import pandas as pd

##show relation between expec_life and GDP_Value

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

def variable_correlation(variable1, variable2):
    # print("__Show__\n")
    both_above = (variable1 > variable1.mean()) & (variable2 > variable2.mean())
    # print(both_above)
    both_below = (variable1 < variable1.mean()) & (variable2 < variable2.mean())
    # print(both_below)

    is_same_direction = both_above | both_below
    # print(is_same_direction)
    num_same_direction = is_same_direction.sum()

    num_different_direction = len(variable1) - num_same_direction

    return (num_same_direction, num_different_direction)


print(variable_correlation(life_expectancy, gdp))

life_expectancy = pd.Series([74.7, 75, 83, 57.6],index=[
                        'Albania',
                        'Algeria',
                        'Andorra',
                        'Angola'
                        ])

print(life_expectancy)
print(life_expectancy.loc['Angola'])  ## show value is 57.6

employment_values = [
    55.70000076,  51.40000153,  90.59874744,  75.69999695,
    58.40000153,  40.09999847,  61.58463949,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
]

employment = pd.Series(employment_values, index=countries)

def max_employment(employment):
    max_country = employment.argmax();
    max_value = employment.loc[max_country]

    return (max_country, max_value)

print(max_employment(employment))

test = [1, 4, 15, 3, 8]
val = pd.Series(test)
print(val.argmax())  ## show value is 2 , show max value position

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
sum = s1 + s2;

print(s1 + s2)

print(sum.dropna())

print(np.zeros(3))
print(np.power(2,3))


arr1 = np.array([1.2 , 2.1, 3.9])
arr2 = np.array([1, 2, 3])

print(np.ceil(arr1))
print(np.floor(arr1))
print(np.round(arr1))
##Result is follow:
# [ 2.  3.  4.]
# [ 1.  2.  3.]
# [ 1.  2.  4.]

Z = np.zeros((10,10)) ## us np.zero(10,10) show data type not understood ERROR
