class Scanner:
    "Read tokens from input program"

    def __init__(self, program_str):
        self.program_str = program_str
        self.pos = 0
        self.tokens = []


    def scan(self.program_str):
        accum = ""

        pos = 0
        while pos < len(self.program_str):
            