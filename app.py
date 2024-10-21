from flask import Flask, request, jsonify
from rule_engine import Node, evaluate_rule

app = Flask(__name__)

# Helper function to recreate AST from JSON
def create_ast_from_json(ast_json):
    if ast_json['type'] == 'operand':
        return Node("operand", value=ast_json['value'])
    return Node(
        "operator",
        create_ast_from_json(ast_json['left']),
        create_ast_from_json(ast_json['right']),
        ast_json['value']
    )

# API to create a rule
@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json['rule_string']
    ast = Node("operand", value=rule_string)  # Simple example to create a node
    return jsonify({"rule": str(ast)})

# API to combine rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rules = request.json['rules']
    operator = request.json.get('operator', 'AND')  # Default operator is AND

    # Start combining rules
    combined_ast = Node("operator", Node("operand", value=rules[0]), Node("operand", value=rules[1]), operator)

    # Combine remaining rules (if any)
    for rule in rules[2:]:
        combined_ast = Node("operator", combined_ast, Node("operand", value=rule), operator)

    return jsonify({"combined_rule": str(combined_ast)})

# API to evaluate rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    try:
        ast_data = request.json.get('ast')
        user_data = request.json.get('user_data')

        if not ast_data or not user_data:
            return jsonify({"error": "AST and user_data are required."}), 400

        # Recreate the AST from JSON
        ast = create_ast_from_json(ast_data)

        # Evaluate rule against the user data
        result = evaluate_rule(ast, user_data)

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
