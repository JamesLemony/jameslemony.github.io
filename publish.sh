#!/bin/bash
folder="/Users/jameslemony/Vault/06 Coding and Projects/Lemony Website"
vaultFolder="/Users/jameslemony/Vault/02 Obsidian/Public/"
publicFolder="/Users/jameslemony/Vault/06 Coding and Projects/Lemony Website/content"

cd "$folder"

echo "Deleting existing files in the Website folder."
rm -rf "$publicFolder"
sleep 0,3

echo "Create new content folder."
mkdir "$publicFolder"
sleep 0,3

echo "Copying files from main folder to Website folder."
cp -R "$vaultFolder" "$publicFolder"
sleep 0,3

echo "Executing Python script for adjusting line breaks."
python3 lineBreaks.py
sleep 0,7

echo "Sending the files for publishing.."
npx quartz sync

echo "Publishing complete."