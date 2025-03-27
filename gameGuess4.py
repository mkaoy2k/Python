"""Find a four-digit number that when multiplied by 4 equals its reverse.

This program solves a mathematical puzzle where we need to find a four-digit
number ABCD such that:
1. When multiplied by 4, the result is still a four-digit number
2. The result is the reverse of the original number
"""

def is_reverse(num1, num2):
    """Check if num2 is the reverse of num1.
    
    Args:
        num1 (int): First number
        num2 (int): Second number to check if it's the reverse of num1
        
    Returns:
        bool: True if num2 is the reverse of num1, False otherwise
    """
    return str(num2) == str(num1)[::-1]

def is_valid_result(num):
    """Check if a number multiplied by 4 is still a four-digit number.
    
    Args:
        num (int): Number to check
        
    Returns:
        bool: True if the result is a four-digit number, False otherwise
    """
    return num * 4 < 10000

def find_abcd():
    """Find a four-digit number that satisfies the puzzle conditions.
    
    Returns:
        int: The four-digit number that satisfies the conditions, or None if not found
    """
    for num in range(1000, 10000):  # Four-digit number range
        result = num * 4
        if is_valid_result(num) and is_reverse(num, result):
            return num
    return None

def main():
    """Main function to run the puzzle solver and display results."""
    print("\nSolving the four-digit number puzzle...")
    print("-" * 50)
    print("Puzzle conditions:")
    print("1. The number is a four-digit number (1000-9999)")
    print("2. When multiplied by 4, the result is still a four-digit number")
    print("3. The result is the reverse of the original number")
    print("-" * 50)
    
    result = find_abcd()
    if result:
        print(f"\nSolution found!")
        print(f"The four-digit number is: {result}")
        print(f"When multiplied by 4: {result * 4}")
        print(f"Which is the reverse of: {result}")
    else:
        print("\nNo solution found that satisfies all conditions.")

if __name__ == '__main__':
    main()
