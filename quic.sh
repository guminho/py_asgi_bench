dst=$1
ruff check --select I --fix $dst
ruff format $dst