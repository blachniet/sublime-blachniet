import os
import subprocess
import sublime
import sublime_plugin

class BlachnietTextCommand(sublime_plugin.TextCommand):
    def get_working_dir(self):
        '''Gets the current working directory of the current document. Returns None
        if the current document has not been saved.

        '''
        file_name = self.view.file_name()
        if file_name is None:
            return None
        return os.path.dirname(self.view.file_name())    

class OpenContainingFolder(BlachnietTextCommand):
    '''Opens a file browser to the current file's containing folder. If the current file has
    not been saved, then the file browser will be opened to some default location.

    '''
    def run(self, edit):
        if os.name == 'nt':
            sublime.status_message("Opening folder...")

            working_dir = self.get_working_dir()
            if working_dir is None:
                subprocess.Popen('explorer.exe')
            else:
                subprocess.Popen('explorer.exe "' + self.get_working_dir() + '"')
        else:
            sublime.status_message("Could not open folder. This feature is only supported on Windows.")

class OpenPowerShellHere(BlachnietTextCommand):
    '''Opens powershell.exe to the current file's directory. If the current file has not been saved, this command will 
    open powershell to the user's directory (~)
    
    '''
    def run(self, edit):
        if os.name == 'nt':
            sublime.status_message("Opening PowerShell");
            working_dir = self.get_working_dir()
            if working_dir is None:
                subprocess.Popen('powershell.exe -noexit -command "cd \'~\'"')
            else:
                subprocess.Popen('powershell.exe -noexit -command "cd \'' + self.get_working_dir() +'\'"')
        else:
            sublime.status_message("Could not open PowerShell. This feature is only supported on Windows.")
