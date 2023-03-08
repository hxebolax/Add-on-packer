# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import globalPluginHandler
import addonHandler
import globalVars
import gui
import ui
import core
from scriptHandler import script
import wx
from threading import Thread
import os
import sys
from . import ajustes
from . import main
from .kill import kill_process_by_name

addonHandler.initTranslation()

def disableInSecureMode(decoratedCls):
	if globalVars.appArgs.secure:
		return globalPluginHandler.GlobalPlugin
	return decoratedCls

@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()

		if hasattr(globalVars, "addonPackager"):
			self.postStartupHandler()
		core.postNvdaStartup.register(self.postStartupHandler)
		globalVars.addonPackager = None

	def postStartupHandler(self):
		hilo = Thread(target=self.runSleep, daemon = True).start()

	def runSleep(self):
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.menuItem = self.toolsMenu.Append(wx.ID_ANY, _("&Utilidades para los complementos de NVDA"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.menuApp, self.menuItem)

	def terminate(self):
		try:
			self.toolsMenu.Remove(self.menuItem)
		except Exception:
			pass

		try:
			core.postNvdaStartup.unregister(self.postStartupHandler)
		except (AttributeError, RuntimeError):
			pass
		super().terminate()

	def runMsgReinicio(self):
		msg = \
_("""Hay una acción pendiente de reiniciar NVDA.

Por motivos de seguridad el complemento no podrá ser usado hasta que no reinicie.

¿Desea reiniciar NVDA ahora?""")
		message = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = message.ShowModal()
		if ret == wx.ID_YES:
			message.Destroy
			core.restart()
		else:
			message.Destroy
			ajustes.IS_WinON = False
			return

	@script(gesture=None, description= _("Muestra la ventana de Utilidades para los complementos de NVDA"), category= _("Utilidades para los complementos de NVDA"))
	def script_menuApp(self, event, menu=False):
		if ajustes.IS_WinON == False:
			if ajustes.reinicio == False:
				HiloComplemento(self, 1).start()
			else:
				ajustes.IS_WinON = True
				wx.CallAfter(self.runMsgReinicio)
		else:
				if menu:
					gui.messageBox(_("Ya hay una instancia de Utilidades para los complementos de NVDA abierta."), _("Información"), wx.ICON_INFORMATION)
				else:
					ui.message(_("Ya hay una instancia de Utilidades para los complementos de NVDA abierta."))

	def menuApp(self, event):
		wx.CallAfter(self.script_menuApp, None, True)

	@script(gesture=None, description= _("Cerrar NVDA cuando se queda bloqueado"), category= _("Utilidades para los complementos de NVDA"))
	def script_kill(self, event):
		HiloComplemento(None, 2).start()

class HiloComplemento(Thread):
	def __init__(self, frame, opcion):
		super(HiloComplemento, self).__init__()

		self.frame = frame
		self.opcion = opcion
		self.daemon = True

	def run(self):
		def appLauncherMain():
			self._main = main.VentanaPrincipal(gui.mainFrame, self.frame)
			gui.mainFrame.prePopup()
			self._main.Show()

		def killNVDA():
			kill_process_by_name("nvda.exe")

		if self.opcion == 1:
			wx.CallAfter(appLauncherMain)
		elif self.opcion == 2:
			wx.CallAfter(killNVDA)

