def arithmetic_arranger(problems, solve=False):
    # Check if the number of problems is valid
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize empty lists for different parts of the problem
    first_line = []
    second_line = []
    separator_line = []
    solution_line = []

    # Iterate through each problem
    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are valid numbers
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the operands have more than 4 digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the solution if requested
        if solve:
            if operator == '+':
                solution = int(operand1) + int(operand2)
            else:
                solution = int(operand1) - int(operand2)
            solution_line.append(str(solution).rjust(len(problem) + 2))

        # Append the formatted strings to respective lists
        first_line.append(operand1.rjust(len(problem) + 2))
        second_line.append(operator + " " + operand2.rjust(len(operand2)))
        separator_line.append("-" * (len(problem) + 2))

    # Join the lists into formatted strings
    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(separator_line)
    if solve:
        arranged_problems += "\n" + "    ".join(solution_line)

    return arranged_problems


problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems, solve=True)
print(arranged_problems)
