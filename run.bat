@cls
@echo off
echo Creando complemento...
scons --clean
scons
scons pot
addonPackager-1.2.nvda-addon