# some bash defaults and useful funcs

export PS1="\[\e[0;36m\][\u@\h:\W \$(git branch 2>/dev/null | grep '^*' | colrm 1 2)]$ \[\e[m\]"

alias dir='ls -la'

alias dir='ll -a'

zpli () {zenpack --link --install $1; if [ $? -eq 0 ]; then zenoss restart; fi;}

function cdx() {
  dir=$(find /x -maxdepth 1 -iname "*$1*" | head -n 1)
  if [ -n "$dir" ]; then
    cd $dir
  fi
}
export -f cdx

