# CloudServer

Cloud Drive: Secure, user-friendly file storage with automatic backup and cross-device synchronization, developed using Django, ensuring data safety and accessibility in the digital age.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Register, login, and manage user profiles.
- **Device Management**: Add, view, edit, and delete devices associated with a user.
- **File Management**: Upload, download, view, and delete files associated with a device.
- **Secure Storage**: Files are stored securely with a structured directory system.
- **Cross-Device Synchronization**: Access your files from any device associated with your account.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dev-Yassin/CloudServer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd CloudServer
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Register a new user or log in with existing credentials.
2. Add devices to your account.
3. Upload files to a specific device.
4. Download or delete files as needed.

## Directory Structure

- `cloud_server_app`: Main application directory containing models, views, templates, and other app-specific files.
- `cloud_server_project`: Project configuration directory.
- `media`: Directory where user files are stored, structured by username and device.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/dev-Yassin/CloudServer/blob/main/LICENSE) file for details.
