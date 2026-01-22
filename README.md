# ReversingSudoku
This Repository contains our Explainable Machine Learning Project. We aim to create a ILP Model using Popper that extracts the rules of sudoku.


Usage of virtual environment:

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

python3 src/run_popper.py   --bk src/popper/bk.pl   --bias src/popper/bias.pl   --exs src/popper/exs.pl   --force-recall 1   --timeout 1200

