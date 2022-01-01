# Add-on Packager

This add-on was created so that everyone can create backups of installed add-ons.

NVDA has a wide variety of add-ons, that can be installed from the [NVDA Community Add-ons website](https://addons.nvda-project.org)

At the same time, there are a number of unofficial add-ons created by users around the world, the sources of which can be difficult to find after reinstalling the operating system or NVDA itself.

The idea came about when a friend asked me for an unofficial add-on, and since I didn't have a packaged add-on, I had to package it.

It is generally very easy to package an add-on, but not everyone knows about it, so I thought it would be better if NVDA had such a feature.

This add-on packages selected user add-ons that are installed on a computer to be installed on another PC or simply to share.
## Using the add-on

The add-on is divided into four areas:

* The first one contains a list of all the add-ons we have installed, whether they are enabled or disabled. In this list, we can select all the add-ons we need.
* The second contains a row of buttons for quickly selecting all add-ons or quickly deselecting all the selections we made.
* The third area is a read-only text box, which is empty by default, and there is a button to select a directory.
* The fourth is a row of buttons with a button for creating already selected add-ons and another one for exiting the add-on.

I've made the textbox read-only to make it easier to check the output directory at any given time. I decided not to use it as a normal edit box to avoid accidental clicking and it might affect the directory.

Also, the first time you select a folder, the selected folder will be saved for quick creation until the folder is removed from drive. In this case, the folder must be selected again.

### Add-on hotkeys

* Alt + L: Go to the list of add-ons.
* Alt + S: Select all add-ons, whether the add-on has already been checked out or not.
* Alt + D: Deselect all checked add-ons.
* Alt + B: Opens a window for selecting a folder.
* Alt + G: Generates selected add-ons.
* Alt + C or Alt + F4: Closes the add-on.

The add-on will inform us at any time if there are any errors in use. It will warn if we generate an add-on without selecting it, or by selecting an add-on and leaving the folder field blank. The add-on will inform us about the successful generation of add-ons,as well as any errors that occurred during the generation.

There is also a progress bar while generating add-ons to give a percentage.

## A small note about minor changes to the generated add-on file

Previously, when creating an add-on, the add-on would automatically add a "gen" tag to the name of the generated add-on file at the end, which indicated that the add-on was not original, but in this release this tag was removed, as such a tag is not required, because the generated add-ons are similar to the original packaged add-ons, so the generated add-ons will now be without the "gen" tag.

## Privacy Notice

It should be noted that the final generated file is a standard NVDA add-on file, so it is strictly forbidden to put sensitive information in the add-on folder that will be generated, because this add-on adds or removes nothing, it just generates the installed add-ons.

This is never the case with official add-ons, but as mentioned, there are hundreds of unofficial add-ons out there, so we advise you not to put sensitive information in the add-on folder.

the author of the add-on "AddonPacker" is exempt from liability.

