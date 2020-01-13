Title: The Slurm Cookbook
Date: 2018-6-10
Category: tutorials
Slug: slurm-cookbook
Authors: Pietro Marchesi
Summary: A short overview of Slurm for beginners, focused on how you can interact with it to obtain information about jobs and resources.


The Slurm Cookbook is meant to provide you with a brief overview of Slurm and a few examples of how you can interact with it and obtain information about jobs and resources.

Of course, all of the information presented here can be found by in the Slurm documentation, but if you are just getting started with Slurm it may not be obvious where to look for things.

**Note**: The Cookbook does not really cover batch scripts, because there are many other guides online which provide plenty of examples.

A three course meal
-------------------

First of all, what does Slurm actually do? Slurm is a cluster management and job scheduling system for Linux clusters (an ensemble of connected computers running Linux). As such, Slurm is mainly concerned with three things:

1.  **Allocating resources to users so that they can perform work** (by resources, we mean the computers (or nodes) which form the cluster).
    
2.  **Managing a queue of pending jobs.** As long as there are free resources on the cluster, Slurm can simply give users the resources they need. But at some point, the requests of the various users may be incompatible. It is Slurm's job to decide what to execute when, and trying to do that in a smart way so as to use the resources efficiently.
    
3.  **Handling the launch, executing, and monitoring of jobs submitted by users.**
    

The main ingredients
--------------------

Let's first get an overview of the main user commands that Slurm provides, before looking at some examples of how we can use them.

