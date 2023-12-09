import ast

class CodeManager:
    def __init__(self, path_file):
        self.path_file = path_file
        self.python_code = self._read_python_file()
        cpp_code = '''
#include <iostream>
#include "string"

using namespace std;

int main() {

'''
        cpp_code += self.translate_to_cpp()
        cpp_code += 'return 0;\n}'
        self._create_cpp_file(cpp_code)

    def _create_cpp_file(self, cpp_code):
        # Crear un nuevo archivo con las estructuras traducidas
        translation_file_path = self.path_file.replace('.py', '.cpp')
        with open(translation_file_path, 'w') as file:
            file.write(cpp_code)

    def _read_python_file(self):
        with open(self.path_file, 'r') as file:
            return file.read()

    def translate_to_cpp(self):
        try:
            parsed_tree = ast.parse(self.python_code)
            cpp_code = self._translate_node(parsed_tree)
            return cpp_code
        except SyntaxError as e:
            return f"Error de sintaxis en el archivo Python: {str(e)}"
        
    def _target_type(self, target_type):
        if 'int' in target_type:
            return 'int'
        elif 'str' in target_type:
            return 'string'
        elif 'float' in target_type:
            return 'double'
        elif 'bool' in target_type:
            return 'bool'
        
    def _translate_node(self, node):
        if isinstance(node, ast.Module):
            cpp_code = ''
            for stmt in node.body:
                cpp_code += self._translate_node(stmt)
            return cpp_code
        elif isinstance(node, ast.While):
            condition = self._translate_node(node.test)
            body_list = [self._translate_node(stmt) for stmt in node.body]
            body = " ".join(body_list)
            return f'    while ({condition}) {{\n{body}\n}}\n'
        elif isinstance(node, ast.If):
            condition = self._translate_node(node.test)
            body_list = [self._translate_node(stmt) for stmt in node.body]
            body = " ".join(body_list)
            else_body_list = [self._translate_node(stmt) for stmt in node.orelse] if node.orelse else ''
            else_body = " ".join(else_body_list)
            print(type(node.orelse))
            return f'    if ({condition}) {{\n{body}\n}} else {{\n{else_body}\n}}\n' if else_body != '' else f'    if ({condition}) {{\n{body}\n}}\n'
        elif isinstance(node, ast.Assign):
            targets = ', '.join(target.id for target in node.targets)
            value = self._translate_node(node.value)
            target_type = self._target_type(str(type(value)))
            return f'    {target_type} {targets} = {value};\n'
        elif isinstance(node, ast.Expr):
            return self._translate_node(node.value)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == 'print':
                args = ', '.join(self._translate_node(arg) for arg in node.args)
                return f'    cout << {args} << endl;\n'
        elif isinstance(node, ast.Str):
            return f'"{node.s}"'
        elif isinstance(node, ast.BinOp):
            left = self._translate_node(node.left)
            right = self._translate_node(node.right)
            op = self._translate_node(node.op)
            return f'{left} {op} {right}'
        elif isinstance(node, ast.Add):
            return '+'
        elif isinstance(node, ast.Sub):
            return '-'
        elif isinstance(node, ast.Mult):
            return '*'
        elif isinstance(node, ast.Div):
            return '/'
        elif isinstance(node, ast.Compare):
            left = self._translate_node(node.left)
            ops = ', '.join(self._translate_node(op) for op in node.ops)
            comparators = ', '.join(self._translate_node(comp) for comp in node.comparators)
            return f'{left} {ops} {comparators}'
        elif isinstance(node, ast.Eq):
            return '=='
        elif isinstance(node, ast.NotEq):
            return '!='
        elif isinstance(node, ast.Lt):
            return '<'
        elif isinstance(node, ast.LtE):
            return '<='
        elif isinstance(node, ast.Gt):
            return '>'
        elif isinstance(node, ast.GtE):
            return '>='
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Num):
            return node.n
        else:
            return '     Error'
