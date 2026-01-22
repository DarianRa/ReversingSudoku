ReversingSudoku
This Repository contains our Explainable Machine Learning Project. We aim to create a ILP Model using Popper that extracts the rules of sudoku.

Disclaimer: This project was created with the help of AI tools. We debugged, generated and improved the code. The ideas, logical structure and theoretical background of this work were developed entirely by us.

We used the NuWLS-c 2023 Engine as recommended by Andrew Cropper.

Usage of virtual environment:

python3 -m venv venv source venv/bin/activate pip3 install -r requirements.txt

python3 src/run_popper.py --bk src/popper/bk.pl --bias src/popper/bias.pl --exs src/popper/exs.pl --force-recall --timeout 1200