# import mem_profile
import meminfo
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

total = 1_000_000
print('Generator Performance:')
print('===>Before:')
meminfo.mem_info()
print()

g1 = time.process_time()
people = people_generator(total)
g2 = time.process_time()

print('===>After:')
meminfo.mem_info()
print('Took {:.2f} Seconds'.format(g2 - g1))
print()


print('List Performance:')
print('===>Before:')
meminfo.mem_info()
print()

t1 = time.process_time()
people = people_list(total)
t2 = time.process_time()

print('===>After:')
meminfo.mem_info()
print('Took {:.2f} Seconds\n'.format(t2 - t1))
print()
