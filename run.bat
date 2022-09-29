@cls
@echo off
echo Creando complemento...
scons --clean
scons
scons pot
addonPackager-1.2.1.nvda-addon