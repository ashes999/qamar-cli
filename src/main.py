import os
import sys
from zipfile import ZipFile
import io.directory as Directory

class Main:

    def __init__(self):
        self.valid_commands = {
            "create": self.create_template
        }

    def execute(self, args):
        if len(args) == 0:
            print("Usage: qamar <command> <args>. Valid commands are: {0}".format(self.valid_commands.keys()))
            sys.exit(1)
        else:
            command = args[0]
            if not self.valid_commands.has_key(command):
                print("Unknown command: {0}. Valid commands are: {1}".format(command, self.valid_commands.keys()))
                sys.exit(1)                
            else:
                args = args[1:]
                self.valid_commands[command](args)

    def create_template(self, *args):
        args = [a for a in args[0]]
        x= ""        
        templates = [f[0:f.rindex('.')] for f in os.listdir('templates') if f.endswith('.zip')]
        if len(args) != 2:
            print "Usage: create <template> <target directory>. Valid templates are: {0}".format(templates)
            sys.exit(1)            
        else:
            template = args[0]
            destination = args[1]
            zip_candidates = [f for f in templates if f.lower() == template.lower()]
            if len(zip_candidates) != 1:
                print("'{0}' doesn't seem to be a valid templates. Templates are: {1}'".format(template, templates))
                sys.exit(1)            
            else:
                zip_name = zip_candidates[0]
                Directory.ensure_exists(destination)
                with ZipFile('templates/{0}.zip'.format(zip_name), 'r') as template_zip:
                    template_zip.extractall(destination)
                print("Created template for {0} at {1}".format(template, destination))
