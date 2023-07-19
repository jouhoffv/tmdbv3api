#!/bin/bash

# Add all changes
git add .

# Commit changes with a custom commit message
commit_message="Update changes"
git commit -m "$commit_message"

# Display the action and filename for each file
git_status=$(git status --porcelain)
while IFS= read -r line; do
    action=$(echo "$line" | awk '{print $1}')
    filename=$(echo "$line" | awk '{print $2}')
    echo "$action -- $filename"
done <<< "$git_status"

# Prompt for confirmation to push
read -p "Do you want to push to the master branch? (y/n) [default: y]: " choice
choice=${choice:-y}  # Set default value to 'y' if no input is provided

# Check the user's choice
if [[ $choice == "y" || $choice == "Y" ]]; then
    # Push changes to the master branch on the origin remote
    git push origin master
else
    echo "Aborted. Changes were not pushed to the master branch."
fi
