# -*- coding: utf-8 -*-
# Copyright (C) 2020 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import globalPluginHandler
import addonHandler
import gui
import config
import wx
import shutil
import os
import pickle
from threading import Thread
# Call to the bookstore including pubsub
from .pubsub import pub

# For translation
addonHandler.initTranslation()

# Creation of a GlobalPlugin class, derived from globalPluginHandler.GlobalPlugin.
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Creating the constructor of the newly created GlobalPlugin class.
	def __init__(self, *args, **kwargs):
		# Call of the constructor of the parent class.
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		# Creation of our menu.
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.menuItem = self.toolsMenu.Append(wx.ID_ANY, _("&Add-on packer"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.generaAddon, self.menuItem)

	def generaAddon(self, event):
# Calling the main window of the plug-in
		dlg = MainWindows()
		dlg.ShowModal()

# List containing all the add-ons
lista = list(addonHandler.getAvailableAddons())
# Output directory containment
directorySave = ""

# definition to check output directory
def ConfigFile():
	global directorySave
	fileConfig = config.getUserDefaultConfigPath() + "/addonPackager.dat"
	if os.path.isfile(fileConfig):
		file = open(	fileConfig, 'rb')
		directorySave = pickle.load(file)
		file.close()
		if os.path.exists(directorySave):
			pass
		else:
			directorySave = ""
	else:
		file = open(fileConfig, "wb")
		pickle.dump(directorySave, file)
		file.close()

# Save the output directory to a configuration file
def ConfigFileSave():
	fileConfig = config.getUserDefaultConfigPath() + "/addonPackager.dat"
	file = open(fileConfig, "wb")
	pickle.dump(directorySave, file)
	file.close()

# Creating the Main Window of the Plug-in
class MainWindows(wx.Dialog):
	def __init__(self):

		ConfigFile()
		super(MainWindows, self).__init__(None, -1, title=_("Add-on packer"), style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX |wx.CLIP_CHILDREN)
#		wx.Frame.__init__(self, None, -1, title=_("Add-on packer"), style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX |wx.CLIP_CHILDREN)

		self.SetSize((800, 600))

		self.Centre()
		Panel = wx.Panel(self)

		label1 = wx.StaticText(Panel, wx.ID_ANY, label=_("&List of Add-on:"))
		self.myListBox = wx.ListBox(Panel, style =  wx.LB_HSCROLL | wx.LB_MULTIPLE | wx.LB_NEEDED_SB)
		for i in lista:
			self.myListBox.Append(i.manifest["summary"])
		self.Bind(wx.EVT_LISTBOX, self.OnSelection, self.myListBox)

		self.selectionAllBTN = wx.Button(Panel, wx.ID_ANY, _("&Select all"))
		self.Bind(wx.EVT_BUTTON, self.onselectionAllBTN, self.selectionAllBTN)

		self.unselectionAllBTN = wx.Button(Panel, wx.ID_ANY, _("Deselect &all"))
		self.Bind(wx.EVT_BUTTON, self.onUnselectionAllBTN, self.unselectionAllBTN)

		label2 = wx.StaticText(Panel, wx.ID_ANY, label=_("Destination directory:"))
		self.textDirectory = wx.TextCtrl(Panel, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY)
		self.textDirectory.SetValue(directorySave)
		self.directoryBTN = wx.Button(Panel, wx.ID_ANY, _("Select &directory"))
		self.Bind(wx.EVT_BUTTON, self.onDirectory, self.directoryBTN)

		self.generateAddon = wx.Button(Panel, wx.ID_ANY, _("&Generate add-ons"))
		self.Bind(wx.EVT_BUTTON, self.onGenerate, self.generateAddon)

		self.closeBTN = wx.Button(Panel, wx.ID_CANCEL, _("&Close"))
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)

		self.Bind(wx.EVT_BUTTON, self.onClose, id = wx.ID_CANCEL)

		sizeV = wx.BoxSizer(wx.VERTICAL)
		sizeH1 = wx.BoxSizer(wx.HORIZONTAL)
		sizeH2 = wx.BoxSizer(wx.HORIZONTAL)
		sizeH3 = wx.BoxSizer(wx.HORIZONTAL)

		sizeV.Add(label1, 0, wx.EXPAND)
		sizeV.Add(self.myListBox, 1, wx.EXPAND|wx.ALL, 5)

		sizeH1.Add(self.selectionAllBTN, 2, wx.CENTER)
		sizeH1.Add(self.unselectionAllBTN, 2, wx.CENTER)

		sizeV.Add(sizeH1, 0, wx.CENTER)

		sizeV.Add(label2, 0, wx.EXPAND)
		sizeH2.Add(self.textDirectory, 1, wx.EXPAND)
		sizeH2.Add(self.directoryBTN, 0)

		sizeV.Add(sizeH2, 0, wx.EXPAND)

		sizeH3.Add(self.generateAddon, 2, wx.CENTER)
		sizeH3.Add(self.closeBTN, 2, wx.CENTER)

		sizeV.Add(sizeH3, 0, wx.CENTER)

		Panel.SetSizer(sizeV)

	def OnSelection(self, event):
		pass

	def onselectionAllBTN(self, event):
		num = self.myListBox.GetCount()
		for i in range(num):
			self.myListBox.SetSelection(i)

	def onUnselectionAllBTN(self, event):
		self.myListBox.Clear()
		for i in lista:
			self.myListBox.Append(i.manifest["summary"])
		self.myListBox.SetFocus()

	def onDirectory(self, event):
		dlg = wx.DirDialog(self, _("Select a directory:"),
			style=wx.DD_DEFAULT_STYLE
#			| wx.DD_DIR_MUST_EXIST
#			| wx.DD_CHANGE_DIR
			)
		if dlg.ShowModal() == wx.ID_OK:
			self.textDirectory.SetValue(dlg.GetPath())
			global directorySave
			directorySave =dlg.GetPath()
			ConfigFileSave()
			dlg.Destroy()
		else:
			dlg.Destroy()

	def onGenerate(self, event):
		selection = self.myListBox.GetSelections()
		if len(selection) == 0:
			gui.messageBox(_("You need to select at least one add-on to continue the action."), _("Error"), wx.ICON_ERROR)
			self.myListBox.SetFocus()
		else:
			if self.textDirectory.GetValue() == "":
				gui.messageBox(_("You need to select an output directory to continue the action."), _("Error"), wx.ICON_ERROR)
				self.directoryBTN.SetFocus()
			else:
				self.Close()
				dlg = ProgressThread(selection)
				dlg.ShowModal()

	def onClose(self, event):
