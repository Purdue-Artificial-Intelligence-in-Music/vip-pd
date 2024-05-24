
# PD 1: Intro to Lab Servers, GitHub, etc.

Written by Tim Nadolsky

## Introduction

Hello! This assignment is intended to teach you how to use GitHub and the lab servers. After completing this assignment you should know how to:
- Access the lab servers.
- Perform basic terminal operations in a Unix shell.
- Use Conda on the lab servers.
- Use the GitHub online interface.
- Use basic Git operations to add files to GitHub from the command line.
- Make and resolve pull requests.

Here we go!

## Part 1. Accessing the lab servers

In this section we will learn how to access the lab's servers.

First, if you are not on the Purdue academic campus, you will need to install the [Cisco AnyConnect VPN](https://it.purdue.edu/newsroom/2020/200316-webvpn.php) to access Purdue servers remotely. Once it is installed, you should login with your Purdue career account credentials to establish the connection. You will need to accept a 2FA Duo Mobile request for this.

Next, we will use the *ssh* command to establish a connection to the server. For this tutorial we will be using our lab server called *ee230lnx04.ecn.purdue.edu*. We have several other servers as well, but they are somewhat slower and should only be used if *ee230lnx04* is at capacity.

If your account exists, your username on this server should be ``<career account username>@ee230lnx04.ecn.purdue.edu``. That is, if Bob had the career account username ``billybob04``, his username would be ``billybob04@ee2...``

We can *ssh* (access a remote shell) on a computer by using the command:

``ssh <hostname>``

Thus, we can *ssh* into our account on *ee230lnx04* with the command:

``ssh <username>@ee230lnx04.ecn.purdue.edu``

Your password is your old ``<pin>,push<X>`` password from the BoilerKey days (this may be a problem if you entered Purdue in Fall 2023 or later; Teams DM a leader for help). You will also need to 2FA with Duo Mobile to login.

If your account does not exist or you can't login for whatever reason, **stop!** Teams DM a lab leader for assistance here.

At any point, if you need to exit the remote shell and return to your original terminal, you can type ``exit`` to close the ssh. You can also type ``Ctrl/Option-C`` at any time to (attempt to) stop a running command while it's running.

## Part 2. Basic shell operations

At this point, if everything else has gone correctly, you should be at a shell prompt on *ee230lnx04* under your account. If you've never used a shell before, you can basically treat this as a typing version of Windows File Explorer or macOS Finder. We anticipate that almost everyone on this team will have at least minimal prior experience working with a Unix shell, so here is a crash course on how to use a terminal plus a list of important commands.

By default, your shell prompt (e.g. a line where you can type in a command) is something of the format: 
```<username>@<hostname>:<current directory>$```

This looks complicated, but it's easier to see in practice. For example, if ``billybob04`` is following this tutorial and is in the directory ``/home/shay/``, his prompt would look something like:
```billybob04@ee230lnx04:/home/shay/$```

Here are some commands you can use to get around. To run a command, type it out and press Enter on your keyboard to run it.

- ``pwd``: Print the working (current) directory (full, unabbreviated version).
- ``ls``: List the files in your current folder.
- ``cd <directory>``: Change directory to a new folder.
- ``touch <filename>``: Create a new completely empty file with the specified filename.
- ``mkdir <directory name>``: Make a new directory with the specified name.
- ``mv <filename> <destination>``: Move the file to a new destination (can also be used to rename a file).
- ``nano <filename>``: Open the specified file with the text editor *nano*.
- ``rm <filename>``: Remove the specified file (not directory).
- ``rmdir <directory name>``: Remove the specified directory, as long as it is not empty.
- ``man <command name>``: Open a manual about a specific command to learn more. (You can also just Google the command nowadays)

Many of these commands have flags/arguments beyond what's listed here. Use the *man* command or Google to find these special flags, which allow you to do things that are tough to do in a GUI file explorer.

There are also some special directory abbreviations that Unix uses and that you can use to make your life easier.

- ``~``: Your home directory, likely ``/home/shay/a/<username>``. Use ``cd ~`` to instantly go back to your home directory (solves a lot of annoying navigation problems!)
- ``/`` (with nothing before it): the root (outermost) directory of the filesystem.
- ``.``: The current directory. Use it when you are not sure where you are running the command from or what your filesystem looks like when you run the command.
- ``..``: The parent directory of your working directory. This is more useful than meets the eye: you can use ``cd ..`` to go to the parent directory of the one you're currently in; that is, if you are in ``/home/shay/a``, you can use ``cd ..`` to go to ``/home/shay``. 

Finally, you can use the Tab key to autocomplete filenames (e.g. if you have a directory called ``SUPER_LONG_DIRECTORY_NAME``, typing *SUP* and then pressing Tab will (almost always) autocomplete the rest of the name for you).

## Part 3: Git(Hub) basics

For this part, we are going to make a basic GitHub repository and do some things in it to show how it works.

Start by going to [GitHub](https://github.com/), making an account, and making a new **private** repository called *AIM_summ24_PD1*. (This name doesn't actually matter but all our commands will be written with this name as a placeholder.)

We are now going to pull this repository to our server. To do this (and virtually all the other repository actions) we use a tool called *git*. 

First, we can clone (make a copy of) the repository on our server by running the command:
``git clone https://github.com/<username>/AIM_summ24_PD1``.
You will need to sign in to *git* using GitHub to do this step. You will need to make a personal access token in place of your password, which can be done using the instructions [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Once done, you can access the new folder using the command ``cd AIM_summ24_PD1``.

Let's have some fun now. On your own, make a new directory called ``important_things``, *cd* into that directory, make a new file called ``message.txt``, use *nano* to open the message, write something silly into the file, save and exit the file, and ``cd`` back to the parent directory.

Was that too bad? In case you're having trouble, the following sequence of commands should do the trick:
```
mkdir important_things
cd important_things
touch message.txt
nano message.txt
<Super secret nano things; use Ctrl/Option-C to exit and press Y to save the modified buffer>
cd ..
```

Now we're going to add these files to your GitHub repo(sitory). First, let's tell *git* to track your new file. We can use the command ``git add <filename>`` to tell *git* to track file(s). In this, we can type:

``git add important_things/message.txt``

Note the relative path used here and in the commands above; we don't have to type out the full path every time we want to run a command, as the shell automatically prepends ``./`` to our paths if we don't type a ``/`` first.

Next, let's tell *git* we want to commit our existing changes using the command ``git commit``.

A box will pop up with a space for you to enter a commit description in the text editor *vim*. This editor is a little less friendly but we can still work with it. Press I to enter -- INSERT -- mode (where you can write text), type a descriptive commit message (e.g. "A super secret message"), press Esc to exit -- INSERT -- mode, and type ``:wq`` and press Enter to save the file.

Finally, we can type ``git push`` to sync our changes with online.

You can use the basic process of ``git add``, ``git commit``, and ``git push`` to do 90% of the day-to-day file management you need using GitHub. The next section will cover a good chunk of the remaining 10% - specifically, how to work with others using *git* and GitHub.

## Part 4: Branches and PRs

In this section, we will cover some more advanced topics of how to work with others using *git* and GitHub.

Let's start by making a new branch. Branches allow multiple users to develop code in parallel. Users can add, commit, pull, push, and make changes to each branch independently without touching the others. GitHub and *git* allow these branches to be managed and stored much more efficiently than simply by making several working copies of starter code.

You can make a new branch using the command ``git branch <name>``. Once you make a branch, you'll need to switch to it using the command ``git checkout <branch name>``. In this case, let's make a new branch called ``new_feature`` using the commands ``git branch new_feature`` and ``git checkout new_feature``. 

Now, we need to give our branch an "upstream" source to grab its code from. To do that, we set the "upstream" branch to "main" (e.g. our original branch) using the following command:
``git branch --set-upstream-to=origin/main new_feature``.

Let's now grab our files from GitHub. To do this, we can use the ``git pull`` command, which synchronizes our local repository with GitHub's files. (You should get a message that your files are up-to-date since we haven't made any changes.)

To test this branch, use the terminal to modify your copy of ``important_things/message.txt``. Once you're done, ``git add``, ``git commit``, and ``git push`` the changes. You might have to use ``git push origin HEAD`` to get the changes to appear on GitHub.

Once you're done, you should be able to use the branch switcher (top-left quarter drop-down menu on your repo's homepage) to see both the ``main`` and ``new_feature`` branches. In particular, notice that the copy of ``message.txt`` on ``main`` contains your original message, while the copy on ``new_feature`` contains your new message.

How do we synchronize the two branches? By making a pull request! This is most easily done with the GitHub GUI. To make a pull request, go to the GitHub page for your repo, select the ``new_feature`` branch, and go to Pull requests -> New pull request, base = ``main`` and compare = ``new_feature``.  Add a descriptive message for your pull request (e.g. "Merging the new copy of message.txt into the main branch") and click "Create pull request".

In this case, you should be able to merge the branches automatically, so go ahead and click "Merge pull request" to perform the merge. The branches should now both have the new copy of ``message.txt``.

Do **NOT** delete the old branch once you're done. It will be necessary for the exercises below.

## Part 5. Git summary + tips

These are the very basics of how to use GitHub, ``git``, the Unix shell, and our lab's servers. In general, here are the basic steps you need to use GitHub correctly:

1. Clone the repo to your local machine.
2. Create/switch to a new branch for development.
3. ``git pull`` to update your local files.
4. Do your development.
5. ``git add``, ``git commit``, and ``git push`` your files to GitHub.
6. When you are ready to merge your development branch with the main branch, make a pull request using GitHub's GUI.
7. Merge the PR (with approval from grad student mentors and student leaders) and start over at step 2. 

Here are some things you should never do on GitHub or lab machines as well (some funnier, some less so).

**NEVER** trust anyone who asks you to run ``rm -rf <anything>`` on your computer without understand what they are asking you to do. This command recursively deletes anything in the path specified and will destroy your filesystem (unrecoverable).

**NEVER** write a vague or non-detailed commit/PR message. Good messages help others understand what changes you've made to the code and in what capacity. Poorly written messsages make it harder for others to understand what was done in the past to the code (and to recover from disaster if a repository/branch gets wrecked for whatever reason). 

**NEVER** push directly to the "master"/"main" branch in any repository with multiple branches - always make a new branch for each new feature. Pushing directly to master defeats one of the most powerful tools of GitHub and makes it exponentially harder for others to collaborate with you. In addition, if you break the master branch with a push, anyone attempting to use the master branch as a source for a new branch will also pull a broken branch, further propagating errors in the system.

## Part 6: Quick Conda overview

Finally, in this tutorial, we will be doing a quick overview of *conda*. *conda* is a Python environment manager, which allows you to have multiple Python installations on the same user/machine. 

We utilize a shared *conda* installation, in which environments are shared between users. This is to save disk space from installing packages many times, as well as to avoid disk space limitations from ECN on user account space.

To activate our shared *conda* instance, run the following commands in your shell. You will need to run this every time you log in, or add it to your ``.bashrc`` (not recommended, yet).

```
export PATH=/home/ee230lnx04/a/shared-conda/bin:$PATH
source /home/ee230lnx04/a/shared-conda/etc/profile.d/conda.sh
```

Then, to verify that this worked, run ``conda info --envs``. You should see the following output:

```
base                     /home/ee230lnx04/a/shared-conda
ddsp_actual              /home/ee230lnx04/a/shared-conda/envs/ddsp_actual
md-gpu                   /home/ee230lnx04/a/shared-conda/envs/md-gpu
... (some other output)
```

If these environments do not show up, Teams DM Tim ASAP so we can sort this out.

Since these environments are shared, we will not be creating shared environments for this tutorial. Instead, we will create a local environment and demo some things so you get an idea of how it works.

Let's create a new *conda* environment using ``conda create``. Normally, we would use the ``--name`` option to simply create it in the default directory, but instead, we will use the ``--prefix`` option to specify a path for it. (When you create an environment in the default directory, you can simply type the name for the environment everywhere you would type the prefix, making things much simpler.)

Create a new dir at ``~/envs`` to store your environments. Make a new environment called ``test_env`` using the command ``conda create --prefix ~/envs/test_env``.

The environment location should show as (full path) ``~/envs/test_env``.

Once done, you should activate the environment using ``conda activate ~/envs/test_env``. Now, all commands run relating to Python or *conda* will be run using this environment's copy of Python.

Let's make some changes to the environment. Install Python 3.8 using ``conda install python==3.8`` and Numpy 1.23.0 using ``pip install numpy==1.23.0``. 

If you did this correctly, you should be able to open a live shell of Python by typing ``python``. The Python version shown should be ``3.8.0`` (not ``3.11.5`` or any other version), and ``import numpy`` should not throw an error. You can use ``exit()`` to exit Python once this completes.

Before we deactivate, let's print our current environment to a file using the command ``conda env export >> test_env.yml``. 

Once this is done, use ``conda deactivate`` to deactivate the environment. Now, notice that if you open Python without the environment activated, it opens Python ``3.11.5`` at the time of writing (which is what is pre-installed on ECN servers).

As a final trick, we'll show off one more capability of *conda*. First, let's remove our environment ``test_env`` using the command ``conda env remove --prefix ~/envs/test_env``.

Then, we can recreate it using the ``.yml`` file we exported earlier using the command ``conda env create -f test_env.yml --prefix ~/envs/test_env``. You can verify that everything works the same as before.

Thus, by exporting and sharing your ``.yml`` environment files, you can easily share environments to multiple computers/users easily.

## Reminder:

After completing this assignment, you should know how to:
- Access the lab servers.
- Perform basic terminal operations in a Unix shell.
- Use Conda on the lab servers.
- Use the GitHub online interface.
- Use basic Git operations to add files to GitHub from the command line.
- Make and resolve pull requests.
If some of this isn't clear, please go back and re-read/re-do some of the exercises above.

## Exercises (must submit these!)

1. To prove you aren't doing this on your local Linux/Mac machine or on Colab, run the command ``nvidia-smi >> smi_output.txt``, which outputs information about installed Nvidia GPUs to a text file called ``smi_output.txt`` in your working directory. If you're on the right server, you should get a block of text containing the words "Quadro RTX 6000" somewhere in the middle when the file is opened with *nano* or *vim*.
2. If ``~/envs/test_env`` isn't available as a *conda* environment, add it back using the steps above. Then, install ``matplotlib==3.7.5`` using *pip* and export the environment to a file called ``test_env_modified.yml``.
3. Make a new branch in your GitHub repository above called ``new_feature_2`` based off ``main`` AFTER completing the tutorial exercise. Pull it to your machine, put both ``smi_output.txt`` and ``test_env_modified.yml`` in this branch. Then, ``git add``, ``git commit``, and ``git push`` the files. Finally. PR/merge the result. Make sure to write descriptive commit messages at every step! Do **NOT** delete the old branch(es) after merging with main.

Once you are ready to turn in this exercise, you should have a GitHub repo with 3 branches (``main``, ``new_feature``, ``new_feature_2``). ``main`` should contain your modified ``message.txt``, ``smi_output.txt``, and ``test_env_modified.yml``. Details on how to turn this in are TBD.

