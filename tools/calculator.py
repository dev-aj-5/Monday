import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def evaluate(expression):

    def _eval(node):

        if isinstance(node, ast.Constant):
            return node.value

        elif isinstance(node, ast.BinOp):

            return OPERATORS[type(node.op)](
                _eval(node.left),
                _eval(node.right)
            )

        elif isinstance(node, ast.UnaryOp):

            return OPERATORS[type(node.op)](
                _eval(node.operand)
            )

        raise TypeError(node)

    tree = ast.parse(expression, mode="eval")

    return _eval(tree.body)