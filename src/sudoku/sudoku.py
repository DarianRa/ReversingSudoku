class sudoku:
    '''this class represents a sudoku.'''
    
    ''' This is the constructor of the class and sets the values attribute to the numbers given as a string'''
    def __new__(self, numbers: str):
        
        if( len(numbers) != 81) :
            raise ValueError(f"Expected 81 characters, but got {len(numbers)}.")
        if( not numbers.isdigit()):
            raise ValueError(f"A Sudoku may only contain digits as characters")
        
        ''' The sudoku is saved here in form of an 81 character string, which represents all of the rows concatenated starting with row#1.
        So row#1 + row#2 + ... + row#9'''
        self.values = numbers



    def validator():
        pass

    def solver():
        pass

    def printer(self):

        def cell(ch: str) -> str:
            return "." if ch in ("0", ".") else ch


        lines = []
        border = "+-------+-------+-------+"
        lines.append(border)

        for r in range(9):
            row = []
            for c in range(9):
                row.append(cell(self.values[r * 9 + c]))

            lines.append(
                "| " + " ".join(row[0:3]) +
                " | " + " ".join(row[3:6]) +
                " | " + " ".join(row[6:9]) + " |"
            )

            if r in (2,5,8):
                lines.append(border)
        return "\n".join(lines)