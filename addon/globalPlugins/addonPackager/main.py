# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import addonHandler
import gui
from gui.nvdaControls import CustomCheckListBox
import core
import winsound
import wx
import os
from . import utilidades
from . import ajustes

addonHandler.initTranslation()

class VentanaPrincipal(wx.Dialog):
	def __init__(self, parent):
		super(VentanaPrincipal, self).__init__(parent, -1)

		ajustes.IS_WinON = True
		self.SetSize((1000, 800))
		self.SetTitle(_("Utilidades para los complementos de NVDA"))

		self.listAddons = list(addonHandler.getAvailableAddons())
		self.IS_Active = False
		self.reinicio = False
		self.listaTemporalInstalador = None
		self.listaComplementosHabilitados = []
		self.listaComplementosdeshabilitados = []
		self.dirDocumentacion = []

		self.panel_principal = wx.Panel(self, wx.ID_ANY)

		sizer_principal = wx.BoxSizer(wx.VERTICAL)

		self.lista = wx.Listbook(self.panel_principal, wx.ID_ANY)
		sizer_principal.Add(self.lista, 1, wx.EXPAND, 0)
#####
		self.panel_empaquetador = wx.Panel(self.lista, wx.ID_ANY)
		self.lista.AddPage(self.panel_empaquetador, _("Empaquetador de complementos"))

		sizerEmpaquetador = wx.BoxSizer(wx.VERTICAL)

		label_1 = wx.StaticText(self.panel_empaquetador, wx.ID_ANY, _("&Lista de complementos:"))
		sizerEmpaquetador.Add(label_1, 0, wx.EXPAND, 0)

		self.listbox_empaquetador = CustomCheckListBox(self.panel_empaquetador, wx.ID_ANY)
		sizerEmpaquetador.Add(self.listbox_empaquetador, 1, wx.EXPAND, 0)

		sizerEmpaquetadorBotones = wx.BoxSizer(wx.HORIZONTAL)
		sizerEmpaquetador.Add(sizerEmpaquetadorBotones, 0, wx.EXPAND, 0)

		self.seleccionEmpaquetadorBTN = wx.Button(self.panel_empaquetador, 101, _(u"&Selección"))
		sizerEmpaquetadorBotones.Add(self.seleccionEmpaquetadorBTN, 2, wx.CENTRE, 0)

		self.generaEmpaquetadorBTN = wx.Button(self.panel_empaquetador, 102, _("&Generar"))
		sizerEmpaquetadorBotones.Add(self.generaEmpaquetadorBTN, 2, wx.CENTRE, 0)
#####
		self.panel_instalador = wx.Panel(self.lista, wx.ID_ANY)
		self.lista.AddPage(self.panel_instalador, _("Instalador múltiple"))

		sizerInstalador = wx.BoxSizer(wx.VERTICAL)

		self.directorioInstaladorBTN = wx.Button(self.panel_instalador, 103, _("&Seleccione un directorio con complementos a instalar..."))
		sizerInstalador.Add(self.directorioInstaladorBTN, 0, wx.EXPAND, 0)

		label_3 = wx.StaticText(self.panel_instalador, wx.ID_ANY, _("&Lista de complementos:"))
		sizerInstalador.Add(label_3, 0, wx.EXPAND, 0)

		self.listbox_Instalador = CustomCheckListBox(self.panel_instalador, wx.ID_ANY)
		sizerInstalador.Add(self.listbox_Instalador, 1, wx.EXPAND, 0)

		sizerInstaladorBotones = wx.BoxSizer(wx.HORIZONTAL)
		sizerInstalador.Add(sizerInstaladorBotones, 0, wx.EXPAND, 0)

		self.seleccionInstaladorBTN = wx.Button(self.panel_instalador, 104, _(u"&Selección"))
		sizerInstaladorBotones.Add(self.seleccionInstaladorBTN, 2, wx.CENTRE, 0)

		self.instalaBTN = wx.Button(self.panel_instalador, 105, _("&Instalar"))
		sizerInstaladorBotones.Add(self.instalaBTN, 2, wx.CENTRE, 0)
