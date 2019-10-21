import numpy
import time

my_arr = numpy.arange(1000000)
my_list = list(range(1000000))

# this only runs in shell
#print(%time for _ in range(10): my_arr2 = my_arr * 2)
#print(%time for _ in range(10): my_list2 = [x * 2 for x in my_list])

start = time.time()
my_arr2 = my_arr * 2
#print(my_arr2)
end = time.time()
print("Execution time: ", end - start)
start = time.time()
my_list2 = [x * 2 for x in my_list]
#print(my_list2)
end = time.time()
print("Execution time: ", end - start)
