if status is-interactive
    # Commands to run in interactive sessions can go here
end

fish_ssh_agent

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/ant/miniforge3/bin/conda
    eval /home/ant/miniforge3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/home/ant/miniforge3/etc/fish/conf.d/conda.fish"
        . "/home/ant/miniforge3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/home/ant/miniforge3/bin" $PATH
    end
end
# <<< conda initialize <<<


fish_add_path /home/ant/.spicetify