#		if event.GetEventType() == 10012: # EVT_BUTTON
			ConfigFileSave()
			self.DestroyChildren()
			self.Destroy()
#			self.SetReturnCode(wx.ID_CANCEL)

#			event.Skip()

class GeneratingThread(Thread):
	def __init__(self, value):

		Thread.__init__(self)
		self.value = value
		self.daemon = True
		self.start()

	def run(self):
		try:
			for i in self.value:
				addonSave = directorySave + "/" + lista[i].manifest["name"] + "_" + lista[i].manifest["version"].replace(":", "_") + "_Gen"
				shutil.make_archive(addonSave, "zip", lista[i].path, base_dir=None)
				shutil.move(addonSave + ".zip", addonSave + ".nvda-addon")
				wx.CallAfter(pub.sendMessage, "nextProgress", msg=i)
			wx.CallAfter(pub.sendMessage, "correctoCHK_BK", msg=_("All add-ons were correctly generated."))
		except:
			wx.CallAfter(pub.sendMessage, "errorCHK_BK", msg=_("The add-ons could not be generated."))

class ProgressThread(wx.Dialog):
	def __init__(self, value):
		wx.Dialog.__init__(self, None, title=_("Generating add-ons"), style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX |wx.CLIP_CHILDREN)

		self.Centre()

		panel=wx.Panel(self)

		self.Bind(wx.EVT_CLOSE, self.onNull)

		label = wx.StaticText(panel, wx.ID_ANY, label=_("Please wait..."))
		self.progressBar=wx.Gauge(panel, wx.ID_ANY, range=len(value), style = wx.GA_HORIZONTAL)
		label.SetFocus()

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(label, 0, wx.EXPAND)
		sizer.Add(self.progressBar, 0, wx.EXPAND)
		panel.SetSizer(sizer)

		pub.subscribe(self.next, "nextProgress")
		pub.subscribe(self.done, "correctoCHK_BK")
		pub.subscribe(self.error, "errorCHK_BK")

		GeneratingThread(value)

	def next(self, msg):
		self.progressBar.SetValue(msg)

	def done(self, msg):
		self.Close()
		gui.messageBox(msg, _("Information"), wx.ICON_INFORMATION)
		self.Destroy()

	def error(self, msg):
		self.Close()
		gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
		self.Destroy()

	def onNull(self, event):
		pass