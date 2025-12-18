import subprocess
import sudoku.sudoku

cmd = [
    "python3",
    "src/popper/lib/popper.py",
    "src/popper/"
]

result = subprocess.run(cmd, capture_output=True, text=True)

print("STDOUT:\n", result.stdout)
print("STDERR:\n", result.stderr)