""" Visual art and writing don't exist on an aesthetic hierarchy
    that positions one above the other, because each is capable of
    things the other can't do at all. Sometimes one picture is equal
    to 30 pages of discourse, just as there are things images are
    completely incapable of communicating."""

from subprocess import call, check_output

#class ShellAesthetic:

#    def __init__(data):

#        self.profile = data["profile_name"]
#        self.transparency = data["transparency"]

# check if aesthetic profile exists and list it
def find_theme():
	call("dconf", "list",
		 )
