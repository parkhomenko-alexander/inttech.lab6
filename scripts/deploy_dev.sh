cd ../

pip freeze > requirements.txt
git add -A
git commit -m "[25]cicd-upgrade"
git push origin master
cd scripts