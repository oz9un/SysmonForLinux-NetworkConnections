import sys, os
from xml.etree import ElementTree as ET

class ruleGroupCreator:
	def __init__(self, current_config, target_file):
		self.target_file = target_file
		self.base_config = "base.xml"
		self.current_config = current_config
	

	def readDestinations(self):
		file = open(self.target_file, 'r')
		self.banned_destinations = [dest.rstrip('\n') for dest in file.readlines()]
		

	def readBaseConfig(self):
		file = open(self.base_config)
		self.basexml_parsed = [line.rstrip('\n') for line in file.readlines()]


	def createBannedConfigs(self):
		self.newConfigLines = []
		for bannedIp in self.banned_destinations:
			base_filter = ['<DestinationIp ', 'condition="is">', str(bannedIp) , '</DestinationIp>']
			self.newConfigLines.append("".join(base_filter))
		
		temp_file = open("tempconfig.xml", 'a+')
		temp_file.write('<NetworkConnect onmatch="include">\n')
		for bannedIp in self.newConfigLines:
			temp_file.write(bannedIp)
			temp_file.write('\n')
		temp_file.write('</NetworkConnect>')


	def finalConfigFile(self):
		self.base_tree = ET.parse(self.current_config)
		self.new_tree = ET.parse("tempconfig.xml")

		if os.path.exists("tempconfig.xml"):
			os.remove("tempconfig.xml")
		else:
			print("The file does not exist") 

		eventFilter = self.base_tree.find("./EventFiltering")
		eventFilter.append(self.new_tree.getroot())

		self.base_tree.write("final.xml")

	def run(self):
		self.readDestinations()
		self.readBaseConfig()
		self.createBannedConfigs()
		self.finalConfigFile()

if __name__ == '__main__':
	rgc = ruleGroupCreator(sys.argv[1], sys.argv[2])
	rgc.run()
