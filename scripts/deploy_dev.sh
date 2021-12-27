source ../env/Scripts/activate
pwd
which pip
pip freeze > requirements.txt
git add -A
git commit -m "[25]cicd-upgrade"
git push origin master