#!/bin/bash

# Add all changes
git add .

# Commit changes with a custom commit message
commit_message="Update changes"
git commit -m "$commit_message"

# Push changes to the master branch on the origin remote
git push origin master
