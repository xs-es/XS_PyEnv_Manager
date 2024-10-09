import sys
import os
from PyQt5 import QtWidgets, QtCore
from xsPyEnv_ui import Ui_MainWindow  # Import the converted UI Python file
import subprocess

class VenvManager(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect UI elements to their corresponding actions
        self.createVenvButton.clicked.connect(self.create_virtual_env)
        self.installButton.clicked.connect(self.install_package)
        self.searchButton.clicked.connect(self.search_python_versions)

        # Initialize Python versions (using pyenv or default)
        self.populate_python_versions()

    def populate_python_versions(self):
        """Populate available Python versions using pyenv"""
        try:
            # Fetch available Python versions (pyenv-win or pyenv)
            result = subprocess.run(["pyenv", "versions"], capture_output=True, text=True)
            versions = result.stdout.splitlines()
            self.pyVersionBox.addItems([v.strip() for v in versions if v.strip()])
            self.statusView.append("Python versions populated successfully.")
        except Exception as e:
            self.statusView.append(f"Error populating Python versions: {str(e)}")

    def create_virtual_env(self):
        """Create a virtual environment using the selected Python version"""
        selected_version = self.pyVersionBox.currentText()
        venv_name = self.searchBox.text()

        if not venv_name:
            self.statusView.append("Please provide a virtual environment name.")
            return

        try:
            # Create the virtual environment using pyenv or python
            result = subprocess.run(
                ["pyenv", "virtualenv", selected_version, venv_name],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                self.statusView.append(f"Virtual environment '{venv_name}' created successfully.")
                self.refresh_installed_envs()
            else:
                self.statusView.append(f"Error creating virtual environment: {result.stderr}")
        except Exception as e:
            self.statusView.append(f"Failed to create virtual environment: {str(e)}")

    def install_package(self):
        """Install a package in the currently selected virtual environment"""
        package_name = self.searchBox.text()
        selected_env = self.installedView.currentItem()

        if not package_name or not selected_env:
            self.statusView.append("Please provide a package name and select a virtual environment.")
            return

        try:
            # Activate the environment and install the package
            result = subprocess.run(
                ["pyenv", "activate", selected_env.text()],
                capture_output=True, text=True
            )
            if result.returncode != 0:
                raise Exception(result.stderr)

            result = subprocess.run(
                ["pip", "install", package_name],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                self.statusView.append(f"Package '{package_name}' installed successfully.")
            else:
                self.statusView.append(f"Error installing package: {result.stderr}")
        except Exception as e:
            self.statusView.append(f"Failed to install package: {str(e)}")

    def refresh_installed_envs(self):
        """Refresh the list of installed virtual environments"""
        try:
            # Fetch the installed virtual environments using pyenv
            result = subprocess.run(["pyenv", "virtualenvs"], capture_output=True, text=True)
            envs = result.stdout.splitlines()
            self.installedView.clear()
            self.installedView.addItems([e.strip() for e in envs if e.strip()])
            self.statusView.append("Installed environments refreshed.")
        except Exception as e:
            self.statusView.append(f"Error refreshing environments: {str(e)}")

    def search_python_versions(self):
        """Search available Python versions (dummy implementation)"""
        self.statusView.append("Searching for available Python versions...")
        self.populate_python_versions()

    def closeEvent(self, event):
        """Ensure proper cleanup on application close"""
        result = QtWidgets.QMessageBox.question(
            self,
            "Confirm Exit",
            "Are you sure you want to exit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VenvManager()
    window.show()
    sys.exit(app.exec_())
