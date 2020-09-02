# -*- coding: utf-8 -*-
# Copyright (C) 2020 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules.
import globalPluginHandler
import addonHandler
import gui
import globalVars
import wx
import shutil
import os
import pickle
from threading import Thread
# Call to the bookstore including pubsub
from .pubsub import pub

# For translation
addonHandler.initTranslation()

# List containing all the add-ons
lista = list(addonHandler.getAvailableAddons())

# Creation of a GlobalPlugin class, derived from globalPluginHandler.GlobalPlugin.
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Creating the constructor of the newly created GlobalPlugin class.
	def __init__(self):
		# Call of the constructor of the parent class.
		super(GlobalPlugin, self).__init__()
		self._MainWindows = None

		if globalVars.appArgs.secure:
			return

		# Creation of our menu.
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		# Translators: Name of the item in the tools menu
		self.menuItem = self.toolsMenu.Append(wx.ID_ANY, _("&Add-on packer"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.generaAddon, self.menuItem)

	def terminate(self):
		try:
			if not self._MainWindows:
				self._MainWindows.Destroy()
		except (AttributeError, RuntimeError):
			pass

	def generaAddon(self, event):
# Calling the main window of the plug-in
		if not self._MainWindows:
			self._MainWindows = MainWindows(gui.mainFrame)

		if not self._MainWindows.IsShown():
			gui.mainFrame.prePopup()
			self._MainWindows.Show()

# Creating the Main Window of the Plug-in
class MainWindows(wx.Dialog):

# definition to check output directory
	def ConfigFile(self):
		fileConfig = os.path.join(globalVars.appArgs.configPath, "addonPackager.dat")
		if os.path.isfile(fileConfig):
			file = open(fileConfig, 'rb')
			self.directorySave = pickle.load(file)
			file.close()
			if os.path.exists(self.directorySave):
				pass
			else:
				self.directorySave = ""
		else:
			try:
				file = open(fileConfig, "wb")
				pickle.dump(self.directorySave, file)
				file.close()
			except:
				pass

# Save the output directory to a configuration file
	def ConfigFileSave(self):
		fileConfig = os.path.join(globalVars.appArgs.configPath, "addonPackager.dat")
		file = open(fileConfig, "wb")
		pickle.dump(self.directorySave, file)
		file.close()

# Function taken from the add-on emoticons to center the window
	def _calculatePosition(self, width, height):
		w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
		h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
		# Centre of the screen
		x = w / 2
		y = h / 2
		# Minus application offset
		x -= (width / 2)
		y -= (height / 2)
		return (x, y)

	def __init__(self, parent):
		self.directorySave=""
		WIDTH = 800
		HEIGHT = 600
		pos = self._calculatePosition(WIDTH, HEIGHT)

		# Translators: Title of the plug-in in the main dialogue
		super(MainWindows, self).__init__(parent, -1, title=_("Add-on packer"), pos = pos, size = (WIDTH, HEIGHT))

		self.ConfigFile()

		Panel = wx.Panel(self)

		# Translators: Label that identifies the list of add-ons
		label1 = wx.StaticText(Panel, wx.ID_ANY, label=_("&List of Add-on:"))
		self.myListBox = wx.ListBox(Panel, style =  wx.LB_HSCROLL | wx.LB_MULTIPLE | wx.LB_NEEDED_SB)
		for i in lista:
			self.myListBox.Append(i.manifest["summary"])
		self.Bind(wx.EVT_LISTBOX, self.OnSelection, self.myListBox)

		# Translators: Button name to select all add-ons
		self.selectionAllBTN = wx.Button(Panel, wx.ID_ANY, _("&Select all"))
		self.Bind(wx.EVT_BUTTON, self.onselectionAllBTN, self.selectionAllBTN)

		# Translators: Button name to deselect all add-ons
		self.unselectionAllBTN = wx.Button(Panel, wx.ID_ANY, _("Deselect &all"))
		self.Bind(wx.EVT_BUTTON, self.onUnselectionAllBTN, self.unselectionAllBTN)

		# Translators: Label that identifies the area to choose directory to save the add-ons
		label2 = wx.StaticText(Panel, wx.ID_ANY, label=_("Destination directory:"))
		self.textDirectory = wx.TextCtrl(Panel, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY)
		self.textDirectory.SetValue(self.directorySave)

		# Translators: Name of the button to choose directory
		self.directoryBTN = wx.Button(Panel, wx.ID_ANY, _("Select &directory"))
		self.Bind(wx.EVT_BUTTON, self.onDirectory, self.directoryBTN)

		# Translators: Name of the button to generate the add-ons
		self.generateAddon = wx.Button(Panel, wx.ID_ANY, _("&Generate add-ons"))
		self.Bind(wx.EVT_BUTTON, self.onGenerate, self.generateAddon)

		# Translators: Exit button name
		self.closeBTN = wx.Button(Panel, wx.ID_CANCEL, _("&Close"))
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)

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
		# Translators: Title of the dialog box to select directory
		dlg = wx.DirDialog(self, _("Select a directory:"),
			style=wx.DD_DEFAULT_STYLE
#			| wx.DD_DIR_MUST_EXIST
#			| wx.DD_CHANGE_DIR
			)
		if dlg.ShowModal() == wx.ID_OK:
			self.textDirectory.SetValue(dlg.GetPath())
			self.directorySave =dlg.GetPath()
			self.ConfigFileSave()
		dlg.Destroy()

	def onGenerate(self, event):
		selection = self.myListBox.GetSelections()
		if len(selection) == 0:
			# Translators: Error message warning that no add-on was selected
			gui.messageBox(_("You need to select at least one add-on to continue the action."),
				# Translators: Title of the dialog box no add-ons selected, Error
				_("Error"), wx.ICON_ERROR)
			self.myListBox.SetFocus()
		else:
			if self.textDirectory.GetValue() == "":
				# Translators: Error message to warn that no directory was selected
				gui.messageBox(_("You need to select an output directory to continue the action."),
					# Translators: Title of the dialog box no directory, Error
					_("Error"), wx.ICON_ERROR)
				self.directoryBTN.SetFocus()
			else:
				dlg = ProgressThread(selection, self.directorySave)
				dlg.ShowModal()
				self.onClose(None)

	def onClose(self, event):
		self.ConfigFileSave()
		self.Destroy()
		gui.mainFrame.postPopup()