*   `squeue` allows you to view information about jobs. In particular, you will see which jobs are pending, which are running, which are completing, and which are completed. These are the states that a job will encounter throughout its lifetime assuming everything goes according to plan (but a job may also fail or be cancelled for several reasons).
*   `salloc` provides a Slurm job allocation, i.e. a set of resources. It then runs a command specified by the user, and when command is complete, frees up the job allocation.
*   `sbatch`: submit batch script to run jobs non-interactively on the compute nodes.
*   `srun` Runs parallel jobs on allocated resources (but can also request resources directly).
*   `sacct` displays accounting data (i.e. data on past jobs which are not on the queue anymore).
*   `sancel` can be used to cancel jobs on the queue, or more generally to send them signals.
*   `sinfo` gives you information about the nodes and partitions which compose the cluster, such as the number of nodes and their state.
*   `scontrol` allows you to view and modify Slurm configurations (but it's mostly for system administrators).

A handy summary of these commands together with some options can also be found [here](https://slurm.schedmd.com/pdfs/summary.pdf).

A note on `sbatch`, `salloc`, and `srun`
----------------------------------------

It may be confusing at first to distinguish between these three commands. In practice, you can think of it as follows: what `salloc` and `sbatch` do is allocate resources for jobs (i.e. they tell the system: "I need these many CPUs with this much memory "), whereas `srun` uses those resources to launch parallel jobs. The difference between `sbatch` and `salloc` is that `sbatch` is used to submit batch scripts which run non-interactively on the compute nodes, whereas `salloc` can get you the resources and allow you to run interactive commands on the nodes.

`srun` is generally launched within a job allocation, meaning that either `salloc` or `sbatch` have allocated the resources, and `srun` inherits these resources and the relevant options (which you could also overwrite). But `srun` can also fight for itself: if is called outside a job allocation, it can claim the necessary resources directly.

Some good recipes
-----------------

This part contains a few examples of how you can use some of the main user command.

### Inspecting the queue with `squeue`

Let's start simple: let's look at the current queue using `squeue`. Sometimes there may be a lot of jobs on the queue belonging to other users, which can make it difficult to check on your own jobs. You can filter the jobs that `squeue` displays by passing the `--user` parameter.

squeue --user=<myusername>

Generally `squeue` cuts the name of the job to a few characters, which can be annoying. It would be nicer to have it display the full job name. The `--format` parameter comes to the rescue
```
squeue --format="%.8i %.9P %18j %10u %.8T %.12M %9N"
```
By default Slurm only allocates 8 characters to the job name, so in the example above, for the field `j` which corresponds to job name, we can change `%.8j` to `%18j` to make sure the full name gets displayed. Removing the dot aligns the text to the left. In the [documentation for `squeue`](https://slurm.schedmd.com/squeue.html) you can find all the fields which you can pass to `--format` and format them to your liking.

Of course, we don't want to have to type this every time. What we can do instead is creating an alias. Let's copy the following into the `.bashrc` file (which is in your home directory):
```
alias squeue='squeue --format="%.8i %.9P %18j %10u %.8T %.12M %9N"'
```
Now, we can have our nicely formatted output by simply typing `squeue`.

**NOTE:** The `.bashrc` script is executed every time you start an interactive shell on the cluster (i.e. when you log in), and it can be used to initialize a bunch of useful stuff. Changes you make it will not have any effect unless you log out and log back in or directly source it by running `source ~/.bashrc`.

Note that `squeue` also supports a `--Format` parameter. Generally, `--Format` is more readable (for job name you would pass `name` instead of `j`) and has more fields (in `--format`, since it only uses single letters, at some point the letters run out), but `--format` is more flexible for formatting the output (you can't specify the number of characters using `--Format` as far as I know).

Here is an example using `--Format`:
```
squeue --user=<myusername> --Format=jobid,username,account,statecompact,starttime,timelimit,numcpus
```
* * *

### Viewing system properties and state with `sinfo`

Let's not forget to take a careful look at our cluster, as this may influence how we decide to design or run our applications. By simply running `sinfo`, we can take a look at the partitions: their availability, their state, how many nodes they have, etc.

We can also take a look at the individual nodes, using the `-N` option. To include some more information in the output (for example the memory of each node) we can pass the `-l` flag (compactly, `sinfo -Nl`).

A very useful additional field is the number of cores on each node, by using `--format` and the `C` field.
```
sinfo -N --format "%.10n %.9P %.15C %.10m %.10O %.8t"
```
On the cluster of the lab, the output looks as follows:
```
 HOSTNAMES PARTITION   CPUS(A/I/O/T)     MEMORY   CPU\_LOAD    STATE
  csn-cpu1      cpu\*        4/8/0/12      31996      10.44      mix
  csn-cpu2      cpu\*       2/10/0/12      31996       2.02      mix
  csn-cpu3      cpu\*       0/12/0/12      31996       0.01     idle
  csn-cpu4      cpu\*       1/11/0/12      31996       1.01      mix
  csn-cpu5      cpu\*       0/12/0/12      31996       0.01     idle
  csn-cpu6      cpu\*       0/40/0/40     128736       0.01     idle
  csn-cpu7      cpu\*       0/40/0/40     128735       0.01     idle
  csn-cpu8      cpu\*       0/40/0/40     128736       0.01     idle
  csn-cpu9      cpu\*      12/28/0/40     128736       8.50      mix
  csn-gpu1       gpu       4/36/0/40     257675       0.19      mix
```
Here, memory is expressed in megabytes. Note that CPUS on each node are presented in the A/I/O/T format, which stands for allocated/idle/other (offline/down)/total. You can see that the state is `idle` when no cpu cores are allocated, and `mix` when some but not all the cores are being used. The `CPU_LOAD` on the other hand is an indication of how much work we are giving to our nodes.

We can obtain a similar result with the `--Format` parameter
```
sinfo -N --Format=nodehost,cpusstate,cpusload,memory,statecompact
```
Lastly, I may want to view information only of the nodes that I am currently using. We can achieve this by first using `squeue` to find out where my jobs are running, create a variable called `mynodes` by parsing the output of `squeue`, and then use it in the call to `sinfo`:
```
mynodes=$(squeue --user=pmarche1 -o "%N" | grep csn | tr "\\n" ",")
sinfo -N --nodes "$mynodes"  --Format=nodehost,cpusstate,cpusload,memory,statecompact
```
* * *

### Reviewing past jobs with `sacct`

If we want to find out information about jobs which are not on the queue anymore (so they don't show up with `squeue`) we can resort to `sacct`.

For instance, we may be interested in finding out on which compute nodes our jobs ended up. We can specify a list of job IDs, as well as a list of fields for the `--format` option.
```
sacct --jobs=7058,7057 --format=User,JobID,account,AllocNodes,NodeList,Timelimit,elapsed,ReqMem,MaxRss,ExitCode
```
Here, the `NodeList` field will tell us on which nodes our jobs landed. `--format` supports many more fields, which you can list by `sacct --helpformat`.

Note that `sacct` by default (and if you do not specify the job IDs with `--jobs`) only shows you jobs from the current day (since midnight). To show older jobs, you can pass the `--starttime` option:
```
sacct --starttime=<mm.dd.yy>
```
`sacct` may also not display the full job name by default. To make sure that we see the full name, we can format it by adding `%` and a number of characters after each field, for instance
```
sacct --user pmarche1 --format=User,JobID,JobName%20,AllocNodes,NodeList
```
This allocates 20 characters to the field `JobName`. Again, you can use aliases to avoid having to remember the full command.

* * *

### Running interactive jobs

In some occasions we may want to run interactive jobs on one or more nodes. To do so, you can call `salloc` and then start an interactive session using `srun`.
```
salloc --partition <partition> srun -N1 --pty /bin/bash
```
In the example, we specify the partition we want to work on and the number of nodes (but we could specify other requirements for the allocation). Importantly, we have to pass the `--pty` option which tells Slurm to drop us in a `ssh` session on the node we receive. Lastly, we need to give `srun` the actual command to run: since we want an interactive session, we want to run some kind of shell, for instance `/bin/bash`.

Earlier on, I mentioned that `srun` can also be called without the help of `sbatch` or `salloc`, in which case it will go and fetch resources directly. As an example, we can in fact do:
```
srun --partition cpu --pty /bin/bash
```
* * *

### Killing jobs with `scancel`

Lastly, let's kill some jobs. The most basic way is to pass a job ID to `scancel`, for instance `scancel 3425`. But suppose you have many jobs on the queue which need to be cancelled: copy-pasting each job ID can take forever. Luckily, there are many ways in which you can constrain the `scancel` operation. For instance, you can kill all your jobs with
```
scancel --user=<myusername> 
```
Or only jobs with a certain name
```
scancel --jobname=<myjobID>
```
You can cancel only job which are in a particular state (state can be `PENDING`, `RUNNING`, `SUSPENDED`).
```
scancel --state=<state>
```
And of course combine all these options however you want.

