# -*- coding: utf-8 -*-
# Copyright (C) 2020 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.
#
# Thanks to the translators:
#
# English: slanovani
# French: Rémy Ruiz
# Portuguese: Ângelo Miguel Abrantes
# Arabic: Wafiq Taher
# simplified Chinese: cary-rowen
# Spanish: Héctor J. Benítez Corredera
# import the necessary modules.
import globalPluginHandler
import addonHandler
import gui
import globalVars
from gui.nvdaControls import CustomCheckListBox
from scriptHandler import script
import wx
import os
import pickle
from threading import Thread
import zipfile

# For translation
addonHandler.initTranslation()

# List containing all the add-ons
listAddons = list(addonHandler.getAvailableAddons())

# Flag to know if a window is open
IS_WIN_on = False

# Creation of a GlobalPlugin class, derived from globalPluginHandler.GlobalPlugin.
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Creating the constructor of the newly created GlobalPlugin class.
	def __init__(self):
		# Call of the constructor of the parent class.
		super(GlobalPlugin, self).__init__()
		self._MainWindows = None

		if globalVars.appArgs.secure: return

		# Creation of our menu.
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		# Translators: Name of the item in the tools menu
		self.menuItem = self.toolsMenu.Append(wx.ID_ANY, _("&Add-on packer"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_generaAddon, self.menuItem)

	def terminate(self):
		try:
			if not self._MainWindows:
				self._MainWindows.Destroy()
		except (AttributeError, RuntimeError):
			pass

	@script(gesture=None,
		# TRANSLATORS: note for translators on the description
		description= _("Show the plug-in packer window"),
		# TRANSLATORS: note for translators on the category
		category= _("Add-on packer"))
	def script_generaAddon(self, event):
# Calling the main window of the plug-in

		if IS_WIN_on == False:
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
			if not os.path.exists(self.directorySave): self.directorySave = ""
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

		WIDTH = 800
		HEIGHT = 600
		pos = self._calculatePosition(WIDTH, HEIGHT)

		# Translators: Title of the plug-in in the main dialogue
		super(MainWindows, self).__init__(parent, -1, title=_("Add-on packer"), pos = pos, size = (WIDTH, HEIGHT))

		self.directorySave = ""
		self.ConfigFile()

		Panel = wx.Panel(self)

		# Translators: Label that identifies the list of add-ons
		label1 = wx.StaticText(Panel, wx.ID_ANY, label=_("&List of Add-ons:"))
		self.myListBox = CustomCheckListBox(Panel, 2)

		for i in listAddons:
			self.myListBox.Append(i.manifest["summary"])
		self.myListBox.SetSelection(0)
		self.myListBox.SetFocus()
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
			self.myListBox.Check(	i, True)
		self.myListBox.SetSelection(0)
		self.myListBox.SetFocus()

	def onUnselectionAllBTN(self, event):
		self.myListBox.Clear()
		for i in listAddons:
			self.myListBox.Append(i.manifest["summary"])
		self.myListBox.SetSelection(0)
		self.myListBox.SetFocus()

	def onDirectory(self, event):
		# Translators: Title of the dialog box to select directory
		dlg = wx.DirDialog(self, _("Select a directory:"),
			style=wx.DD_DEFAULT_STYLE
			)
		if dlg.ShowModal() == wx.ID_OK:
			self.textDirectory.SetValue(dlg.GetPath())
			self.directorySave =dlg.GetPath()
			self.ConfigFileSave()
		dlg.Destroy()

	def onGenerate(self, event):
		selection = [i for i in range(self.myListBox.GetCount()) if self.myListBox.IsChecked(i)]
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
				threadHome =ThreadLaunch(selection, self.directorySave)
				threadHome.start()
				self.onClose(None)

	def onClose(self, event):
		self.ConfigFileSave()
		self.Destroy()
		gui.mainFrame.postPopup()

class ThreadLaunch(Thread):
	def __init__(self, selection, directorySave):
		super(ThreadLaunch, self).__init__()

		self.selection = selection
		self.directorySave = directorySave

		self.daemon = True

	def run(self):
		def LaunchDialog(selection, directorySave):
			self._MainWindows = ProgressThread(gui.mainFrame, selection, directorySave)
			gui.mainFrame.prePopup()
			self._MainWindows.Show()

		wx.CallAfter(LaunchDialog, self.selection, self.directorySave)

class GeneratingThread(Thread):
	def __init__(self, frame, value, dir):

		super(GeneratingThread, self).__init__()

		self.frame = frame
		self.value = value
		self.directorySave = dir
		self.daemon = True
		self.start()

	# Function to compress plug-in folders and remove all __pycache__ folders
	def zipfolder(self, foldername, target_dir):            
		zipobj = zipfile.ZipFile(foldername + '.nvda-addon', 'w', zipfile.ZIP_DEFLATED)
		rootlen = len(target_dir) + 1
		for base, dirs, files in os.walk(target_dir):
			if '__pycache__' in dirs:
				dirs.remove('__pycache__')
			for file in files:
				fn = os.path.join(base, file)
				zipobj.write(fn, fn[rootlen:])
		zipobj.close()

	def run(self):
		try:
			for i in self.value:
				addonSave = os.path.join(self.directorySave, listAddons[i].manifest["name"] + "_" + listAddons[i].manifest["version"].replace(":", "_") + "_Gen")
				self.zipfolder(addonSave, listAddons[i].path)
				wx.CallAfter(self.frame.next, i)
			# Translators: Message informing that the add-ons were generated correctly
			wx.CallAfter(self.frame.done, _("All add-ons were correctly generated."))
		except:
			# Translators: Message informing that add-on generation failed
			wx.CallAfter(self.frame.error, _("The add-ons could not be generated."))

class ProgressThread(wx.Dialog):

	def __init__(self, frame, value, dir):

		# Translators: Title of the progress dialog
		super(ProgressThread, self).__init__(None, -1, title=_("Generating add-ons"))

		self.Centre()

		global IS_WIN_on
		IS_WIN_on = True

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

		GeneratingThread(self, value, dir)

	def next(self, event):
		self.progressBar.SetValue(event)

	def done(self, event):
		global IS_WIN_on
		IS_WIN_on = False
		gui.messageBox(event,
			# Translators: Title of the dialog box, completed correctly. Information
			_("Information"), wx.ICON_INFORMATION)
		self.Destroy()
		gui.mainFrame.postPopup()

	def error(self, event):
		global IS_WIN_on
		IS_WIN_on = False
		gui.messageBox(event,
			# Translators: Title of the dialog box, could not be completed. Error
			_("Error"), wx.ICON_ERROR)
		self.Destroy()
		gui.mainFrame.postPopup()

	def onNull(self, event):
		pass