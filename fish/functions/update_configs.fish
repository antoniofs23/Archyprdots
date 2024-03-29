function update_configs
	# copy all config files to git repo
	cd ~/.config/
	cp -r -v kitty/ fish/ waybar/ wofi/ hypr/ nvim/ swaylock/ swaync/ ~/Archyprdots
  pacman -Q > ~/Archyprdots/logs/packages.txt

  # push to github
	cd ~/Archyprdots
	git add .
	git commit -m "automated-updating"
	git push

  # cd back home
end
