class sudoku:
    '''this class represents a sudoku.'''
    
    ''' This is the constructor of the class and sets the values attribute to the numbers given as a string.
    The sudoku is saved in values in form of an 81 character string, which represents all of the rows concatenated starting with row#1.
        So row#1 + row#2 + ... + row#9'''
    def __init__(self, numbers: str):
        
        if( len(numbers) != 81) :
            raise ValueError(f"Expected 81 characters, but got {len(numbers)}.")
        if( not numbers.isdigit()):
            raise ValueError(f"A Sudoku may only contain digits as characters")
        
        self.values = numbers




    def validator(self)-> bool:
        sudoku = list(self.values)

        def check_list(s: list)-> bool:
            seen = set()
            for x in s:
                if x in seen:
                    return False
                else:
                    seen.add(x)
            return True

        for i in range(9):
            row = sudoku[i*9:(i+1)*9]
            valid_row = check_list(row)
            if not valid_row:
                self.validity = False
                return
        
        for i in range(9):
            collum = sudoku[i::9]
            valid_collum = check_list(collum)
            if not valid_collum:
                self.validity
                return
        
        blocks = [[] for _ in range(9)]
        for i,ch in enumerate(sudoku):
            r, c = divmod(i,9)
            b = (r//3) * 3 + (c//3)
            blocks[b].append(ch)
        for i in blocks:
            valid_box = check_list(i)
            if not valid_box:
                self.validity = False
                return
            
        self.validity = True
        return
    



    def solver():
        pass

    

    def prettyprint(self):
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
    
    def print_exs_format(self) -> str:
        if not hasattr(self, "validity"):
            self.validator()
        sudoku = self.values
        result_string = ""
        if self.validity:
            result_string = result_string + "pos(valid_sudoku(\n"
        else:
            result_string = result_string + "neg(valid_suduoku(\n"
        
        for i in range(9):
            row = sudoku[i*9:(i+1)*9]
            result_string += "  row(["
            for j in row:
                result_string += f"{j}, "
            result_string += "]),\n"
        result_string += "\n"
        for i in range(9):
            collum = sudoku[i::9]
            result_string += "  col(["
            for j in collum:
                result_string += f"{j}, "
            result_string += "]),\n"
        result_string += "\n"

        blocks = [[] for _ in range(9)]
        for i,ch in enumerate(sudoku):
            r, c = divmod(i,9)
            b = (r//3) * 3 + (c//3)
            blocks[b].append(ch)
        for i in blocks:
            result_string += "block(["
            for j in i:
                result_string += f"{j}, "
            result_string += "]),\n"
        result_string += "))."
        return result_string