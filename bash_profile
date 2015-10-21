some bash defaults

export PS1="\[\e[0;36m\][\u@\h:\W \$(git branch 2>/dev/null | grep '^*' | colrm 1 2)]$ \[\e[m\]"

alias dir='ls -la'
