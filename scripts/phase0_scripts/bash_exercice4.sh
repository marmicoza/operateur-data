#!/bin/bash
DATE=$(date +%Y-%m-%d)
mkdir -p sessions

for i in 1 2 3 4 5; do
    mkdir -p sessions/session_$i
    cat > sessions/session_$i/notes.md << EOF
# Session $i
Date : $DATE
Notes : 
EOF
done