#####
		self.panel_desinstala = wx.Panel(self.lista, wx.ID_ANY)
		self.lista.AddPage(self.panel_desinstala, _("Desinstala complementos"))

		sizerDesinstalador = wx.BoxSizer(wx.VERTICAL)

		label_4 = wx.StaticText(self.panel_desinstala, wx.ID_ANY, _("&Lista de complementos:"))
		sizerDesinstalador.Add(label_4, 0, wx.EXPAND, 0)

		self.listbox_Desinstalador = CustomCheckListBox(self.panel_desinstala, wx.ID_ANY)
		sizerDesinstalador.Add(self.listbox_Desinstalador, 1, wx.EXPAND, 0)

		sizerDesinstaladorBotones = wx.BoxSizer(wx.HORIZONTAL)
		sizerDesinstalador.Add(sizerDesinstaladorBotones, 0, wx.EXPAND, 0)

		self.seleccionDesinstaladorBTN = wx.Button(self.panel_desinstala, 106, _(u"&Selección"))
		sizerDesinstaladorBotones.Add(self.seleccionDesinstaladorBTN, 2, wx.CENTRE, 0)

		self.desinstalarBTN = wx.Button(self.panel_desinstala, 107, _("&Desinstalar"))
		sizerDesinstaladorBotones.Add(self.desinstalarBTN, 2, wx.CENTRE, 0)
#####
		self.panel_habidesabi = wx.Panel(self.lista, wx.ID_ANY)
		self.lista.AddPage(self.panel_habidesabi, _("Habilita / deshabilita complementos"))

		sizerHabiDesabi = wx.BoxSizer(wx.VERTICAL)

		label_5 = wx.StaticText(self.panel_habidesabi, wx.ID_ANY, _("&Lista de complementos habilitados:"))
		sizerHabiDesabi.Add(label_5, 0, wx.EXPAND, 0)

		self.listbox_habilitados = CustomCheckListBox(self.panel_habidesabi, wx.ID_ANY)
		sizerHabiDesabi.Add(self.listbox_habilitados, 2, wx.EXPAND, 0)

		label_6 = wx.StaticText(self.panel_habidesabi, wx.ID_ANY, _("&Lista de complementos deshabilitados:"))
		sizerHabiDesabi.Add(label_6, 0, wx.EXPAND, 0)

		self.listbox_deshabilitados = CustomCheckListBox(self.panel_habidesabi, wx.ID_ANY)
		sizerHabiDesabi.Add(self.listbox_deshabilitados, 2, wx.EXPAND, 0)

		sizerHabiDesabiBotones = wx.BoxSizer(wx.HORIZONTAL)
		sizerHabiDesabi.Add(sizerHabiDesabiBotones, 0, wx.EXPAND, 0)

		self.seleccionHabiDesabiBTN = wx.Button(self.panel_habidesabi, 108, _(u"&Selección"))
		sizerHabiDesabiBotones.Add(self.seleccionHabiDesabiBTN, 2, wx.CENTRE, 0)

		self.procesarHabiDesabiBTN = wx.Button(self.panel_habidesabi, 109, _("&Procesar"))
		sizerHabiDesabiBotones.Add(self.procesarHabiDesabiBTN, 2, wx.CENTRE, 0)
