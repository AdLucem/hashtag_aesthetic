import subprocess
import sys
import json

# global name variables
PROJECT_FILE = "./project_details.json"

# custom exceptions
class WrongCommand(Exception):
	pass

# functions

def readProjects(prType):
	"""To read in the details of projects belonging to
	a specific category- active, semiactive, academic or notes-
	from the project file"""

	with open(PROJECT_FILE, "r+") as f:
		data = json.load(f)

	projects = data[prType]
	return projects



def mkProjects(projects, command):

	"""For a list of projects with their details, either
	retrieve them from the storage place or update them,
	based on the command given"""

	try:
		if command not in ["retrieve", "update"]:
 			raise WrongCommand

	except WrongCommand:
		print("Command must be 'retrieve' or 'update' only.")

	else:
		for project in projects:
			cmds = project[command]

			for cmd in cmds:
				subprocess.run(cmd)


def getCommand():
	return sys.argv[1]


if __name__ == "__main__":

	c = getCommand()
	p = readProjects("notes")
	mkProjects(p, c)



