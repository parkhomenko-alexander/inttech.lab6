git add -A
cd ..
pip freeze > requirements.txt
git commit -m "[25]cicd-upgrade"
git push origin master