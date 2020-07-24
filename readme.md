# Packer of complements

This add-on arises from the need to have a backup of the add-ons installed.

NVDA has a large collection of official add-ons, easy to obtain from the official repositories or from the different Github accounts of the authors.

But at the same time it also has a number of unofficial add-ons that are sometimes difficult to know where they came from.

The idea came up when a friend asked me for an unofficial add-on and because I didn't have the add-on handy I had to pack it.

Well the process of packaging an add-on is easy but not known by everyone so I thought it would be great if NVDA had it.

So that's what this add-on does, it automatically packages those add-ons that the user wants to have so they can be installed in another copy of NVDA, in a clean installation of NVDA or just to share it.
## Using the add-on

The complement is divided into four areas:

* The first area contains a list of all our installed add-ons whether they are enabled or disabled. In this list we can select all the add-ons we want.
* The second one is a row of buttons to quickly select all the add-ons or to quickly delete all the selections that we had made.
* The third one a reading text box that will contain the output directory and a button to select that output directory.

And put the read-only text box to make it easy to check the output directory at any given time. E decided not to put it in normal write mode to avoid some keystrokes by mistake and that the directory could be affected.

* The fourth one is a row of buttons with the button to generate the already packed plugins and another one to exit the plugin.

### Quick keys in the plug-in

* Alt + L: It will position us in the focus of the complement list.
* Alt + S: It will select all the add-ons regardless of whether there are any already marked.
* Alt + A: It will uncheck all the add-ons we have marked.
* Alt + D: It will open a directory selection window to select the output directory.
* Alt + G: It will start the generation of the add-ons that we had selected in the output directory.
* Alt + C or Alt + F4: It will close the plug-in.

## Other information of interest

* The plug-in will alert us at all times with information dialogues about the course of the drive.
* It will warn us if we try to generate a plug-in without having one selected.
* It will warn us if we try to generate a plug-in without having a defined output directory.
* It will warn us when the process is a success as well as when an error occurs.
* The output directory will be saved so that it is specified the next time we use the add-on, this setting will be deleted if the output directory is eliminated and we will have to select another existing directory.
* When generating the add-ons we will be warned by a progress bar that will indicate the percentage that has been done at all times.
* The resulting files have a tag in the name to identify that they have been generated and are not original. This tag is (gen).

# Very important note

Mention that the resulting files are as we have them in our Addon directory without adding or removing anything from this addon.

This means that all the information of the add-on we select is included.

It is not normal for an add-on developer to include sensitive information within the add-on directory itself.

In fact it is considered bad practice so it is unlikely that at least in official add-ons this will happen.

But because there are hundreds of unofficial add-ons of different kinds, you are warned that if an add-on includes sensitive information in its own directory, this sensitive information will be included in the generated file.


That's why we have to take into account this aspect of privacy and security to know if we are going to share a generated add-on if it has sensitive information that we don't want to share.

As I mentioned this is almost improbable, but you are warned and by using this add-on you agree to know that you have been warned and to release the author of this add-on from all liability.