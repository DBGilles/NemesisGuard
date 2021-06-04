# NemesisGuard

This repository contains the source code for NemesisGuard, a tool for automatically closing a novel category of timing side-channels caused by 
instruction timing differences in branches of secret dependent conditional jumps. 
These side channels were first introduced in the paper [Nemesis: Studying microarchitectural timing leaks in rudimentary CPU interrupt logic](https://people.cs.kuleuven.be/~jo.vanbulck/ccs18.pdf). 

## abstract 
Protected Module Architectures are a promising line of research to safeguard sensitive
applications executing in an untrusted operating system. These architectures ensure
that an untrusted OS is prevented from accessing the module’s code or data. Recent
research has shown, however, that PMAs are still vulnerable to controlled-channel
attacks, a type of side-channel attack that leverages the attacker’s high level of
control over the OS to open additional side-channels.

One such attack is Nemesis. Nemesis exploits the CPU’s interrupt mechanism
to leak micro-architectural timings from protected modules. The attacker is able
to infer information about the secret-dependent control flow of a program based on
differences in instruction timings in branches of conditional jump instructions. This
thesis proposes a novel algorithm for automatically transforming existing binaries
to close these timing leaks. Additional instructions are inserted into branches of a
conditional jump instruction to ensure that corresponding instructions have identical
latencies, making the branches indistinguishable to an attacker who is able to observe
instruction timings. The proposed algorithm applies these transformations through
the use of binary rewriting. Unlike previous solutions that require either recompilation
of the source code, or modifications to the hardware, the proposed algorithm can be
applied to commercial off-the-shelf binaries. This makes it an attractive solution for
use in the field.

An implementation is presented for the Intel x86_64 architecture. A number
of experiments are performed to evaluate the effectiveness and correctness of the
algorithm. The results indicate that the proposed solution effectively close all timing
leaks without altering the program outcome.

## installation:

1. This repository extends RetroWrite. A slightly modified version of retroWrite is included as a third-party module. make sure this module has been cloned properly
 	```
	git submodule init 
	git submodule update 
	```
2. Inside the retrowrite submodule run the script `setup.h`. This scripts downloads some needed files and creates the virtual environment that will be used to run the code 
	```
	cd third-party/retrowrite 
	./setup.sh
	```
3. activate the virtual environmnet
	```
	source third-party/retrowrite/retro/bin/activate```
	```
3. Two directories need to be added to PYTHONPATH in order for the code to work properly. To do so run the following command before running the code 
	```
	source set_path.sh
	```
	
4. make sure `graphviz` is installed 
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
