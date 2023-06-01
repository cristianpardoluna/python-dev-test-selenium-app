# Test python developer
**Author:** Cristian Pardo (cristianpardoluna@gmail.com)
## Test
Create a program that collects articles from the https://www.bbc.com/news website. We are only interested in the sections "/business" (Business - without the "Features & Analysis", "Watch/Listen" and "Special reports" subsections) and "/technology" (Tech - without the Watch/Listen and Features & Analysis subsections).

- The script should save every article to a separate JSON file, keeping only the article content (TITLE and BODY). All non-relevant content (external links, links to categories, CSS, scripts, multimedia content, etc.) should be removed.

- Make sure to keep track of the downloaded content. If run again, the script should only collect articles we have not downloaded already.

- (bonus) Containerize your Python application. Outputs should be outside the container.

The program should be written in Python and could use the Selenium framework.

## Solution
This program creates a `.json` files from BBC articles from the business section. \
It takes advantage of Python's ``threading`` library and starts a new thread for each request that the chronium driver has to do in order to get the article's data. \
It uses ``Selenium`` to query and select the matching data. \
If the article data exists it won't start a new thread. \
If the following steps are executed **the user can get the outputs (.json files) in a local path**.

## How to run the program 
1. Build the image:
    ```sh
    docker build . -t selenium-app
    ```
2. Run the container:
    ```sh
    # NOTE: declare the VOLUME so you can get the results in /local/path/results once the container exits
    docker run -v /local/path/results:/app/results
    ```
3. See the results in `/local/path/results` as `.json` file.
