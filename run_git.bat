@cls
@echo off
scons --clean
git init
git add --all
git commit -m "Versión 1.5"
git push -u origin master
git tag 1.5
git push --tags
pause