class GeneratingThread(Thread):
	def __init__(self, value, dir):

		super(GeneratingThread, self).__init__()
		self.value = value
		self.directorySave = dir
		self.daemon = True
		self.start()

	def run(self):
		try:
			for i in self.value:
				addonSave = os.path.join(self.directorySave, lista[i].manifest["name"] + "_" + lista[i].manifest["version"].replace(":", "_") + "_Gen")
				shutil.make_archive(addonSave, "zip", lista[i].path, base_dir=None)
				shutil.move(addonSave + ".zip", addonSave + ".nvda-addon")
				wx.CallAfter(pub.sendMessage, "nextProgress", msg=i)
			# Translators: Message informing that the add-ons were generated correctly
			wx.CallAfter(pub.sendMessage, "correctoCHK_BK", msg=_("All add-ons were correctly generated."))
		except:
			# Translators: Message informing that add-on generation failed
			wx.CallAfter(pub.sendMessage, "errorCHK_BK", msg=_("The add-ons could not be generated."))

class ProgressThread(wx.Dialog):

	def __init__(self, value, dir):

		# Translators: Title of the progress dialog
		super(ProgressThread, self).__init__(None, -1, title=_("Generating add-ons"))

		self.Centre()

		panel=wx.Panel(self)

		self.Bind(wx.EVT_CLOSE, self.onNull)

		# Translators: Tag that asks the user to wait
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

		GeneratingThread(value, dir)

	def next(self, msg):
		self.progressBar.SetValue(msg)

	def done(self, msg):
		self.Close()
		gui.messageBox(msg,
			# Translators: Title of the dialog box, completed correctly. Information
			_("Information"), wx.ICON_INFORMATION)
		self.Destroy()

	def error(self, msg):
		self.Close()
		gui.messageBox(msg,
			# Translators: Title of the dialog box, could not be completed. Error
			_("Error"), wx.ICON_ERROR)
		self.Destroy()

	def onNull(self, event):
		pass