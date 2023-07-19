#!/bin/bash

# Add all changes
git add .

# Commit changes with a custom commit message
commit_message="Update changes"
git commit -m "$commit_message"

# Display the changes
git_diff=$(git diff --numstat)
changes=()
while IFS= read -r line; do
    added=$(echo "$line" | awk '{print $1}')
    deleted=$(echo "$line" | awk '{print $2}')
    filename=$(echo "$line" | awk '{print $3}')
    
    if [[ $added != 0 && $deleted != 0 ]]; then
        change="changed"
    elif [[ $added != 0 ]]; then
        change="insertions"
    elif [[ $deleted != 0 ]]; then
        change="removals"
    fi

    changes+=("$change: \"$filename\"")
done <<< "$git_diff"

# Prepare and display the changes summary
echo "---"
if [[ ${#changes[@]} -eq 1 ]]; then
    echo "${changes[0]}"
else
    echo "${#changes[@]} files changed"
    for change in "${changes[@]}"; do
        echo "- $change"
    done
fi

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
