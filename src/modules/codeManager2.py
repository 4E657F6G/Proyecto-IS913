class CodeManager:

    def __init__(self, path_file):
        self.path_file = path_file
        self.run(self.path_file)

    def read_file(self):
        with open(self.path_file, "r") as f:
            self.code = f.read()

    def translate_code(self):
        self.translated_code = ""
        for line in self.code.split("\n"):
            self.translated_code += self._translate_line(line)

    def _translate_line(self, line):
        line = line.strip()
        if line.startswith("class"):
            return self._translate_class(line)
        elif line.startswith("while"):
            return self._translate_while(line)
        elif line.startswith("print"):
            return self._translate_print(line)
        elif line.startswith("if"):
            return self._translate_if(line)
        else:
            return line

    def _translate_class(self, line):
        line = line.replace(":", " {\n")
        return line 

    def _translate_while(self, line):
        line = line.replace(":", "{\n")
        line = line.replace("True", "true")
        line = line.replace("False", "false")
        return line

    def _translate_print(self, line):
        line = line.replace("print(", "std::cout <<")
        line = line.replace(")", ";")
        return line

    def _translate_if(self, line):
        line = line.replace("True", "true")
        line = line.replace("False", "false")
        line = line.replace(":", " {")
        line += "\n}"
        return line

    def write_file(self, path_output):
        new_file_cpp= path_output.replace('.py', '.cpp')
        with open(new_file_cpp, "w") as f:
            f.write(self.translated_code)

    def run(self, path_output):
        self.read_file()
        self.translate_code()
        self.write_file(path_output)