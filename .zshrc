export ZSH=$HOME/.oh-my-zsh

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

MAILCHECK=0
ZSH_THEME="3den"
CASE_SENSITIVE="true"

# OSgaews-
export PATH=$PATH:/bin
export PATH=$PATH:/usr/bin
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:/sbin
export PATH=$PATH:/usr/sbin
export PATH=$PATH:/usr/X11/bin
export PATH=$PATH:$HOME/bin

source $ZSH/oh-my-zsh.sh

DOTS=$HOME/dotfiles
source $DOTS/.langs
source $DOTS/.general
source $SCRIPTS/.kuberc

alias source_zsh='source ~/.zshrc'
alias open_zsh='subl ~/.zshrc'

# Editor Sublime
export EDITOR='subl -w'
alias subl-wd='$HOME/Library/Application\ Support/Sublime\ Text\ 3/Packages/User'

