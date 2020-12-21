#Write a function that loops through a list of numbers and returns the count of those divisible by 10

def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#create a function that creates a list of greetings based off a list of names
def add_greetings(names):
  greetings = []
  for name in names:
    greeting = "Hello, " + name
    greetings.append(greeting)
  return greetings

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

def exponents(bases, powers):
  raised = []
  for base in bases:
    for power in powers:
      raised.append(base**power)
  return raised


#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for i in lst1:
    sum1 += i
  for x in lst2:
    sum2 +=x
  #return sum1, sum2
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

def over_nine_thousand(lst):
  i=0
  sum1 = 0
  while(i < len(lst)):
    if sum1 >= 9000:
      break
    else:
      sum1 += lst[i]
      i = i + 1
  return sum1


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

def same_values(lst1, lst2):
  same_value = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      same_value.append(i)
  return same_value


#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

def reversed_list(lst1, lst2):
  size = len(lst2)
  i = 0
  value = True
  for num in lst1:
    if lst1[i] == lst2[(size-1) - i]:
      value = True
      i = i + 1
    else:
      value = False
      i = i + 1
      break
  return value


#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))