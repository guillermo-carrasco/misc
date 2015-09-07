_NOTE:_ Script taken from [here](https://gist.github.com/twksos/44b45abf5263635776ec).
I just modified the necessary bits to make it work with OS X Yosemite and add this
explanation

<hr />

This small script allows for the automatic connection to a VPN in MacOS X.

In order to make it work, you need to create an application using the script and
give it access to the clipboard, to do so:

1. Open AppleScript Editor
2. Paste the code of `autoconnect_vpn.scpt` and change the VPN credentials
3. Save the script **using "Application" as format** using the name you prefer
4. Open Security & Privacy menu, go to the privacy tab and unlock it by clicking the
bottom left small lock. Finally drag and drop the newly created app to the list of
"Allow the apps below to control your computer"

You're done, now, by typing `CMD + space + <name_you_gave_to_the_application>` you
should automatically connect to the VPN.
