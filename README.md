# NemesisGuard
installation:

1. if appicable, download retrowrite. run 
	`git submodule init`
	`git submodule update`

2. in retrowrite run setup.sh 
	this creates an environment in git clone and installs some capstone stuff 
3. make sure third-party/retrowrite is added to the Python path (so that all imports work) :

to run code first activatethe ma

1. make sure the retrowrite submodule is cloned properly. if not run 
	```
	git submodule init 
	git submodule update
	```
2. create the virtual environment by running the retrowrite setup. in `third-part/retrowrite` run `setup.sh`
3. activate the virtual environmnet
	```
	source third-party/retrowrite/retro/bin/activate```
	```
4. make sure `graphviz` is installer 
	```
	sudo apt-get install graphviz graphviz-dev
	```

4. Install the required packages 
	```
	pip install -r requirements.txt
	```
5. run program 
