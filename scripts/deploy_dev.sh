source ../env/Scripts/activate
pwd
pip freeze > requirements.txt
git add -A
git commit -m "[25]cicd-upgrade"
git push origin master