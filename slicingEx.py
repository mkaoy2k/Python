"""Examples of slicing a list
Syntax: list[start:end:step]
where 'end' is not inclusive
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
print('Slicing a list:', my_list)
print('===>1st [0]:', my_list[0])
print('===>or[-10]:', my_list[0])
print('===>range 0-5:', my_list[0:6])
print('===>range 5-9:', my_list[5:])

print('===>even numbers:', my_list[2:-1:2])
print('===>reversed even numbers:', my_list[-2:1:-2])
print(f'===>resersed entire list :{my_list[::-1]}\n')


sample_url = 'http://coreyms.com'
print(f'Slicing a string:"{sample_url}"')

# Reverse the url
print('===>Reverse the url:', sample_url[::-1])

# Get the top level domain
print('===>Get the top level domain:', sample_url[-4:])

# Print the url without the http://
print('===>url without the http://:', sample_url[7:])

# Print the url without the http:// or the top level domain
print('   url without the http:// or the top level domain:', sample_url[7:-4])
