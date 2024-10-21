class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # left child node
        self.right = right  # right child node
        self.value = value  # value for operand nodes

    def __repr__(self):
        if self.type == "operand":
            return str(self.value)
        return f"({self.left} {self.value} {self.right})"

def evaluate_condition(field_value, operator, condition_value):
    # Handle different comparison operators explicitly
    if operator == '==':
        return field_value == condition_value
    elif operator == '!=':
        return field_value != condition_value
    elif operator == '>':
        return field_value > condition_value
    elif operator == '<':
        return field_value < condition_value
    elif operator == '>=':
        return field_value >= condition_value
    elif operator == '<=':
        return field_value <= condition_value
    return False

def evaluate_rule(ast, user_data):
    if ast.type == "operand":
        # Split condition: e.g., "age > 30" or "department == 'Sales'"
        condition = ast.value.split()
        field, operator, value = condition[0], condition[1], condition[2]

        # Get the value from the user_data
        field_value = user_data[field]

        # Handle integer or string comparisons
        if value.isdigit():
            value = int(value)  # Convert to int for comparison
            return evaluate_condition(field_value, operator, value)
        else:
            # Handle string comparisons (strip quotes)
            value = value.strip("'\"")
            return evaluate_condition(field_value, operator, value)

    elif ast.type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, user_data) and evaluate_rule(ast.right, user_data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, user_data) or evaluate_rule(ast.right, user_data)
