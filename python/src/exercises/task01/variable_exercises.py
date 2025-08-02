"""
Task 1: Variable Declaration and Initialization

Complete the methods below by implementing the required functionality.
Each method has specific requirements detailed in the docstrings.

Run the tests with: python -m pytest tests/task01/ -v
"""

from typing import Union


class VariableExercises:

    """
    Python exercises for variable declaration and initialization.
    Unlike Java, Python uses dynamic typing - no need to declare types explicitly.
    """

    def initialize_integer(self) -> int:
        return 42
    
        """
        Create and return an integer variable with the value 42
        
        Returns:
            int: The integer value 42
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def initialize_float(self) -> float:
        return 3.14159
        """
        Create and return a float variable with the value 3.14159
        
        Returns:
            float: The float value 3.14159
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def initialize_boolean(self) -> bool:
        return True
        """
        Create and return a boolean variable with the value True
        
        Returns:
            bool: The boolean value True
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def initialize_string(self) -> str:
        return "Hello, World!"
        """
        Create and return a string variable with the value "Hello, World!"
        
        Returns:
            str: The string value "Hello, World!"
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def initialize_list(self) -> list:
        return [1, 2, 3, 4, 5]
        """
        Create and return a list with the values [1, 2, 3, 4, 5]
        
        Returns:
            list: A list containing [1, 2, 3, 4, 5]
        """
        # TODO: Implement this method
        raise NotImplementedError("Method not implemented yet")

    def variable_reassignment(self) -> int:
        value = 10
        value += 5  # or value = value + 5
        value *= 2  # or value = value * 2
        return value
    
        """
        Demonstrate variable reassignment in Python
        Start with value 10, then add 5, then multiply by 2
        
        Returns:
            int: The final calculated value (should be 30)
        """
        # TODO: Implement this method
        # value = 10
        # value += 5  # or value = value + 5
        # value *= 2  # or value = value * 2
        # return value
        raise NotImplementedError("Method not implemented yet")

    def work_with_constants(self) -> int:
        ConstantValue = 100
        return ConstantValue
        """
        Work with constants in Python (conventionally UPPER_CASE)
        Create a constant with value 100 and return it
        Note: Python doesn't have true constants, but uses naming convention
        
        Returns:
            int: The constant value 100
        """
        # TODO: Implement this method
        # CONSTANT_VALUE = 100
        # return CONSTANT_VALUE
        raise NotImplementedError("Method not implemented yet")

    def type_conversion(self) -> int:
        original_value = 9.99
        converted_value = int(original_value)  # This will truncate the decimal part
        return converted_value
        """
        Type conversion exercise
        Convert the float 9.99 to an integer (truncating the decimal)
        
        Returns:
            int: The integer value 9
        """
        # TODO: Implement this method
        # original_value = 9.99
        # return int(original_value)
        raise NotImplementedError("Method not implemented yet")

    def multiple_assignment(self) -> tuple: 
        a, b, c = 1, 2, 3
        return (a, b, c)
        """
        Demonstrate Python's multiple assignment feature
        Assign values 1, 2, 3 to variables a, b, c respectively and return them as a tuple
        
        Returns:
            tuple: A tuple containing (1, 2, 3)
        """
        # TODO: Implement this method
        # a, b, c = 1, 2, 3
        # return (a, b, c)
        raise NotImplementedError("Method not implemented yet")

    def dynamic_typing(self) -> tuple:
        variable = 42
        first_value = variable
        variable = "Hello"
        second_value = variable
        return (first_value, second_value)  
        """
        Demonstrate Python's dynamic typing
        Start with a variable as an integer 42, then reassign it to string "Hello"
        Return both values as a tuple
        
        Returns:
            tuple: A tuple containing (42, "Hello")
        """
        # TODO: Implement this method
        # variable = 42
        # first_value = variable
        # variable = "Hello"
        # second_value = variable
        # return (first_value, second_value)
        raise NotImplementedError("Method not implemented yet")
