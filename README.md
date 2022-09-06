# Dictionary Inverted Index 

Challenge:  Build an inverted index (Big Data context)

By Jacky Barraza 

 

# **Approach Taken**

Considering the dataset and the goal of inverted index, I develop a short program using Spark SQL, where the files are loaded from a directory in hdfs, which will allow handle big data through the distributed file system. 

 

# **Architecture**

Files input: taken from the URL and translate to an ubuntu virtual machine, where Hadoop was setup and Jupiter Notebooks too. 

Processing: Code was built in Spark SQL in a notebook called: [**SQL-SparkJackyB.ipynb**](https://1drv.ms/u/s!AgUr9Sk0RNaAgqcm-Y-q4rpRyfcIkQ?e=i5Up6F)

Files output: hdfs path. 

 

# **Performance**

The execution of the code till get the results was done in less of 3min with the dataset provide. No error shows. Check html file: [**SQL-SparkJackyB.html**](https://1drv.ms/u/s!AgUr9Sk0RNaAgqcsLHZCwzzk029TmQ?e=O3AbNA)

 

# **Testing**

The beginning code was test with a small set of files, in order to build, review, revised and advance.

**Executing the code in your system**

**Needs: hdfs setup, Jupiter Notebook**

1. Files to test need to be in hdfs. Save the path where those are located

2. Create in hdfs a folder for the outputs and save the path

3. Open the notebook provide called [**SQL-SparkJackyB.ipynb**](https://1drv.ms/u/s!AgUr9Sk0RNaAgqcm-Y-q4rpRyfcIkQ?e=i5Up6F) and change the path with the inputs file located in hdfs (step1) in the cell 4.

4. Run the notebook

   

# **Improving the proposal**

The code can be implemented also doing streaming using Kafka or Nifi. Once the connection is done, a notebook running spark streaming will get the new information added to the path in hdfs. The new data will be analyzed, and the dictionary index will be updated. This can be saved in a database such as MongoDB, in a bucket or where the data lake is located. 

 

# **Backup History of the process**

As a first approach I was using python to build the program, but I couldn’t get the setup for python reading from a hdfs connection. I tried to install several libraries such as pydoop, pyarrow snakebite or hdfs3, no success in the process, which took me to the approach presented above. 

 

The result of the time inverted is a python that created the inverted index dictionary and you need to provide the path and some words if you want to perform a query. I attached a notebook and the script with the file, running with a data test. The application: Running it in the secret book collection.

 

If you want to run the notebook, remember to have the path where your data is located. 

 

1. Script: Inverted_Index_Test_JackyB-toScript2.py

2. Notebook: Inverted_Index_Test_JackyB-toScript2.ipynb

   

 

 

 

 