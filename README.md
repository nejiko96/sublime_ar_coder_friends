# Sublime AtCoderFriends

## Description

Sublime Text plugin that runs [AtCoderFriends](https://github.com/nejiko96/at_coder_friends) commands on current file or project root folder.

## Install

- Install [AtCoderFriends](https://github.com/nejiko96/at_coder_friends).
- Go to Sublime Text Packages directory (Menu > Preferences > Browse Packages...).
- Clone this repository under the Packages directory:
```
git clone https://github.com/nejiko96/sublime_at_coder_friends "AtCoderFriends"
```
- Restart Sublime Text.

## Configuration

Create ```.at_coder_friends.yml``` and place it in the project root folder.

```yaml
user: <user>
password: <password>
```

## Usage

Open Command Palette and select __AtCoderFriends:*__ command.

- **AtCoderFriends: New Contest** creates new contest folder and emits example data and source skeletons

- **AtCoderFriends: Test One** runs first test case of current file.

- **AtCoderFriends: Test All** runs all test cases of current file.

- **AtCoderFriends: Submit** submits code from current file.
