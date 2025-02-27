	$ brew install fish
	$ curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/	install | fish
	$ omf install sashimi	

To configure fish properly
	
	$ brew install fish ​
	$ fish
	$ fish_add_path /opt/homebrew/bin
	$ echo "/opt/homebrew/bin/fish" | sudo tee -a /etc/shells
	$ chsh -s /opt/homebrew/bin/fish

Note: if you end up with terminal errors, it is becase you have not done the $PATH addition correctly. 

