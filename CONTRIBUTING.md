# Contributing

Contributing to this repository, we follow [Ansible Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html) in all our interactions within the project.

## Issue tracker

Whether you are looking for an opportunity to contribute or you found a bug and already know how to solve it, please go to the [issue tracker](https://github.com/ansible-collections/community.mysql/issues).
There you can find feature ideas to implement, reports about bugs to solve, or submit an issue to discuss your idea before implementing it which can help choose a right direction initially and potentially save a lot of time and effort.
Also somebody can already start discussing or working on implementing the same or similar idea,
so you can cooperate to create a better solution together.

## Open pull requests

Look through currently [open pull requests](https://github.com/ansible-collections/community.mysql/pulls).
You can help by reviewing them. There can be good pull requests which are not merged only because there are a lack of reviews. Also there can be worth, reviewed, but abandoned ones, which you could politely ask the original authors to complete yourself.
And it is always worth saying that good reviews are often more valuable than pull requests themselves.

## Looking for an idea to implement

First, see the paragraphs above.

If you came up with a new feature, it is always worth creating an issue
before starting to write code to discuss the idea with the community first.

## Step-by-step guide how to get into development quickly

We assume you use Linux as a work environment (you can use a virtual machine as well).

1. Install ``docker``, launch it.

2. Clone the [ansible-core](https://github.com/ansible/ansible) repository:
```bash
git clone https://github.com/ansible/ansible.git
```
3. Go to the cloned repository and prepare the environment:
```bash
cd ansible && source hacking/env-setup
pip install -r requirements.txt
cd ~
```
4. Create the following directories in your home directory:
```bash
mkdir -p ~/ansible_collections/community/mysql
```

5. Fork the ``community.mysql`` repository via the GitHub web interface.

6. Clone the forked repository from your profile to the created path:
```bash
git clone https://github.com/YOURACC/community.mysql.git ~/ansible_collections/community/mysql
```

7. Go there:
```bash
cd ~/ansible_collections/community/mysql
```

8. Be sure you are in the main branch:
```bash
git status
```

9. Show remotes. There should be the ``origin`` repository only:
```bash
git remote -v
```

10. Add the ``upstream`` repository:
```bash
git remote add upstream https://github.com/ansible-collections/community.mysql.git
```

11. Update your local ``main`` branch:
```bash
git fetch upstream
git merge upstream/main
```

12. Create a branch for your changes:
```bash
git branch -b name_of_my_branch
```

13. It can be a good approach is to start with writing integration tests if applicable.

Note: If there are any difficulties with writing the tests or you are not sure if the case can be covered, feel free to skip this step.
If needed, other contributors can help you with it later.

All integration tests are stored in ``tests/integration/targets`` subdirectories.
You are interested in a subdirectory containing a name of module you are going to change.
For example, if you are fixing the ``mysql_user`` module, its tests are in ``tests/integration/targets/test_mysql_user/tasks``

There is the ``main.yml`` file which includes other test files.
Look for a suitable one to integrate your tests or create and include a dedicated one.
You can use one of the existing as a draft.

When fixing a bug, write a task which reproduces the bug from the issue.

Put the reported case in the tests, then run integration tests with the following command:
```bash
ansible-test integration test_mysql_user --docker -vvv > ~/test.log
```
If the tests do not want to run, first, check you complete step 3 of this guide.

If the tests ran successfully, there are usually two possible outcomes:
a) If the bug has not appeared and the tests have passed successfully, ask the reporter to provide more details. The bug can be not a bug actually or can relate to a particular software version used or specifics of local environment configuration.

b) The bug has appeared and the tests has failed as expected showing the reported symptoms.

14. Fix the bug.

15. Run ``flake8``:
```bash
flake8 /path/to/changed/file
```
It is worth installing and running and ``flake8`` against the changed file(s) first.
It shows unused imports, which is not shown by sanity tests, as well as other common issues.

16. Run sanity tests:
```bash
ansible-test sanity /path/to/changed/file --docker
```
If they failed, look at the output carefully - it is usually very informative and helps to identify a problem line quickly.
Sanity failings usually relate to wrong code and documentation formatting.

17. Run integration tests:
```bash
ansible-test integration test_mysql_user --docker -vvv > ~/test.log
```

There are two possible outcomes:
a) They have failed. Look into the ``test.log``.
Errors are usually at the end of the file.
Fix the problem place in the code and run again.
Repeat the cycle until the tests pass.

b) They have passed. Remember they failed originally? Our congratulations! You has probably fixed the bug, though we hope not introducing a couple of new ones;)

18. Commit your changes with an informative but short commit message:
```bash
git add /path/to/changed/file
git commit -m "mysql_user: fix crash when ..."
```

19. Push the branch to the ``origin`` (your fork):
```bash
git push origin name_of_my_branch
```

20. Go to the ``upstream`` (http://github.com/ansible-collections/community.mysql).

21. Go to ``Pull requests`` tab and create a pull request.

GitHub is tracking your fork, so it should see the new branch in it and automatically offer
to create a pull request. Sometimes GitHub does not do it and you should click the ``New pull request`` button yourself.
Then choose ``compare across forks`` under the ``Compare changes`` title.
Choose your repository and the new branch you pushed in the right drop-down list.
Confirm. Fill out the pull request template with all information you want to mention.
Put "Fixes + link to the issue" in the pull request's description.
Put "[WIP] + short description" in the pull request's title.
Click ``Create pull request``.

22. Add a [changelog fragment](https://docs.ansible.com/ansible/devel/community/development_process.html#changelogs) to the ``changelog/fragments`` directory. It will be published in release notes, so users will know about the fix.

23. The CI tests will run automatically on Red Hat infrastructure after every commit.

You will see their status in the bottom of your pull request.
If they are green, remove "[WIP]" from the title. Mention the issue reporter in a comment and let contributors know that the pull request is "Ready for review".

24. Wait for reviews.

25. If the pull request looks good to the community, committers will merge it.

For details, refer to the [Ansible developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html).

If you find any inconsistencies or places in this document which can be improved, feel free to raise an issue or pull request to fix it.