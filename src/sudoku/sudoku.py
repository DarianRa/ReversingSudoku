import random

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
                self.validity = False
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
        lines = []
        head = "pos(valid_sudoku(" if self.validity else "neg(valid_sudoku("
        lines.append(head)
        lines.append("sudoku(")

        # rows
        for i in range(9):
            row = sudoku[i*9:(i+1)*9]
            row_str = ",".join(str(j) for j in row)
            lines.append(f"row([{row_str}]),")


        # columns
        for i in range(9):
            col = sudoku[i::9]
            col_str = ",".join(str(j) for j in col)
            lines.append(f"col([{col_str}]),")


        # blocks
        blocks = [[] for _ in range(9)]
        for i, ch in enumerate(sudoku):
            r, c = divmod(i, 9)
            b = (r // 3) * 3 + (c // 3)
            blocks[b].append(ch)

        for idx, block in enumerate(blocks):
            block_str = ",".join(str(j) for j in block)
            # last block has no trailing comma
            comma = "," if idx < 8 else ""
            lines.append(f"block([{block_str}]){comma}")

        lines.append("))).")
        

        return "\n".join(lines)

    
    def print_exs_format_fake_duplicate(self, type='row', idx=0) -> str:
        if not hasattr(self, "validity"):
            self.validator()

        if not self.validity:
            return ""

        sudoku = self.values
        lines = []

        lines.append("neg(valid_suduoku(")
        lines.append("sudoku(")

        # rows
        for i in range(9):
            row = sudoku[i*9:(i+1)*9]
            if type == 'row' and idx == i:
                row = ["1"] * 9
            row_str = ",".join(str(j) for j in row)
            lines.append(f"row([{row_str}]),")

        lines.append("")

        # columns
        for i in range(9):
            col = sudoku[i::9]
            if type == 'col' and idx == i:
                col = ["1"] * 9
            col_str = ",".join(str(j) for j in col)
            lines.append(f"col([{col_str}]),")

        lines.append("")

        # blocks
        blocks = [[] for _ in range(9)]
        for i, ch in enumerate(sudoku):
            r, c = divmod(i, 9)
            b = (r // 3) * 3 + (c // 3)
            blocks[b].append(ch)

        for b_idx, block in enumerate(blocks):
            if type == 'block' and idx == b_idx:
                block = ["1"] * 9
            block_str = ",".join(str(j) for j in block)
            comma = "," if b_idx < 8 else ""
            lines.append(f"block([{block_str}]){comma}")

        lines.append("))).")

        return "\n".join(lines)

    '''
    This function will create 3 wrong examples. Each error type will be isolated in each of the examples.
    The first part will choose a random number between 0 and 8 and will create an error in that specific row.
    The second part will do the same and create an error in a column.
    The third will do the same for each block.
    '''
    def print_exs_format_isolated_errors(self, type='row', idx=0) -> str:
            if not hasattr(self, "validity"):
                self.validator()

            if not self.validity:
                return ""

            self.values
            lines = []
            lines.append(self.print_exs_format()+"\n")


            # creating erroneous columns
            error_row = random.randint(0,8)
            error_1_column = random.randint(0,8)
            seed = random.randint(0,1)
            check = error_1_column%3
            if check == 0:
                if seed == 0:
                    error_2_column = error_1_column + 1 
                else:
                    error_2_column = error_1_column + 2
            elif check == 1:
                if seed == 0:
                    error_2_column = error_1_column - 1 
                else:
                    error_2_column = error_1_column + 1
            else:
                if seed == 0:
                    error_2_column = error_1_column - 2 
                else:
                    error_2_column = error_1_column - 1 

            print(f"debug: selected row: {error_row}, switched collums: {error_1_column}, {error_2_column}")
            
            value_1 = self.values[error_row*9 + error_1_column]
            value_2 = self.values[error_row*9 + error_2_column]

            false_sudoku_values = list(self.values).copy()
            false_sudoku_values[error_row*9 + error_1_column] = value_2
            false_sudoku_values[error_row*9 + error_2_column] = value_1
            false_sudoku_values = "".join(false_sudoku_values)
            false_sudoku_row = sudoku(false_sudoku_values)
            lines.append(false_sudoku_row.print_exs_format()+"\n")


            # creating erroneous rows
            error_column = random.randint(0,8)
            error_1_row = random.randint(0,8)
            seed = random.randint(0,1)
            check = error_1_row%3
            if check == 0:
                if seed == 0:
                    error_2_row = error_1_row + 1 
                else:
                    error_2_row = error_1_row + 2
            elif check == 1:
                if seed == 0:
                    error_2_row = error_1_row - 1 
                else:
                    error_2_row = error_1_row + 1
            else:
                if seed == 0:
                    error_2_row = error_1_row - 2 
                else:
                    error_2_row = error_1_row - 1

            print(f"debug selected collum: {error_column}, switched rows: {error_1_row}, {error_2_row}")


            value_1 = self.values[error_1_row*9 + error_column]
            value_2 = self.values[error_2_row*9 + error_column]

            false_sudoku_values = list(self.values).copy()
            false_sudoku_values[error_1_row*9 + error_column] = value_2
            false_sudoku_values[error_2_row*9 + error_column] = value_1
            false_sudoku_values = "".join(false_sudoku_values)
            false_sudoku_column = sudoku(false_sudoku_values)
            lines.append(false_sudoku_column.print_exs_format()+"\n")

            # creating erroneous blocks
            row_1_index = random.randint(0,8)
            check = row_1_index//3
            seed = random.randint(0,5)

            if check == 0:
                row_2_index = 3 + seed
            elif check == 2:
                row_2_index = seed
            else:
                if seed < 3:
                    row_2_index = seed
                else:
                    row_2_index = seed + 3

            print(f"debugging blocks, switched rows: {row_1_index}, {row_2_index}")

            row_1 = self.values[row_1_index*9:(row_1_index+1)*9]
            row_2 = self.values[row_2_index*9:(row_2_index+1)*9]

            row_1 = list(row_1).copy()
            row_2 = list(row_2).copy()

            false_sudoku_block_values = list(self.values).copy()

            false_sudoku_block_values[row_1_index*9:(row_1_index+1)*9] = row_2
            false_sudoku_block_values[row_2_index*9:(row_2_index+1)*9] = row_1

            false_sudoku_block = sudoku("".join(false_sudoku_block_values))
            lines.append(false_sudoku_block.print_exs_format()+"\n")

            return "\n".join(lines)

            # one example for 



        