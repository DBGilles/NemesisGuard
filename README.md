# NemesisGuard
## installation:

1. Make sure RetroWrite has been cloned 
	`git submodule init`
	`git submodule update`

2. in retrowrite run setup.sh   
  This script creates the virtual environment that will be used

3. make sure third-party/retrowrite is added to the Python path (so that all imports work) :
	```
	source addtopathscript.sh
	```

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

## Running the program
NemesisGuard provides two tools. The first tool can be used to visualize the CFG of a given function in a binary. The second 
tool aligns a given binary.

### Visualizing CFG 
To visualize a CFG run the following command 
```
python3 nemesisguard.py -b path/to/binary -f function_name -o path/to/optional_output_dir 
```
If no output directory is given then all images are written to the directory `output`. 
###
To align a CFG run the following command 
```
python3 nemesisguard.py -b path/to/binary -t instr1 instr2 ... instrn -o path/to/optional_output_dir
```
This tool outputs a modified assembly file. 
This assembly file can be compiled using any compiler. 


## Evaluation 
The algorithm has been evaluated using Jupyter notebooks to make the interaction easier. These can be found in ... 
