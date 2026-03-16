
def print_table(n):
    print(f"\nMultiplication Table for {n}")
    print("-" * 25)
    for i in range(1, 13):
        result = n * i
        print(f"  {n:>2} x {i:>2} = {result:>3}")

#  Single table 
while True:
    user_input = input("Enter a number between 1 and 12: ")
    number = int(user_input)
    if 1 <= number <= 12:
        print_table(number)
        break
    else:
        print("Invalid! Please enter a number between 1 and 12.")

# print all tables from 1 to 12 ---
print("\n" + "=" * 25)
print("  ALL TABLES (1 to 12)")
print("=" * 25)

for n in range(1, 13):
    print_table(n)
