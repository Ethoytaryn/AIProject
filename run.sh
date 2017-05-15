rsync -e ssh -avz ./* omen:~/neural
ssh omen -t 'python3.5 ~/neural/main.py && exit'
