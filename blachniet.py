import os
import subprocess
import sublime
import sublime_plugin

class BlachnietTextCommand(sublime_plugin.TextCommand):
    def get_working_dir(self):
        '''Gets the current working directory of the current view. Returns None
        if the current document has not been saved.
        
        '''
        if self.view is None or self.view.file_name() is None:
            return None
        return os.path.dirname(self.view.file_name())    

class BlachnietApplicationCommand(sublime_plugin.ApplicationCommand):
    def get_working_dir(self):
        '''Gets the current working directory of the active view in the active window.
        If the active window is None, active view is None, or the view has not been saved,
        then None will be returned
        
        '''
        active_window = sublime.active_window()
        if active_window is not None:
            active_view = active_window.active_view()
            if active_view is not None:
                file_name = active_view.file_name()
                if file_name is not None:
                    return os.path.dirname(file_name)
        return None

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
                subprocess.Popen('explorer.exe "' + working_dir + '"')
        else:
            sublime.status_message("Could not open folder. This feature is only supported on Windows.")

class OpenPowerShellHere(BlachnietApplicationCommand):
    '''Opens powershell.exe to the current file's directory. If the current file has not been saved, this command will 
    open powershell to the user's directory (~)

    '''

    def run(self):
        if os.name == 'nt':
            sublime.status_message("Opening PowerShell...");

            working_dir = self.get_working_dir()
            if working_dir is None:
                subprocess.Popen('powershell.exe -noexit -command "cd \'~\'"')
            else:
                subprocess.Popen('powershell.exe -noexit -command "cd \'' + self.get_working_dir() +'\'"')
        else:
            sublime.status_message("Could not open PowerShell. This feature is only supported on Windows.")
