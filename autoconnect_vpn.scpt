-- Please set your vpn connection name and password here
set VPNName to "your VPN name"
set VPNpassword to "your VPN password"

tell application "System Events"
	tell current location of network preferences
		set VPNService to service VPNName
	end tell

	set isConnected to connected of current configuration of VPNService
	if isConnected then
		disconnect VPNService
	else
		connect VPNService

		set startTime to current date
		repeat until exists (static text 1 of window 1 of application process "UserNotificationCenter" whose name is "VPN Connection")
			if (current date) - startTime is greater than 8 then
				error "Could not connect, the connection dialog did not pop up"
				exit repeat
			end if
			delay 0.2
		end repeat

		set theProcess to application process "UserNotificationCenter"
		set theWindow to window 1 of theProcess
		set theDescription to static text 2 of theWindow

		if name of theDescription is "Enter Username and Password." then
			set theControls to get entire contents of theWindow
			set thePassword to text field 1 of theWindow whose description is "secure text field"
			set value of thePassword to VPNpassword
			set theOKButton to button 1 of theWindow whose title is "OK"
			click theOKButton

			repeat until exists (button 1 of window 1 of application process "UserNotificationCenter" whose title is "Disconnect")
				if exists (button 1 of window 1 of application process "UserNotificationCenter" whose title is "Cancel") then

					set theCancelButton to button 1 of theWindow whose title is "Cancel"
					click theCancelButton
					error "please check password in the script."
					exit repeat
				end if
				delay 0.2
			end repeat

			set theOKButton to button 1 of theWindow whose title is "OK"
			click theOKButton
		end if

	end if
end tell
