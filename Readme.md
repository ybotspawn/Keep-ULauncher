## About

This is a Google Keep launcher extension for the ULauncher desktop assistant platform.  This project is currently a work in progress.  

## Pre Installation

Prior to installation, you should install the gkeepapi, by Kiwiz. Kudos to this author for their hard work on the gkeepapi project (https://github.com/kiwiz/gkeepapi).  This can be installed via your Linux flavor package manager or Python Pip. 

## Installation

This software can be installed into ULauncher by opening the ULauncher preferences and installing this plugin via the extension tab:

![extension view](https://raw.githubusercontent.com/ybotspawn/Keep-ULauncher/master/images/extension-view.png)

Next, click "Add Extension" in the lower left and enter the "https://github.com/ybotspawn/Keep-ULauncher" into the URL prompt:

![extension url view](https://raw.githubusercontent.com/ybotspawn/Keep-ULauncher/master/images/extension-url-view.png)

## Post Installation

Once installed the software will likely require some further configuration to be used.  The default keyword is gk, this and the remaining options can be changed in the extension configuration menu.  Changing the keyword is optional.  The next option, that is required is the Google user name.  This is your google account email, including the @domain if you are a Google Apps for Work user.  

![config view](https://raw.githubusercontent.com/ybotspawn/Keep-ULauncher/master/images/menu-view.png)

The second option is the Google API Key.  This can be your password, but your password will likely not work, especially if you have two factor authentication enabled.  To overcome this issue, you should follow the instructions here: https://support.google.com/accounts/answer/185833 and provide your API Key.  This key should be held locally and protected.

## Usage

Usage is simple, simply open ULauncher and type gk followed by your Google Note information.  A basic BNF style syntax document is available here:

![Keep Language](https://raw.githubusercontent.com/ybotspawn/Keep-ULauncher/master/keeplanguage.txt)

If you're unsure the basic syntax is as follows:

TRUE - Denotes that the note should be pinned <br />
COLOR - Indicates the color the note should be, the defualt is White.  The available options are BLUE, RED, GREEN, BROWN, DARKBLUE, GRAY, ORANGE, PINK, PURPLE, TEAL, YELLOW. <br />
TEXT - Indicates the following text will be placed into the body of your note <br />
TITLE - Indicates the following text will be placed as the title of your note <br />

Example:

![config view](https://raw.githubusercontent.com/ybotspawn/Keep-ULauncher/master/images/create-view.png)