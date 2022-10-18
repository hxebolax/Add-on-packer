# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import addonHandler
import addonAPIVersion
import globalVars
import wx
import os
import zipfile
from threading import Thread
import re
import fnmatch
import string
import random
import shutil
import json
from . import ajustes

addonHandler.initTranslation()

ADDON_API_VERSION_REGEX = re.compile(r"^(0|\d{4})\.(\d)(?:\.(\d))?$")

def getAPIVersionTupleFromString(version):
	"""Converts a string containing an NVDA version to a tuple of the form (versionYear, versionMajor, versionMinor)"""
	match = ADDON_API_VERSION_REGEX.match(version)
	if not match:
		raise ValueError(version)
	return tuple(int(i) if i is not None else 0 for i in match.groups())

def hasAddonGotRequiredSupport(addonMin, currentAPIVersion=addonAPIVersion.CURRENT):
	"""True if NVDA provides the add-on with an API version high enough to meet the add-on's minimum requirements
	"""
	return addonMin <= currentAPIVersion

def isAddonTested(addonMax, backwardsCompatToVersion=addonAPIVersion.BACK_COMPAT_TO):
	"""True if this add-on is tested for the given API version.
	By default, the current version of NVDA is evaluated.
	"""
	return addonMax >= backwardsCompatToVersion

def isAddonCompatible(
		addonMin,
		addonMax,
		currentAPIVersion=addonAPIVersion.CURRENT,
		backwardsCompatToVersion=addonAPIVersion.BACK_COMPAT_TO
):
	"""Tests if the addon is compatible.
	The compatibility is defined by having the required features in NVDA, and by having been tested / built against
	an API version that is still supported by this version of NVDA.
	"""
	return hasAddonGotRequiredSupport(addonMin, currentAPIVersion) and isAddonTested(addonMax, backwardsCompatToVersion)

def GetAddons(directory, extension):
	return [f for f in os.listdir(directory) if f.endswith(extension)]

def ponerComentario(archivo, comentario):
	with zipfile.ZipFile(archivo, 'a') as zip:
		zip.comment = comentario.encode("utf-8")

def leerComentario(archivo):
	with zipfile.ZipFile(archivo, 'r') as zip:
		comentario = zip.comment.decode("utf-8")
	return comentario

def extraeZip(fichero, destino, ficheroZip):
	try:
		with zipfile.ZipFile(ficheroZip) as archive:
			for file in archive.namelist():
				if file.startswith(fichero):
					archive.extract(file, destino)
		return True
	except:
		return False

def anadirAlZip(fichero, ficheroZip):
	try:
		with zipfile.ZipFile(ficheroZip, 'a') as zipf:
			zipf.write(fichero, os.path.basename(fichero))
		return True
	except:
		return False

def zipfolder(foldername, target_dir, addon=True, barraProgreso=False, frame=None):
	if addon:
		zipobj = zipfile.ZipFile(foldername + '.nvda-addon', 'w', zipfile.ZIP_DEFLATED)
	else:
		zipobj = zipfile.ZipFile(foldername, 'w', zipfile.ZIP_DEFLATED)
	total = 0
	rootlen = len(target_dir) + 1
	for base, dirs, files in os.walk(target_dir):
		if addon:
			if '__pycache__' in dirs:
				dirs.remove('__pycache__')
		for fname in files:
			path = os.path.join(base, fname)
			total += os.path.getsize(path)

	current = 0
	for base, dirs, files in os.walk(target_dir):
		if addon:
			if '__pycache__' in dirs:
				dirs.remove('__pycache__')
		for fname in files:
			path = os.path.join(base, fname)
			fn = os.path.join(base, fname)
			percent = 100 * current / total + 1
			if barraProgreso:
				wx.CallAfter(frame.onProgreso, int(percent))
			zipobj.write(fn, fn[rootlen:])
			current += os.path.getsize(path)
	zipobj.close()

