function sd --wraps='cd ~ && cd (find * -type d | fzf)' --description 'alias sd cd ~ && cd (find * -type d | fzf)'
  cd ~ && cd (find * -type d | fzf) $argv
        
end
