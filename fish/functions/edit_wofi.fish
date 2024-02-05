function edit_wofi --wraps='=nvim /home/ant/.config/wofi/style.cc' --wraps='nvim /home/ant/.config/wofi/style.cc' --wraps='nvim /home/ant/.config/wofi/style.css' --description 'alias edit_wofi=nvim /home/ant/.config/wofi/style.css'
  nvim /home/ant/.config/wofi/style.css $argv
        
end
