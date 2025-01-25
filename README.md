# Documentation

This repo holds the raw documentation.

The workflow will automatically generate pages and publish them in the projects Confluence wiki.

Diagrams will also automatically generated and uploaded to the specific page.

The Confluence user id and API token is stored as an environment secret in this repo.

We use an adaptation of [GitHub to Confluence Publisher](https://github.com/andygolubev/github-to-confluence-publisher) and [Python diagrams](https://diagrams.mingrammer.com/).

## Pipeline tests

The markdown files will be linted in the workflow with `pymarkdown --disable-rules MD013,MD024,MD041 scan pages`

### Rules Explanation

| Code        | Description | Reasoning |
| ----------- | ----------- |-----------|
| MD041       | First line in file should be a top-level heading.| In Confluence there is a heading on every page already.|
| MD013       | Line length | For a documentation in Confluence the 80-character limit does not make much sense.|
| MD024       | Multiple headings cannot contain the same content.| Subheadings in different sections should indeed be able to contain the same content.