#####
		self.panel_manifiestos = wx.Panel(self.lista, wx.ID_ANY)
		self.lista.AddPage(self.panel_manifiestos, _("Modificador de manifiestos"))

		sizerManifiestos = wx.BoxSizer(wx.VERTICAL)

		label_7 = wx.StaticText(self.panel_manifiestos, wx.ID_ANY, _("&Lista de complementos instalados:"))
		sizerManifiestos.Add(label_7, 0, wx.EXPAND, 0)

		self.listbox_manifiestos = CustomCheckListBox(self.panel_manifiestos, wx.ID_ANY)
		sizerManifiestos.Add(self.listbox_manifiestos, 1, wx.EXPAND, 0)

		sizerVersionesManifiesto = wx.BoxSizer(wx.HORIZONTAL)
		sizerManifiestos.Add(sizerVersionesManifiesto, 0, wx.EXPAND, 0)

		label_8 = wx.StaticText(self.panel_manifiestos, wx.ID_ANY, _(u"Seleccione versión Mayor:"))
		sizerVersionesManifiesto.Add(label_8, 0, 0, 0)

		self.choiceMayor = wx.Choice(self.panel_manifiestos, wx.ID_ANY)
		sizerVersionesManifiesto.Add(self.choiceMayor, 1, wx.EXPAND, 0)

		label_9 = wx.StaticText(self.panel_manifiestos, wx.ID_ANY, _(u"Seleccione versión Menor:"))
		sizerVersionesManifiesto.Add(label_9, 0, 0, 0)

		self.choiceMenor = wx.Choice(self.panel_manifiestos, wx.ID_ANY)
		sizerVersionesManifiesto.Add(self.choiceMenor, 1, wx.EXPAND, 0)

		label_10 = wx.StaticText(self.panel_manifiestos, wx.ID_ANY, _(u"Seleccione una revisión:"))
		sizerVersionesManifiesto.Add(label_10, 0, 0, 0)

		self.choiceRevision = wx.Choice(self.panel_manifiestos, wx.ID_ANY)
		sizerVersionesManifiesto.Add(self.choiceRevision, 1, wx.EXPAND, 0)

		sizerManifiestosBotones = wx.BoxSizer(wx.HORIZONTAL)
		sizerManifiestos.Add(sizerManifiestosBotones, 0, wx.EXPAND, 0)

		self.seleccionManifiestosBTN = wx.Button(self.panel_manifiestos, 110, _(u"&Selección"))
		sizerManifiestosBotones.Add(self.seleccionManifiestosBTN, 2, wx.CENTRE, 0)

		self.procesoManifiestoBTN = wx.Button(self.panel_manifiestos, 111, _("&Procesar"))
		sizerManifiestosBotones.Add(self.procesoManifiestoBTN, 2, wx.CENTRE, 0)
#####
		self.panel_documentacion = wx.Panel(self.lista, wx.ID_ANY)
		self.lista.AddPage(self.panel_documentacion, _(u"Documentación de complementos"))

		sizerDocumentacion = wx.BoxSizer(wx.VERTICAL)

		label_11 = wx.StaticText(self.panel_documentacion, wx.ID_ANY, _("&Lista de complementos:"))
		sizerDocumentacion.Add(label_11, 0, wx.EXPAND, 0)

		self.listbox_documentacion = wx.ListBox(self.panel_documentacion, wx.ID_ANY)
		sizerDocumentacion.Add(self.listbox_documentacion, 1, wx.EXPAND, 0)

		self.verDocumentacionBTN = wx.Button(self.panel_documentacion, 112, _(u"&Abrir documentación del complemento"))
		sizerDocumentacion.Add(self.verDocumentacionBTN, 0, wx.EXPAND, 0)
