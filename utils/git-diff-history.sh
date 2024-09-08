#!/bin/bash
# -*- coding: utf-8 -*-
#:
#: git-diff-history.sh - Generate a history of diffs for a Git repository
#:
#: Usage: ./git-diff-history.sh
#:
#: This script generates a history of diffs for a Git repository, showing the
#: changes introduced by each commit in reverse chronological order.
#:
#: The output format is as follows:
#:
#: Changes in commit <commit hash> (<commit date>):
#: <diff output>
#:
#: ...and so on for each commit.
#:
#: The script requires Git to be installed and accessible in the system's PATH.
#:
#: Author: Gemini-Pro-1.5-0827
#: Date: 2024-09-09
#:

# change to the root of the repo
cd $(git rev-parse --show-toplevel)

# Get all commit hashes and their dates in reverse chronological order
commits=$(git log --reverse --pretty="%H %aI")

# Iterate through the commits and generate diffs
while IFS= read -r line; do
  # Extract the commit hash and date
  hash=$(echo "$line" | cut -d ' ' -f1)
  date=$(echo "$line" | cut -d ' ' -f2-)

  # Get the parent commit (or empty tree for the initial commit)
  parent=$(git log --pretty="%P" -n 1 $hash)

  # Generate the diff between the current commit and its parent
  echo "Changes in commit $hash ($date):"
  git diff-tree -p $parent $hash
  echo "" # Add an empty line between diffs
done <<< "$commits"