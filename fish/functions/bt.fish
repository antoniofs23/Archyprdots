function bt
  echo $(upower -d | grep model)
  echo $(upower -d | grep percentage)
end
