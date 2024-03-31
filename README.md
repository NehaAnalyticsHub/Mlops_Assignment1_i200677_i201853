# Mlops_Assignment1_i200677_i201853
# # Initialize the repository with Git
git init

# Add files
git add .

# Commit changes
git commit -m "Initial commit"

# Add the GitHub repository as a remote
git remote add origin repolink

# Push changes to GitHub
git push -u origin master

git checkout -b dev
git push -u origin dev

# Create the test branch
git checkout -b test
git push -u origin test


git checkout dev 

git merge origin/main

git merge origin/main --allow-unrelated-histories

git checkout -b test
git add .
git commit -m "Implement feature "
On branch test
git push origin test
To https://github.com/NehaAnalyticsHub/Mlops_Assignment1_i200677_i201853.git
   ec55cd9..e8af1e1  test -> test
git checkout test
git pull origin test
 * branch            test       -> FETCH_HEAD
Already up to date.
git checkout master
Switched to branch 'master'
From https://github.com/NehaAnalyticsHub/Mlops_Assignment1_i200677_i201853
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> origin/master
git pull origin master --allow-unrelated-histories         
From https://github.com/NehaAnalyticsHub/Mlops_Assignment1_i200677_i201853
 * branch            master     -> FETCH_HEAD

git merge --no-ff test
Merge made by the 'ort' strategy.
 .github/workflows/flake8.yml   | 25 +++++++++++++++++++++++++
 app.py                         |  3 ++-
 3 files changed, 54 insertions(+), 1 deletion(-)
 create mode 100644 .github/workflows/flake8.yml
 create mode 100644 .github/workflows/unittest.yml
git push origin master
Enumerating objects: 2, done.
Counting objects: 100% (2/2), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 471 bytes | 471.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/NehaAnalyticsHub/Mlops_Assignment1_i200677_i201853.git
   ec55cd9..04f2e01  master -> master
PS C:\Users\Lenovo\Desktop\i200677_i201853_MlopsA1> 


