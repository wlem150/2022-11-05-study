# match case 문은 if elif 문과 비슷하게 활용할 수 있음

# match case 
for i in range(1, 11):
    match i % 2:
        case 0 :
            print("{} is even".format(i))
        case 1 :
            print("{} is odd".format(i))

for i in range(1, 101):
    match i % 3, i % 5 :
        case(0,0) :
            print("FizzBuzz")
        case(0, _):
            print("Fizz")
        case(_, 0):
            print("Buzz")
        case _:
            print(i)

command = input("show, remove : ")
Sample_list = ["Sample", "Sample2", "Sample3"]

def file_handler_v1(command):
    match command.split():
        case ['show']:
            print('List all files and directorise : ')
            # code to list files
        case ['remove', *files]:
            print(files)
            print('Removing files: {}'.format(files))
            # code to remove files
        case _:
            print('Command not recognized')

file_handler_v1(command)

print(Sample_list)