def descomprimir_zip(frame, archivo, directorio_destino, progreso=True):
	try:
		zf = zipfile.ZipFile(archivo)
		uncompress_size = sum((file.file_size for file in zf.infolist()))
		extracted_size = 0
		for file in zf.infolist():
			extracted_size += file.file_size
			if progreso:
				progress = (lambda x, y: (int(x), int(x*y) % y/y))((extracted_size * 100/uncompress_size), 1e0)
				wx.CallAfter(frame.onProgreso, progress[0])
			zf.extract(file, directorio_destino)
		return True
	except Exception as e:
		return False

def findReplace(directory, find, replace, filePattern):
	for path, dirs, files in os.walk(os.path.abspath(directory)):
		for filename in fnmatch.filter(files, filePattern):
			filepath = os.path.join(path, filename)
			with open(filepath, 'r', errors="ignore") as file:
				fileContent = file.readlines()
			for lineIndex in range(len(fileContent)):
				if (find in fileContent[lineIndex]):
					fileContent[lineIndex] = replace
					with open(filepath, 'w', errors="ignore") as tableFile:
						tableFile.writelines(fileContent)
					break

def id_generator(tamaño=6, composicion=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
	return ''.join(random.choice(composicion) for _ in range(tamaño))

def genDirectorioTemp():
	return os.path.join(globalVars.appArgs.configPath, id_generator(15, string.ascii_uppercase + string.ascii_lowercase + string.digits))

class EmpaquetaComplementosIndividuales(Thread):
	def __init__(self, frame, seleccion, directorio):
		super(EmpaquetaComplementosIndividuales, self).__init__()

		self.frame = frame
		self.seleccion = seleccion
		self.directorio = directorio
		self.daemon = True
		self.start()

	def run(self):
		try:
			for i in self.seleccion:
				addonSave = os.path.join(self.directorio, self.frame.listAddons[i].manifest["name"] + "_" + self.frame.listAddons[i].manifest["version"].replace(":", "_") + "_Gen")
				wx.CallAfter(self.frame.onTextoEstado, _("Creando el complemento: {} {}").format(self.frame.listAddons[i].manifest["name"], self.frame.listAddons[i].manifest["version"]))
				zipfolder(addonSave, self.frame.listAddons[i].path)
				wx.CallAfter(self.frame.onProgreso, i+1)
			msg = \
_("""Se generaron correctamente todos los complementos.

Pulse aceptar para continuar.""")
			wx.CallAfter(self.frame.onCorrecto, msg)
		except Exception as e:
			msg = \
_("""Se produjo un error inesperado. 

Error: {}

Vuelva a intentarlo.""").format(e)
			wx.CallAfter(self.frame.onError, msg)

class InstalaComplementos(Thread):
	def __init__(self, frame, seleccion):
		super(InstalaComplementos, self).__init__()

		self.frame = frame
		self.seleccion = seleccion
		self.daemon = True
		self.start()

	def run(self):
		lstError = []
		num = 0
		numReinicio = 0
		try:
			for i in self.seleccion:
				num += 1
				wx.CallAfter(self.frame.onTextoEstado, _("Instalando el complemento: {}").format(self.frame.listaTemporalInstalador[1][i]))
				wx.CallAfter(self.frame.onProgreso, num)
				bundle = addonHandler.AddonBundle(self.frame.listaTemporalInstalador[0][i])
				if not addonHandler.addonVersionCheck.hasAddonGotRequiredSupport(bundle):
					pass #Podemos crear un control de errores aquí para complementos que no se pueden instalar por incompatibilidad y luego dar un mensaje
				else:
					if addonHandler.addonVersionCheck.isAddonTested(bundle):
						bundleName = bundle.manifest['name']
						isDisabled = False
						for addon in addonHandler.getAvailableAddons():
							if bundleName == addon.manifest['name']:
								if addon.isDisabled:
									isDisabled = True
								if not addon.isPendingRemove:
									addon.requestRemove()
								break
						addonHandler.installAddonBundle(bundle)
						numReinicio += 1
					else:
						lstError.append(i)
			if len(lstError) == 0:
				self.frame.reinicio = True
				msg = \
_("""Se completo la instalación correctamente.

NVDA necesita reiniciarse para aplicar las instalaciones.

¿Desea reiniciar NVDA ahora?""")
				wx.CallAfter(self.frame.onCorrecto, msg)
			else:
				if len(lstError) == len(self.frame.selectionInstall):
					self.frame.reinicio = False
					msg = \
_("""No se pudo instalar el complemento.

Fallo de compatibilidad.

Busque un complemento compatible.""")
					wx.CallAfter(self.frame.onError, msg)
				else:
					temp = []
					for i in lstError:
						temp.append(self.frame.listaTemporalInstalador[1][i])
					msg = \
_("""Se completo la instalación correctamente.

Pero hay complementos que no se pudieron instalar.

Los siguientes complementos son incompatibles, busque una versión compatible:

{}

NVDA necesita reiniciarse para aplicar las instalaciones.
¿Desea reiniciar NVDA ahora?""").format("\n".join(str(x) for x in temp))
					self.frame.reinicio = True
					wx.CallAfter(self.frame.onCorrecto, msg)
		except Exception as e:
			if numReinicio == 0:
				msg = \
_("""Se produjo un error inesperado. 

Error: {}

Vuelva a intentarlo.""").format(e)
				self.frame.reinicio = False
				wx.CallAfter(self.frame.onError, msg)
			else:
				msg = \
_("""Se produjo un error inesperado. 

Error: {}

No obstante hubo complementos que se instalaron y NVDA necesita reiniciar para aplicar los cambios.

¿Desea reiniciar NVDA ahora?""").format(e)
				self.frame.reinicio = True
				wx.CallAfter(self.frame.onCorrecto, msg)

class DesinstalaComplementos(Thread):
	def __init__(self, frame, seleccion):
		super(DesinstalaComplementos, self).__init__()

		self.frame = frame
		self.seleccion = seleccion
		self.daemon = True
		self.start()

	def run(self):
		num = 0
		numReinicio = 0
		try:
			for i in self.seleccion:
				num += 1
				wx.CallAfter(self.frame.onTextoEstado, _("Desinstalando el complemento: {}").format(self.frame.listAddons[i].manifest['summary']))
				wx.CallAfter(self.frame.onProgreso, num)
				self.frame.listAddons[i].isDisabled
				self.frame.listAddons[i].requestRemove()
				numReinicio += 1
			self.frame.reinicio = True
			msg = \
_("""Se completo la desinstalación correctamente.

NVDA necesita reiniciarse para aplicar los cambios.

¿Desea reiniciar NVDA ahora?""")
			wx.CallAfter(self.frame.onCorrecto, msg)
		except Exception as e:
			if numReinicio == 0:
				msg = \
_("""Se produjo un error inesperado. 

Error: {}

Vuelva a intentarlo.""").format(e)
				self.frame.reinicio = False
				wx.CallAfter(self.frame.onError, msg)
			else:
				msg = \
_("""Se produjo un error inesperado. 

Error: {}

No obstante hubo complementos que se desinstalaron y NVDA necesita reiniciar para aplicar los cambios.

¿Desea reiniciar NVDA ahora?""").format(e)
				self.frame.reinicio = True
				wx.CallAfter(self.frame.onCorrecto, msg)

class DirectorioConComplementos(Thread):
	def __init__(self, frame, directorio, lista):
		super(DirectorioConComplementos, self).__init__()

		self.frame = frame
		self.directorio = directorio
		self.lista = lista
		self.daemon = True
		self.start()

	def run(self):
		files = [] # Lista con los nombres de fichero
		names = [] # Lista nombres complementos
		version = [] # Lista versiones complementos
		filesNotCompatible = [] # Lista ficheros no compatibles con API
		fileError = [] # Lista que fallo al cargar el manifiesto.
		flagNotCompatible = False # Bandera compatibles
		flagNotFile = False # Bandera errores
		num = 0
		for i in self.lista:
			num += 1
			try:
				bundle = addonHandler.AddonBundle(os.path.join(self.directorio, i))
				t1 = i
				t2 = bundle.manifest['summary']
				t3 = bundle.manifest['version']
				t4 = bundle.manifest['minimumNVDAVersion']
				t5 = bundle.manifest['lastTestedNVDAVersion']
				if isAddonCompatible(t4, t5):
					files.append(os.path.join(self.directorio, t1))
					names.append(t2)
					version.append(t3)
				else:
					flagNotCompatible = True
					filesNotCompatible.append(i)
			except Exception as e:
				flagNotFile = True
				fileError.append(i)
			wx.CallAfter(self.frame.onTextoEstado, _("Buscando complementos en {}...").format(self.directorio))
			wx.CallAfter(self.frame.onProgreso, num)
		retorno = [files, names, version, filesNotCompatible, fileError, "instalador"]
		if len(retorno[0]) == 0:
			wx.CallAfter(self.frame.onError, _("No hay complementos compatibles en el directorio."), ["instalador"])
		else:
			if flagNotCompatible or flagNotFile:
				msg = \
_("""Se completo con éxito la extracción de información de los complementos.

No obstante, el directorio que introdujo contiene complementos no compatibles.

* Complementos con fallo en el manifiesto: {}.

{}

* Complementos no compatibles con la api actual: {}.

{}

Pulse aceptar para continuar.""").format(len(fileError), "\n".join(fileError), len(filesNotCompatible), "\n".join(filesNotCompatible))
				wx.CallAfter(self.frame.onCorrecto, msg, retorno)
			else:
				msg = \
_("""Se completo con éxito la extracción de información de los complementos.

Pulse aceptar para continuar.""")
				wx.CallAfter(self.frame.onCorrecto, msg, retorno)

class HabilitarDeshabilitar(Thread):
	def __init__(self, frame, listaHabilitados, listaDeshabilitados):
		super(HabilitarDeshabilitar, self).__init__()

		self.frame = frame
		self.listaHabilitados = listaHabilitados
		self.listaDeshabilitados = listaDeshabilitados

		self.daemon = True
		self.start()

	def run(self):
		num = 0
		numReinicio = 0
		try:
			if len(self.listaHabilitados) == 0:
				pass
			else:
				wx.CallAfter(self.frame.onTextoEstado, _("Deshabilitando complementos..."))
				for i in self.listaHabilitados:
					num += 1
					self.frame.listAddons[self.frame.listaComplementosHabilitados[i]].enable(False)
					numReinicio += 1
					wx.CallAfter(self.frame.onProgreso, num)

			if len(self.listaDeshabilitados) == 0:
				pass
			else:
				wx.CallAfter(self.frame.onTextoEstado, _("Habilitando complementos..."))
				for i in self.listaDeshabilitados:
					num += 1
					self.frame.listAddons[self.frame.listaComplementosdeshabilitados[i]].enable(True)
					numReinicio += 1
					wx.CallAfter(self.frame.onProgreso, num)

			self.frame.reinicio = True
			msg = \
_("""Se completo el proceso de habilitar y deshabilitar correctamente.

NVDA necesita reiniciarse para aplicar los cambios.

¿Desea reiniciar NVDA ahora?""")
			wx.CallAfter(self.frame.onCorrecto, msg)
		except Exception as e:
			if numReinicio == 0:
				msg = \
_("""Se produjo un error inesperado. 

Error: {}

Vuelva a intentarlo.""").format(e)
				self.frame.reinicio = False
				wx.CallAfter(self.frame.onError, msg)
			else:
				msg = \
_("""Se produjo un error inesperado. 

Error: {}

No obstante hubo complementos que se habilitaron o deshabilitaron y NVDA necesita reiniciar para aplicar los cambios.

¿Desea reiniciar NVDA ahora?""").format(e)
				self.frame.reinicio = True
				wx.CallAfter(self.frame.onCorrecto, msg)

class ManifiestosInstalados(Thread):
	def __init__(self, frame, selection, mayor, menor, revision):
		super(ManifiestosInstalados, self).__init__()

		self.frame = frame
		self.selection = selection
		self.mayor = mayor
		self.menor = menor
		self.revision = revision

		self.daemon = True
		self.start()

	def run(self):
		num = 0
		numReinicio = 0
		try:
			for i in self.selection:
				num += 1
				wx.CallAfter(self.frame.onTextoEstado, _("Cambiando el manifiesto al complemento: {}").format(self.frame.listAddons[i].manifest['summary']))
				findReplace(self.frame.listAddons[i].path, "lastTestedNVDAVersion", "lastTestedNVDAVersion = {}.{}.{}\n".format(self.mayor, self.menor, self.revision), "manifest.ini")
				wx.CallAfter(self.frame.onProgreso, num)
				numReinicio += 1

			self.frame.reinicio = True
			msg = \
_("""Se cambiaron los manifiestos correctamente.

Para que la acción tenga efecto NVDA tiene que reiniciarse.

¿Desea reiniciar NVDA ahora?""")
			wx.CallAfter(self.frame.onCorrecto, msg)
		except Exception as e:
			if numReinicio == 0:
				msg = \
_("""Se produjo un error inesperado. 

Error: {}

Vuelva a intentarlo.""").format(e)
				self.frame.reinicio = False
				wx.CallAfter(self.frame.onError, msg)
			else:
				msg = \
_("""Se produjo un error inesperado. 

Error: {}

No obstante hubo complementos que se les cambio el manifiesto y NVDA necesita reiniciar para aplicar los cambios.

¿Desea reiniciar NVDA ahora?""").format(e)
				self.frame.reinicio = True
				wx.CallAfter(self.frame.onCorrecto, msg)

class ManifiestosArchivo(Thread):
	def __init__(self, frame, ruta, mayor, menor, revision):
		super(ManifiestosArchivo, self).__init__()

		self.frame = frame
		self.ruta = ruta
		listaDirFichero = os.path.split(os.path.abspath(self.ruta))
		self.directorio = listaDirFichero[0]
		self.nombreFichero = os.path.splitext(listaDirFichero[1])[0]
		self.tempDirectorio = genDirectorioTemp()
		self.mayor = mayor
		self.menor = menor
		self.revision = revision

		self.daemon = True
		self.start()

	def run(self):
		try:
			wx.CallAfter(self.frame.onTextoEstado, _("Trabajando en el complemento: {}").format(self.nombreFichero + ".nvda-addon"))
			os.mkdir(self.tempDirectorio)
			descomprimir_zip(self.frame, self.ruta, self.tempDirectorio)
			wx.CallAfter(self.frame.onProgreso, 25)
			findReplace(self.tempDirectorio, "lastTestedNVDAVersion", "lastTestedNVDAVersion = {}.{}.{}\n".format(self.mayor, self.menor, self.revision), "manifest.ini")
			wx.CallAfter(self.frame.onProgreso, 52)
			addonSave = os.path.join(self.directorio, self.nombreFichero + "_Gen_modify_manifest")
			wx.CallAfter(self.frame.onProgreso, 75)
			zipfolder(addonSave, self.tempDirectorio)
			try:
				shutil.rmtree(self.tempDirectorio, ignore_errors=True)
			except:
				pass
			wx.CallAfter(self.frame.onProgreso, 100)
			msg = \
_("""Se cambio correctamente el manifiesto.

Se genero un complemento con el manifiesto cambiado en:

{}

Pulse aceptar para continuar.""").format(addonSave + ".nvda-addon")
			wx.CallAfter(self.frame.onCorrecto, msg)
		except Exception as e:
			msg = \
_("""Se produjo un error inesperado. 

Error: {}

Vuelva a intentarlo.""").format(e)
			wx.CallAfter(self.frame.onError, msg)

class crearBackup(Thread):
	def __init__(self, frame, ficheroCopia, comentario):
		super(crearBackup, self).__init__()

		self.frame = frame
		self.ficheroCopia = ficheroCopia
		self.comentario = comentario

		self.daemon = True
		self.start()

	def run(self):
		error = []
		try:
			zipobj = zipfile.ZipFile(self.ficheroCopia, 'w', zipfile.ZIP_DEFLATED)
			zipobj.close()
			ponerComentario(self.ficheroCopia, json.dumps(self.comentario))
			for i in self.comentario:
				id = i
				fichero = self.comentario.get(id)
				if id == 0: # Diccionario
					wx.CallAfter(self.frame.onTextoEstado, _("Añadiendo el directorio de diccionarios..."))
					zipfolder(os.path.join(ajustes.dirConfig, fichero), ajustes.dict_directorios.get(id), False, False)
					p = anadirAlZip(os.path.join(ajustes.dirConfig, fichero), self.ficheroCopia)
					if p:
						os.remove(os.path.join(ajustes.dirConfig, fichero))
					else:
						error.append(_("No se pudo agregar el directorio de diccionarios a la copia de seguridad."))
				if id == 1: # Perfiles
					wx.CallAfter(self.frame.onTextoEstado, _("Añadiendo el directorio de Perfiles..."))
					zipfolder(os.path.join(ajustes.dirConfig, fichero), ajustes.dict_directorios.get(id), False, False)
					p = anadirAlZip(os.path.join(ajustes.dirConfig, fichero), self.ficheroCopia)
					if p:
						os.remove(os.path.join(ajustes.dirConfig, fichero))
					else:
						error.append(_("No se pudo agregar el directorio de Perfiles a la copia de seguridad."))
				if id == 2: # Scratchpad
					wx.CallAfter(self.frame.onTextoEstado, _("Añadiendo el directorio de Scratchpad..."))
					zipfolder(os.path.join(ajustes.dirConfig, fichero), ajustes.dict_directorios.get(id), False, False)
					p = anadirAlZip(os.path.join(ajustes.dirConfig, fichero), self.ficheroCopia)
					if p:
						os.remove(os.path.join(ajustes.dirConfig, fichero))
					else:
						error.append(_("No se pudo agregar el directorio de Scratchpad a la copia de seguridad."))

				if id == 3: # Fichero configuración disparadores de perfiles
					wx.CallAfter(self.frame.onTextoEstado, _("Añadiendo el Fichero configuración disparadores de perfiles..."))
					p = anadirAlZip(ajustes.dict_directorios.get(id), os.path.join(ajustes.dirConfig, fichero))
					if p:
						z = anadirAlZip(os.path.join(ajustes.dirConfig, fichero), self.ficheroCopia)
						if z:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
						else:
							error.append(_("No se pudo agregar el Fichero configuración disparadores de perfiles a la copia de seguridad."))
					else:
						error.append(_("No se pudo agregar el Fichero configuración disparadores de perfiles a la copia de seguridad."))

				if id == 4: # Fichero de configuración gestos de entrada
					wx.CallAfter(self.frame.onTextoEstado, _("Añadiendo el Fichero de configuración gestos de entrada..."))
					p = anadirAlZip(ajustes.dict_directorios.get(id), os.path.join(ajustes.dirConfig, fichero))
					if p:
						z = anadirAlZip(os.path.join(ajustes.dirConfig, fichero), self.ficheroCopia)
						if z:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
						else:
							error.append(_("No se pudo agregar el Fichero de configuración gestos de entrada a la copia de seguridad."))
					else:
						error.append(_("No se pudo agregar el Fichero de configuración gestos de entrada a la copia de seguridad."))

				if id == 5: # Fichero de configuración de NVDA
					wx.CallAfter(self.frame.onTextoEstado, _("Añadiendo el Fichero de configuración de NVDA..."))
					p = anadirAlZip(ajustes.dict_directorios.get(id), os.path.join(ajustes.dirConfig, fichero))
					if p:
						z = anadirAlZip(os.path.join(ajustes.dirConfig, fichero), self.ficheroCopia)
						if z:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
						else:
							error.append(_("No se pudo agregar el Fichero de configuración de NVDA a la copia de seguridad."))
					else:
						error.append(_("No se pudo agregar el Fichero de configuración de NVDA a la copia de seguridad."))

				try:
					os.remove(os.path.join(ajustes.dirConfig, fichero))
				except:
					pass
				wx.CallAfter(self.frame.onProgreso, i+1)

		except Exception as e:
			error.append(e)

		if len(error) == 0:
			msg = \
_("""Se creo la copia de seguridad correctamente en:

{}

Pulse aceptar para continuar.""").format(self.ficheroCopia)
			wx.CallAfter(self.frame.onCorrecto, msg, ["copiaseguridad"])
		else:
			try:
				os.remove(self.ficheroCopia)
			except:
				pass
			if len(error) == 1:
				msg = \
_("""Se produjo el siguiente error:

{}

No se pudo crear la copia de seguridad.""").format(error[0])
				wx.CallAfter(self.frame.onError, msg, ["copiaseguridad"])
			else:
				msg = \
_("""Se produjeron los siguientes errores:

{}

No se pudo crear la copia de seguridad.""").format("\n".join(error))
				wx.CallAfter(self.frame.onError, msg, ["copiaseguridad"])

class RestaurarBackup(Thread):
	def __init__(self, frame, ficheroCopia, comentario):
		super(RestaurarBackup, self).__init__()

		self.frame = frame
		self.ficheroCopia = ficheroCopia
		self.comentario = comentario
		self.ficheroNVDA = False

		self.daemon = True
		self.start()

	def run(self):
		error = []
		try:
			for i in self.comentario:
				id = i
				fichero = self.comentario.get(id)
				if id == 0: # Diccionario
					wx.CallAfter(self.frame.onTextoEstado, _("Restaurando el directorio de diccionarios..."))
					p = extraeZip(fichero, ajustes.dirConfig, self.ficheroCopia)
					if p:
						z = descomprimir_zip(self.frame, os.path.join(ajustes.dirConfig, fichero), ajustes.dirDiccionario, False)
						if z:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
							self.ficheroNVDA = True
						else:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
							error.append(_("No se pudo restaurar el directorio de diccionarios."))
					else:
						error.append(_("No se pudo restaurar el directorio de diccionarios."))
				if id == 1: # Perfiles
					wx.CallAfter(self.frame.onTextoEstado, _("Restaurando el directorio de Perfiles..."))
					p = extraeZip(fichero, ajustes.dirConfig, self.ficheroCopia)
					if p:
						z = descomprimir_zip(self.frame, os.path.join(ajustes.dirConfig, fichero), ajustes.dirProfile, False)
						if z:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
							self.ficheroNVDA = True
						else:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
							error.append(_("No se pudo restaurar el directorio de Perfiles."))
					else:
						error.append(_("No se pudo restaurar el directorio de Perfiles."))

				if id == 2: # Scratchpad
					wx.CallAfter(self.frame.onTextoEstado, _("Restaurando el directorio de Scratchpad..."))
					p = extraeZip(fichero, ajustes.dirConfig, self.ficheroCopia)
					if p:
						z = descomprimir_zip(self.frame, os.path.join(ajustes.dirConfig, fichero), ajustes.dirScratchpad, False)
						if z:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
							self.ficheroNVDA = True
						else:
							os.remove(os.path.join(ajustes.dirConfig, fichero))
							error.append(_("No se pudo restaurar el directorio de Scratchpad."))
					else:
						error.append(_("No se pudo restaurar el directorio de Scratchpad."))

				if id == 3: # Fichero configuración disparadores de perfiles
					wx.CallAfter(self.frame.onTextoEstado, _("Restaurando el Fichero configuración disparadores de perfiles..."))
					p = extraeZip(fichero, ajustes.dirConfig, self.ficheroCopia)
					if p:
						try:
							try:
								os.remove(os.path.join(ajustes.dirConfig, "profileTriggers.ini"))
							except:
								pass
							z = descomprimir_zip(self.frame, os.path.join(ajustes.dirConfig, fichero), ajustes.dirConfig, False)
							if z:
								os.remove(os.path.join(ajustes.dirConfig, fichero))
								self.ficheroNVDA = True
							else:
								os.remove(os.path.join(ajustes.dirConfig, fichero))
								error.append(_("No se pudo restaurar el Fichero configuración disparadores de perfiles."))
						except Exception as e:
							error.append(_("No se pudo restaurar el Fichero configuración disparadores de perfiles."))
					else:
						error.append(_("No se pudo restaurar el Fichero configuración disparadores de perfiles."))

				if id == 4: # Fichero configuración gestos de entrada
					wx.CallAfter(self.frame.onTextoEstado, _("Restaurando el Fichero configuración gestos de entrada..."))
					p = extraeZip(fichero, ajustes.dirConfig, self.ficheroCopia)
					if p:
						try:
							try:
								os.remove(os.path.join(ajustes.dirConfig, "gestures.ini"))
							except:
								pass
							z = descomprimir_zip(self.frame, os.path.join(ajustes.dirConfig, fichero), ajustes.dirConfig, False)
							if z:
								os.remove(os.path.join(ajustes.dirConfig, fichero))
								self.ficheroNVDA = True
							else:
								os.remove(os.path.join(ajustes.dirConfig, fichero))
								error.append(_("No se pudo restaurar el Fichero configuración de gestos de entrada."))
						except Exception as e:
							error.append(_("No se pudo restaurar el Fichero configuración de gestos de entrada."))
					else:
						error.append(_("No se pudo restaurar el Fichero configuración gestos de entrada."))

				if id == 5: # Fichero configuración de NVDA
					wx.CallAfter(self.frame.onTextoEstado, _("Restaurando el Fichero configuración de NVDA..."))
					p = extraeZip(fichero, ajustes.dirConfig, self.ficheroCopia)
					if p:
						try:
							try:
								os.remove(os.path.join(ajustes.dirConfig, "nvda.ini"))
							except:
								pass
							z = descomprimir_zip(self.frame, os.path.join(ajustes.dirConfig, fichero), ajustes.dirConfig, False)
							if z:
								os.remove(os.path.join(ajustes.dirConfig, fichero))
								self.ficheroNVDA = True
							else:
								os.remove(os.path.join(ajustes.dirConfig, fichero))
								error.append(_("No se pudo restaurar el Fichero configuración de NVDA."))
						except Exception as e:
							error.append(_("No se pudo restaurar el Fichero configuración de NVDA."))
					else:
						error.append(_("No se pudo restaurar el Fichero configuración de NVDA."))
				wx.CallAfter(self.frame.onProgreso, i+1)
		except Exception as e:
			error.append(e)

		if len(error) == 0:
			if self.ficheroNVDA:
				msg = \
_("""La restauración fue un éxito.

Al restaurar la configuración de NVDA es necesario reiniciar el lector.

Pulse aceptar o cerrar para reiniciar.""")
				wx.CallAfter(self.frame.onCorrecto, msg, ["reiniciar"])
		else:
			if len(error) == 1:
				if self.ficheroNVDA:
					msg = \
_("""Se produjo el siguiente error:

{}

No se pudo restaurar toda la copia de seguridad.

Pero hay elementos que si pudieron ser restaurados.

Al restaurar la configuración de NVDA es necesario reiniciar el lector.

Pulse cancelar o cerrar para reiniciar.""").format(error[0])
					wx.CallAfter(self.frame.onError, msg, ["reiniciar"])
				else:
					msg = \
_("""Se produjo el siguiente error:

{}

No se pudo restaurar la copia de seguridad.

Pulse cancelar o cerrar para continuar.""").format(error[0])
					wx.CallAfter(self.frame.onError, msg, ["copiaseguridad"])
			else:
				if self.ficheroNVDA:
					msg = \
_("""Se produjeron los siguientes errores:

{}

No se pudo restaurar toda la copia de seguridad.

Pero hay elementos que si pudieron ser restaurados.

Al restaurar la configuración de NVDA es necesario reiniciar el lector.

Pulse cancelar o cerrar para reiniciar.""").format("\n".join(error))
					wx.CallAfter(self.frame.onError, msg, ["reiniciar"])
				else:
					msg = \
_("""Se produjeron los siguientes errores:

{}

No se pudo restaurar la copia de seguridad.

Pulse cancelar o cerrar para continuar.""").format("\n".join(error))
					wx.CallAfter(self.frame.onError, msg, ["copiaseguridad"])
