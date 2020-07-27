# Addon Packager

This add-on comes up  from the need to have a backup of the installed add-ons.

NVDA has an ample collection of official add-ons, easy to obtain from the official repositories or from the authors' different github accounts.

But at the same time it also has a number of unofficial add-ons whose source  is sometimes difficult to determine.

The idea came up when a friend asked me for an unofficial add-on, and since the add-on wasn't within my reach I had to package it for him.

Well, the process of packaging an add-on is easy, but not known by everyone, so I thought it would be great if NVDA had such feature.

So that's what this add-on does: it automatically packages those add-ons that the user wants to have so they can be installed in another copy of NVDA, in a clean installation of NVDA or just to share it.
## Using the add-on

The add-on is divided into four areas:

* The first one, which  contains a list of all our installed add-ons whether they are enabled or disabled. In this list we can select all the add-ons we want.
* The second one contains a row of buttons to quickly select all the add-ons or to quickly delete all the selections that we had made.
* The third one a reading text box that will contain the output directory and a button to select that output directory.

I've put the text box as read-only  in order to make it easy to check the output directory at any given time. I've decided not to put it as a normal edit field in order to avoid any  accidental press, and that the directory could thus be affected.

* The fourth one is a row of buttons with the button to generate the already packed add-ons and another one to exit the add-on.

### Ad-on hotkeys

* Alt + L: it will situate our focus on thead-on list.
* Alt + S: It will select all the add-ons for us regardless of whether there was any other already checked.
* Alt + A: It will uncheck all the add-ons we have checked.
* Alt + D: It will open a directory selection window to select the output directory.
* Alt + G: It will start the generation of the add-ons  we have selected in the output directory.
* Alt + C or Alt + F4: It will close the add-on.

## Other information of interest

* The add-on will alert us at all times with information dialogs about the course of usage.
* It will warn us if we try to generate an add-on without having one selected.
* It will warn us if we try to generate an add-on without having a defined output directory.
* It will alert us when the process is successful, as well as when an error occurs.
* The output directory will be saved so that it is specified  next time we use the add-on. This setting will be deleted if the output directory is deleted, and we will have to select another existing directory.
* When generating the add-ons, a progress bar will alert us about the percentage completed at all times.
* The resulting files have a tag in the name to identify that they have been generated and are not original. This tag is (gen).

# A very important notice

It's worth to mention that the resulting files are just the way we have them in our Addon directory, without adding or removing anything by this addon.

This means that all the information of the add-on we select is included.

It is not normal for an add-on developer to include sensitive information within the add-on directory itself.

in fact, this is considered a bad practice, so this will unlikely happen at least in official addons.

But since there are hundreds of unofficial add-ons of different kinds, you are warned that if an add-on includes sensitive information in its own directory, this sensitive information will be included in the generated file.


That's why we have to take this privacy and security aspect into account, in order to know if a generated add-on we are going to share brings any sensitive information that we don't want to share.

As I mentioned, this is almost improbable, but you are warned and by using this add-on you agree to know that you have been warned and that the author of this add-on is exempt  from  all liability.

Translated by slanovani.