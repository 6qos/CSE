import csv

def validate(num: str):
    if divisible_by_2(num) and divisible_by_three(num):
        return True
    return False

def divisible_by_three(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False

# with open("Book1.csv", 'r') as old_csv:
#   with open("MyNewFile.csv", 'w', newline='') as new_csv:
        with
#    reader = csv.reader(old_csv)
#   for row in reader:
#        old_number = row[0]
#        print(int(old_number)+ 1)
#        print(old_number)


with open("Book1.cav", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new.csv)
        print("Processing...")

        with open("Book1.csv", 'r')
            with open("MyNewFile.csv", 'w', newline='') as new_csv:
                print("Writing File...")
                reader = csv.reader(old_csv)
                writer = csv.writer(new_csv)
        for row in reader:
            old_number = int(row[0])
            old_number = row[0]

        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])
            if first_num % 2 == 0:
                writer.writerow(row)
            # print(int(old_number) + 1)
            # print(old_number)
print("OK")