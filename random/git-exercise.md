#git exercises: navigate a repository#

[for reference][("https://jvns.ca/blog/2019/08/30/git-exercises--navigate-a-repository/")]


##exercise##

1.Check out matz’s commit of Ruby from 1998. The commit ID is '3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4'. Find out how many lines of code Ruby was at that time.

   code:
	    '''git checkout 3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4'''
		'''git branch'''
		'''git log --shortstat --author="matz" --since 1998'''

2.Check out the current master branch

   code:
	    '''git checkout master'''

3.Look at the history for the file 'hash.c'. What was the last commit ID that changed that file?

   code:
		'''git log hash.c'''
		'''git log --oneline -n 1 hash.c'''

4.Get a diff of how hash.c has changed in the last 20ish years: compare that file on the master branch to the file at commit '3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4'

   code:
		'''git diff master 3db12e8b236ac8f88db8eb4690d10e4a3b8dbcd4 hash.c | head -n 20'''

5.Find a recent commit that changed 'hash.c' and look at the diff for that commit

   code:
		'''git log -n 1 --pretty=format:%H -- hash.c'''

6.This repository has a bunch of tags for every Ruby release. Get a list of all the tags

   code:
		'''git tag|head'''

7.Find out how many files changed between tag v1_8_6_187 and tag v1_8_6_188

   code:
		'''git diff v1_8_6_187 v1_8_6_188 --stat'''

8.Find a commit (any commit) from 2015 and check it out, look at the files very briefly, then go back to the master branch.

   code:
		'''git log --shortstat --since 2015'''

9.Find out what commit the tag v1_8_6_187 corresponds to.

   code:
		'''git rev-list -n v1_8_6_187'''

10.List the directory '.git/refs/tags'. Run 'cat .git/refs/tags/v1_8_6_187' to see the contents of one of those files.

   code:
		'''ls .git/refs/tags'''
		'''cat .git/refs/tags/v1_8_6_187'''

11.Find out what commit ID 'HEAD' corresponds to right now.

   code:
		'''git rev-list -n 1 HEAD'''

12.Find out how many commits have been made to the test/ directory.

   code:
		'''git log --oneline --test | wc -l'''

13.Get a diff of lib/telnet.rb between the commits 65a5162550f58047974793cdc8067a970b2435c0 and 9e3d9a2a009d2a0281802a84e1c5cc1c887edc71. How many lines of that file were changed?

   code:
		'''git diff --stat 65a5162550f58047974793cdc8067a970b2435c0  9e3d9a2a009d2a0281802a84e1c5cc1c887edc71 -- lib/telnet.rb'''

14.How many commits were made between Ruby v2.5.1 and v2.5.2 (tags v2_5_1 and v2_5_3) (this one is a tiny bit tricky, there’s more than one step)

   code:
		'''git log --oneline v2.5.1..v2.5.2| wc -l'''

15.How many commits were authored by matz (Ruby’s creator)?

   code:
		'''git log --oneline --author=matz |wc -l'''

16.What’s the most recent commit that included the word tkutil?

   code:
		'''git log -n 1 --grep tkutil '''

17.Check out the commit e51dca2596db9567bd4d698b18b4d300575d3881 and create a new branch that points at that commit.

   code:
		'''git branch new e51dca2596db9567bd4d698b18b4d300575d3881'''
		'''git branch'''

18.Run 'git reflog'to see all the navigating of the repository you’ve done so far

   code:
		'''git reflog'''



















