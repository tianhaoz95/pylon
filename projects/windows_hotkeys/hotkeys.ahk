; Change the stuff here to your information
GitHub_Username := "tianhaoz95"

; Calculate global variables
GitHub_Endpoint := "https://github.com/"
GitHub_Profile_URL := GitHub_Endpoint . GitHub_Username
SET_TIMER_URL := "https://www.google.com/search?q=set+a+timer+for+30+minutes"

; For media control:
;   Ctrl + Numpad 4 = Play Previous
;   Ctrl + Numpad 5 = Pause / Resume
;   Ctrl + Numpad 6 = Play Next
^Numpad5::Send {Media_Play_Pause}
^Numpad4::Send {Media_Prev}
^Numpad6::Send {Media_Next}

; GitHub related hotkeys:
;   Ctrl + Numpad 0 = Open GitHub Profile
^Numpad0::Run %GitHub_Profile_URL%

; For productivity
;   Ctrl + Numpad 3 = Set a 30 minutes timer for focus work
;   Ctrl + Numpad Dot = Close the current application (same as Alt + F4)
^Numpad3::Run %SET_TIMER_URL%
^NumpadDot::Send !{F4}
