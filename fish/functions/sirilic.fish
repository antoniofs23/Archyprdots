function sirilic --wraps='python /home/ant/sirilic/sirilic/Sirilic.pyw' --description 'alias sirilic=python /home/ant/sirilic/sirilic/Sirilic.pyw'
  conda deactivate
  python /home/ant/sirilic/sirilic/Sirilic.pyw $argv
        
end
