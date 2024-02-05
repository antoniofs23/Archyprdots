function update_configs
	# copy all config files to git repo
	cd ~/.config/
	cp -r -v kitty/ fish/ waybar/ wofi/ hypr/ nvim/ ~/Archyprdots
  cp /var/log/pacman.log ~/Archyprdots/logs
	# push to github
	cd ~/Archyprdots

	git add .
	git commit -m "automated-updating"
	git push
end
