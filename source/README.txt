-----------------------
DESCRIPTION OF FOLDERS:
-----------------------
1. Folder - DATA: 		Contains .txt files for each network, downloaded from SNAP (e.g. wiki-Vote.txt)
2. Folder - OUTPUTS: 	Contains .gz files outputed by computing largest connected components. Format of the file is 'wiki-Vote_LSCC.gz' and 'wiki-Vote_LWCC.gz'
3. Folder - UTILITIES:	Contains two python scripts.
						Remove_duplicates.py is used to remove duplicates from 'gplus_combined.txt', and outputs 'ego-Gplus.txt'. Both files must be in DATA folder. 
						bitmask.py contains helper functions that compute bitmasks
4. Folder - NETWORKX:	Contains python scripts (unusued now) that utilize NetworkX library. Abandoned due to limited working RAM.
5. Folder - Custom:		Contains custom DFS implementation for computing LCCs. Abandoned due to limited working RAM and NetworkX issues.
6. Root:				Contains various Python scripts for each task.

-----------------------
DESCRIPTION OF FILES:
-----------------------
1. main_igraph.py:		Defines 3 functions. 
						task_1() is used to compute exact statistics.
						task_2_1() is used to compute approximate statistics for all datasets, for some fixed accuracy parameter values.
						task_2_2() is used to generate plots for variable parameter values, for 1 dataset (wiki-vote in our case)
2. task_0_igraph.py:	Self-contained script. main() function is used to compute LSCC and LWCC for all 4 datasets. (Runs out of memory while computing for Pokec and GPlus)
3. task_1_igraph.py:	Computes exact statistics on a given Graph, implements parallelization. (Runs out of memory when computing Median for soc-Epinions, later values were abandoned)
4. task_2_igraph.py:	task_2_1() computes approximate statistics for fixed values of num_samples and k (num_bitmask)
						task_2_2() computes approximate statistics for 1 dataset, using pre-defined ranges for num_samples and k
						
-----------------------
HOW TO RUN:
-----------------------
### Step 1:
-> Install python-igraph. Unofficial .whl package is available for Windows. For Linux, C core has to be installed first.
-> Place all .txt files of each dataset in "data" folder. Cross-verify the names defined in the array inside task_0_igraph.py. Run task_0_igraph.py().

### Step 2:
-> Install Pandas. 
-> Run Remove_duplicates.py script to shrink ego-Gplus dataset.

### Step 3:
-> Install Numpy.
-> Run main_igraph.py, by commenting out task_2 functions. This will execute task_1 function, and will generate LSCC and LWCC in .gz format inside "outputs" folder for each dataset. 
-> Note: Depends on availabe RAM

### Step 4:
-> Run main_igraph.py, by commenting task_1 and task_2_2 functions. This will compute approximate statistics for each dataset for pre-defined samples = 20 and k = 4. 
-> Note: ANF_Basic requires O(k (log n)) Memory. The computation will take time.

### Step 5:
-> Run main_igraph.py, by commenting task_1 and task_2_1 functions. This will compute approximate statistics for wiki-Vote dataset for both LSCC and LWCC, for range of samples and k. This will generate plots. 