function pacman_logs --wraps='cat /var/log/pacman.log' --description 'alias pacman_logs cat /var/log/pacman.log'
  cat /var/log/pacman.log $argv
        
end