#####
		sizer_estado = wx.BoxSizer(wx.VERTICAL)
		sizer_principal.Add(sizer_estado, 0, wx.EXPAND, 0)

		label_2 = wx.StaticText(self.panel_principal, wx.ID_ANY, _("&Estado:"))
		sizer_estado.Add(label_2, 0, wx.EXPAND, 0)

		self.textEstado = wx.TextCtrl(self.panel_principal, wx.ID_ANY, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		sizer_estado.Add(self.textEstado, 1, wx.EXPAND, 0)

		self.progreso = wx.Gauge(self.panel_principal, wx.ID_ANY, 10)
		sizer_estado.Add(self.progreso, 0, wx.EXPAND, 0)

		sizer_Estado_Botones = wx.BoxSizer(wx.HORIZONTAL)
		sizer_estado.Add(sizer_Estado_Botones, 0, wx.EXPAND, 0)

		self.aceptarBTN = wx.Button(self.panel_principal, 197, _("&Aceptar"))
		sizer_Estado_Botones.Add(self.aceptarBTN, 2, wx.CENTRE, 0)

		self.cancelarBTN = wx.Button(self.panel_principal, 198, _("&Cancelar"))
		sizer_Estado_Botones.Add(self.cancelarBTN, 2, wx.CENTRE, 0)

		self.cerrarBTN = wx.Button(self.panel_principal, 199, _("Cerrar"))
		sizer_Estado_Botones.Add(self.cerrarBTN, 0, 2, wx.CENTRE, 0)

		self.panel_documentacion.SetSizer(sizerDocumentacion)

		self.panel_manifiestos.SetSizer(sizerManifiestos)

		self.panel_habidesabi.SetSizer(sizerHabiDesabi)

		self.panel_desinstala.SetSizer(sizerDesinstalador)

		self.panel_instalador.SetSizer(sizerInstalador)

		self.panel_empaquetador.SetSizer(sizerEmpaquetador)

		self.panel_principal.SetSizer(sizer_principal)

		self.Layout()
		self.CenterOnScreen()
		self.eventos()

	def eventos(self):
		self.Bind(wx.EVT_CHECKLISTBOX, self.OnSelection, self.listbox_empaquetador)
		self.Bind(wx.EVT_CHECKLISTBOX, self.OnSelection, self.listbox_Instalador)
		self.textEstado.Bind(wx.EVT_CONTEXT_MENU, self.onPasar)
		self.Bind(wx.EVT_BUTTON,self.onBoton)
		self.Bind(wx.EVT_CHAR_HOOK, self.onkeyVentanaDialogo)
		self.Bind(wx.EVT_CLOSE, self.onSalir)
		self.onEstado()
		self.inicio()

	def onEstado(self):
		self.listbox_Instalador.Disable()
		self.seleccionInstaladorBTN.Disable()
		self.instalaBTN.Disable()
		self.textEstado.Disable()
		self.aceptarBTN.Disable()
		self.cancelarBTN.Disable()

	def inicio(self):
		for i in self.listAddons:
			self.listbox_empaquetador.Append(i.manifest["summary"])
			self.listbox_Desinstalador.Append(i.manifest["summary"])
			if addonHandler.Addon(i.path).getDocFilePath():
				self.listbox_documentacion.Append(i.manifest["summary"])
				self.dirDocumentacion.append(addonHandler.Addon(i.path).getDocFilePath())

		del self.listaComplementosHabilitados[:]
		del self.listaComplementosdeshabilitados[:]
		for i in range(0, len(self.listAddons)):
			if self.listAddons[i].isDisabled:
				self.listbox_deshabilitados.Append(self.listAddons[i].manifest["summary"])
				self.listaComplementosdeshabilitados.append(i)
			else:
				self.listbox_habilitados.Append(self.listAddons[i].manifest["summary"])
				self.listaComplementosHabilitados.append(i)

		self.listbox_empaquetador.SetSelection(0)
		self.listbox_Desinstalador.SetSelection(0)
		self.listbox_habilitados.SetSelection(0)
		self.listbox_documentacion.SetSelection(0)

		if len(self.listaComplementosdeshabilitados) == 0:
			self.listbox_deshabilitados.Disable()
		else:
			self.listbox_deshabilitados.SetSelection(0)

		for i in self.listAddons:
			ver = i.manifest["lastTestedNVDAVersion"]
			verFin = ".".join(str(e) for e in ver)
			self.listbox_manifiestos.Append("{} - {}".format(i.manifest["summary"], verFin))
		self.listbox_manifiestos.SetSelection(0)

		self.choiceMayor.Append(ajustes.mayor)
		self.choiceMayor.SetSelection(1)
		self.choiceMenor.Append(ajustes.menor)
		self.choiceMenor.SetSelection(0)
		self.choiceRevision.Append(ajustes.revision)
		self.choiceRevision.SetSelection(0)

	def onPasar(self, event):
		return

	def OnSelection(self, event):
		pass

	def onProgreso(self, event):
		self.progreso.SetValue(event)

	def onTextoEstado(self, event):
		self.textEstado.Clear()
		self.textEstado.AppendText(event)

	def onCorrecto(self, event, lista=None):
		self.listaTemporalInstalador = lista
		self.progreso.SetValue(0)
		winsound.MessageBeep(0)
		self.IS_Active = False
		self.textEstado.Clear()
		self.textEstado.AppendText(event)
		self.textEstado.SetInsertionPoint(0) 
		self.aceptarBTN.Enable()
		self.cerrarBTN.Enable()

	def onError(self, event, lista=None):
		self.listaTemporalInstalador = lista
		self.progreso.SetValue(0)
		winsound.MessageBeep(16)
		self.IS_Active = False
		self.textEstado.Clear()
		self.textEstado.AppendText(event)
		self.textEstado.SetInsertionPoint(0) 
		self.cancelarBTN.Enable()
		self.cerrarBTN.Enable()

	def onBoton(self, event):
		id = event.GetId()
		if id == 101: # Botón seleccion empaquetador. 
			self.menu = wx.Menu()
			item1 = self.menu.Append(1, _("&Seleccionar todo"))
			item2 = self.menu.Append(2, _("&Deseleccionar todo"))
			self.menu.Bind(wx.EVT_MENU, self.onSeleccion)
			self.seleccionEmpaquetadorBTN.PopupMenu(self.menu)
		elif id == 102: # Botón generar empaquetador.
			self.selection = [i for i in range(self.listbox_empaquetador.GetCount()) if self.listbox_empaquetador.IsChecked(i)]
			if len(self.selection) == 0:
				gui.messageBox(_("Tiene que seleccionar un complemento para continuar."), _("Error"), wx.ICON_ERROR)
				self.listbox_empaquetador.SetFocus()
			else:
				dlg = wx.DirDialog(self, _("Seleccione un directorio:"), style=wx.DD_DEFAULT_STYLE)
				if dlg.ShowModal() == wx.ID_OK:
					self.directorySave =dlg.GetPath()
					dlg.Destroy()
					self.IS_Active = True
					self.progreso.SetRange(len(self.selection))
					self.lista.Disable()
					self.cerrarBTN.Disable()
					self.textEstado.Enable()
					self.textEstado.SetFocus()
					utilidades.EmpaquetaComplementosIndividuales(self, self.selection, self.directorySave)
				else:
					dlg.Destroy()
		elif id == 103: # Botón selecciona directorio con complementos instalador.
			dlg = wx.DirDialog(self, _("Seleccione un directorio:"), style=wx.DD_DEFAULT_STYLE)
			if dlg.ShowModal() == wx.ID_OK:
				self.dirInstalador = dlg.GetPath()
				dlg.Destroy()
				x = utilidades.GetAddons(self.dirInstalador, ".nvda-addon")
				if len(x) == 0:
					gui.messageBox(_("No se encontraron complementos en el directorio que selecciono."), _("Información"), wx.ICON_INFORMATION)
					self.directorioInstaladorBTN.SetFocus()
				else:
					self.listaTemporalInstalador = None
					self.IS_Active = True
					self.progreso.SetRange(len(x))
					self.lista.Disable()
					self.cerrarBTN.Disable()
					self.textEstado.Enable()
					self.textEstado.SetFocus()
					utilidades.DirectorioConComplementos(self, self.dirInstalador, x)
			else:
				dlg.Destroy()
		elif id == 104: # Botón seleccion instalador. 
			self.menu = wx.Menu()
			item1 = self.menu.Append(3, _("&Seleccionar todo"))
			item2 = self.menu.Append(4, _("&Deseleccionar todo"))
			self.menu.Bind(wx.EVT_MENU, self.onSeleccion)
			self.seleccionInstaladorBTN.PopupMenu(self.menu)
		elif id == 105: # Botón instalar instalador. 
			self.selectionInstall = [i for i in range(self.listbox_Instalador.GetCount()) if self.listbox_Instalador.IsChecked(i)]
			if len(self.selectionInstall) == 0:
				gui.messageBox(_("Necesita elegir al menos un complemento para continuar."), _("Error"), wx.ICON_ERROR)
				self.listbox_Instalador.SetFocus()
			else:
				self.IS_Active = True
				self.progreso.SetRange(len(self.selectionInstall))
				self.lista.Disable()
				self.cerrarBTN.Disable()
				self.textEstado.Enable()
				self.textEstado.SetFocus()
				utilidades.InstalaComplementos(self, self.selectionInstall)
		elif id == 106: # Botón seleccion desinstalador. 
			self.menu = wx.Menu()
			item1 = self.menu.Append(5, _("&Seleccionar todo"))
			item2 = self.menu.Append(6, _("&Deseleccionar todo"))
			self.menu.Bind(wx.EVT_MENU, self.onSeleccion)
			self.seleccionDesinstaladorBTN.PopupMenu(self.menu)
		elif id == 107: # Botón desinstalar desinstalador. 
			self.selectionUninstall = [i for i in range(self.listbox_Desinstalador.GetCount()) if self.listbox_Desinstalador.IsChecked(i)]
			if len(self.selectionUninstall) == 0:
				gui.messageBox(_("Necesita elegir al menos un complemento para continuar."), _("Error"), wx.ICON_ERROR)
				self.listbox_Desinstalador.SetFocus()
			else:
				self.IS_Active = True
				self.progreso.SetRange(len(self.selectionUninstall))
				self.lista.Disable()
				self.cerrarBTN.Disable()
				self.textEstado.Enable()
				self.textEstado.SetFocus()
				utilidades.DesinstalaComplementos(self, self.selectionUninstall)
		elif id == 108: # Seleccion boton habilitar desabilitar
			self.menu = wx.Menu()
			if len(self.listaComplementosdeshabilitados) == 0:
				item1 = self.menu.Append(7, _("&Seleccionar todo"))
				item2 = self.menu.Append(8, _("&Deseleccionar todo"))
			else:
				self.menuHabilitados = wx.Menu()
				item1 = self.menuHabilitados.Append(7, _("&Seleccionar todo"))
				item2 = self.menuHabilitados.Append(8, _("&Deseleccionar todo"))
				self.menu.AppendSubMenu(self.menuHabilitados, _("Complementos &habilitados"))
				self.menudeshabilitados = wx.Menu()
				item3 = self.menudeshabilitados.Append(9, _("&Seleccionar todo"))
				item4 = self.menudeshabilitados.Append(10, _("&Deseleccionar todo"))
				self.menu.AppendSubMenu(self.menudeshabilitados, _("Complementos &deshabilitados"))
			self.menu.Bind(wx.EVT_MENU, self.onSeleccion)
			self.seleccionHabiDesabiBTN.PopupMenu(self.menu)
		elif id == 109: # habilitar / deshabilitar boton procesar
			self.selectionHabilitados = [i for i in range(self.listbox_habilitados.GetCount()) if self.listbox_habilitados.IsChecked(i)]
			self.selectionDeshabilitados = [i for i in range(self.listbox_deshabilitados.GetCount()) if self.listbox_deshabilitados.IsChecked(i)]

			if len(self.selectionHabilitados) == 0 and len(self.selectionDeshabilitados) == 0:
				gui.messageBox(_("Necesita elegir al menos un complemento para continuar."), _("Error"), wx.ICON_ERROR)
				self.listbox_habilitados.SetFocus()
			else:
				self.IS_Active = True
				self.progreso.SetRange(len(self.selectionHabilitados)+len(self.selectionDeshabilitados))
				self.lista.Disable()
				self.cerrarBTN.Disable()
				self.textEstado.Enable()
				self.textEstado.SetFocus()
				utilidades.HabilitarDeshabilitar(self, self.selectionHabilitados, self.selectionDeshabilitados)
		elif id == 110: # botón selección manifiestos
			self.menu = wx.Menu()
			item1 = self.menu.Append(11, _("&Seleccionar todo"))
			item2 = self.menu.Append(12, _("&Deseleccionar todo"))
			self.menu.Bind(wx.EVT_MENU, self.onSeleccion)
			self.seleccionManifiestosBTN.PopupMenu(self.menu)
		elif id == 111: # boton procesar manifiestos
			self.menu = wx.Menu()
			item1 = self.menu.Append(13, _("Procesar &instalados"))
			item2 = self.menu.Append(14, _("Procesar un archivo de &complemento"))
			self.menu.Bind(wx.EVT_MENU, self.onSeleccion)
			self.procesoManifiestoBTN.PopupMenu(self.menu)
		elif id == 112: # boton ver documentación
			wx.LaunchDefaultBrowser('file://' + self.dirDocumentacion[self.listbox_documentacion.GetSelection()], flags=0)

		elif id== 197: # Botón aceptar general.
			if self.reinicio:
				core.restart()
			else:
				self.onEstado()
				self.lista.Enable()
				self.lista.SetFocus()
				if self.listaTemporalInstalador == None:
					return
				elif self.listaTemporalInstalador[-1] == "instalador":
					self.listbox_Instalador.Enable()
					self.seleccionInstaladorBTN.Enable()
					self.instalaBTN.Enable()
					self.listbox_Instalador.Clear()
					for i in range(0, len(self.listaTemporalInstalador[1])):
						self.listbox_Instalador.Append("{} {}".format(self.listaTemporalInstalador[1][i], self.listaTemporalInstalador[2][i]))
					self.listbox_Instalador.SetSelection(0)
					self.listbox_Instalador.SetFocus()
		elif id == 198: # Botón cancelar general.
			if self.reinicio:
				pass
			else:
				self.onEstado()
				self.lista.Enable()
				self.lista.SetFocus()
				if self.listaTemporalInstalador == None:
					return
				elif self.listaTemporalInstalador[-1] == "instalador":
					self.directorioInstaladorBTN.SetFocus()
		elif id == 199: # Botón cerrar general.
			self.onSalir(None)

	def onSeleccion(self, event):
		id = event.GetId()
		if id == 1: # Empaquetador seleccionar todo.
			num = self.listbox_empaquetador.GetCount()
			for i in range(num):
				self.listbox_empaquetador.Check(	i, True)
			self.listbox_empaquetador.SetSelection(0)
			self.listbox_empaquetador.SetFocus()
		elif id == 2: # Empaquetador deseleccionar todo.
			self.listbox_empaquetador.Clear()
			for i in self.listAddons:
				self.listbox_empaquetador.Append(i.manifest["summary"])
			self.listbox_empaquetador.SetSelection(0)
			self.listbox_empaquetador.SetFocus()
		elif id == 3: # Instalador seleccionar todo.
			num = self.listbox_Instalador.GetCount()
			for i in range(num):
				self.listbox_Instalador.Check(	i, True)
			self.listbox_Instalador.SetSelection(0)
			self.listbox_Instalador.SetFocus()
		elif id == 4: # Instalador deseleccionar todo.
			self.listbox_Instalador.Clear()
			for i in range(0, len(self.listaTemporalInstalador[1])):
				self.listbox_Instalador.Append("{} {}".format(self.listaTemporalInstalador[1][i], self.listaTemporalInstalador[2][i]))
			self.listbox_Instalador.SetSelection(0)
			self.listbox_Instalador.SetFocus()
		elif id == 5: # Desinstalador seleccionar todo.
			num = self.listbox_Desinstalador.GetCount()
			for i in range(num):
				self.listbox_Desinstalador.Check(	i, True)
			self.listbox_Desinstalador.SetSelection(0)
			self.listbox_Desinstalador.SetFocus()
		elif id == 6: # Desinstalador deseleccionar todo.
			self.listbox_Desinstalador.Clear()
			for i in self.listAddons:
				self.listbox_Desinstalador.Append(i.manifest["summary"])
			self.listbox_Desinstalador.SetSelection(0)
			self.listbox_Desinstalador.SetFocus()
		elif id == 7: # Habilitar seleccionar todo.
			num = self.listbox_habilitados.GetCount()
			for i in range(num):
				self.listbox_habilitados.Check(	i, True)
			self.listbox_habilitados.SetSelection(0)
			self.listbox_habilitados.SetFocus()
		elif id == 8: # Habilitar deseleccionar todo.
			self.listbox_habilitados.Clear()
			for i in self.listaComplementosHabilitados:
				self.listbox_habilitados.Append(self.listAddons[i].manifest["summary"])
			self.listbox_habilitados.SetSelection(0)
			self.listbox_habilitados.SetFocus()
		elif id == 9: # deshabilitados seleccionar todo.
			num = self.listbox_deshabilitados.GetCount()
			for i in range(num):
				self.listbox_deshabilitados.Check(	i, True)
			self.listbox_deshabilitados.SetSelection(0)
			self.listbox_deshabilitados.SetFocus()
		elif id == 10: # deshabilitados deseleccionar todo.
			self.listbox_deshabilitados.Clear()
			for i in self.listaComplementosdeshabilitados:
				self.listbox_deshabilitados.Append(self.listAddons[i].manifest["summary"])
			self.listbox_deshabilitados.SetSelection(0)
			self.listbox_deshabilitados.SetFocus()
		elif id == 11: # Manifiestos seleccionar todo.
			num = self.listbox_manifiestos.GetCount()
			for i in range(num):
				self.listbox_manifiestos.Check(	i, True)
			self.listbox_manifiestos.SetSelection(0)
			self.listbox_manifiestos.SetFocus()
		elif id == 12: # Manifiestos deseleccionar todo.
			self.listbox_manifiestos.Clear()
			for i in self.listAddons:
				ver = i.manifest["lastTestedNVDAVersion"]
				verFin = ".".join(str(e) for e in ver)
				self.listbox_manifiestos.Append("{} - {}".format(i.manifest["summary"], verFin))
			self.listbox_manifiestos.SetSelection(0)
			self.listbox_manifiestos.SetFocus()
		elif id == 13: # Manifiestos procesar instalados.
			self.selectionManifiestos = [i for i in range(self.listbox_manifiestos.GetCount()) if self.listbox_manifiestos.IsChecked(i)]
			if len(self.selectionManifiestos) == 0:
				gui.messageBox(_("Necesita elegir al menos un complemento para continuar."), _("Error"), wx.ICON_ERROR)
				self.listbox_manifiestos.SetFocus()
			else:
				self.IS_Active = True
				self.progreso.SetRange(len(self.selectionManifiestos))
				self.lista.Disable()
				self.cerrarBTN.Disable()
				self.textEstado.Enable()
				self.textEstado.SetFocus()
				mayor = ajustes.diccionarioMayor.get(self.choiceMayor.GetSelection())
				menor = ajustes.diccionarioMenor.get(self.choiceMenor.GetSelection())
				revision = self.choiceRevision.GetSelection()
				utilidades.ManifiestosInstalados(self, self.selectionManifiestos, mayor, menor, revision)
		elif id == 14:  # Manifiestos procesar fichero.
			wildcard = _("Complemento de NVDA (*.nvda-addon)|*.nvda-addon")
			dlg = wx.FileDialog(None, message=_("Seleccione un complemento de NVDAd"), defaultDir=os.getcwd(), defaultFile="", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW)
			if dlg.ShowModal() == wx.ID_OK:
				fichero = dlg.GetPath()
				dlg.Destroy()
				self.IS_Active = True
				self.progreso.SetRange(100)
				self.lista.Disable()
				self.cerrarBTN.Disable()
				self.textEstado.Enable()
				self.textEstado.SetFocus()
				mayor = ajustes.diccionarioMayor.get(self.choiceMayor.GetSelection())
				menor = ajustes.diccionarioMenor.get(self.choiceMenor.GetSelection())
				revision = self.choiceRevision.GetSelection()
				utilidades.ManifiestosArchivo(self, fichero, mayor, menor, revision)
			else:
				dlg.Destroy()

	def onkeyVentanaDialogo(self, event):
		if event.GetKeyCode() == 27: # Pulsamos ESC y cerramos la ventana
			self.onSalir(None)
		else:
			event.Skip()

	def onSalir(self, event):
		if self.IS_Active:
			return
		else:
			if self.reinicio:
				ajustes.reinicio = True
			ajustes.IS_WinON = False
			self.Destroy()
			gui.mainFrame.postPopup()
