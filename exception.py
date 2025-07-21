"""
Exception handling: Process of managing and responding a runtime errors or unexpected situations that can occur when a program is being executed. 
One can handle these errors with the try, except, else, and finally blocks.
Exception handling used to prevent crashes due to unforeseen errors, provide informative error messages to users, and log debugging information. 
"""
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError as e:
    print(f"Cannot divide by zero.{e}")
except ValueError as e:
    print(f"Invalid input. Please enter a number.{e}")
else:
    print("Result:", result)
finally:
    print("Exception handling complete.")