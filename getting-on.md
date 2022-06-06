---
layout: default
---

##  Getting on

Got hooked? If you fancy your own GitHub webpage that allows you to programme Python in the browser, we've got something for you:

0. Get your GitHub account at https://github.com/
1. Go to [https://github.com/Durham-Hackathon/template-website](https://github.com/Durham-Hackathon/template-website)
2. In the upper right corner, click on `fork`
3. In the forked repo, go to `Settings` → `Pages`
4. Change the `Source`: `None` → `gh-pages` → `save`
5. Your website will now be built. You may need to wait for a while for it to be available. 
6. Click on the link at the top of the `Settings` page to visit your webpage. 
7. In case your website is not yet deployed, you may want to check for error messages by clicking on Actions and expanding.

In order to edit the content on your webpage or to persist your code:
1. Write and test your code in the browser
2. Go to your fork of the template-website
3. Click on `index.md` to open it
4. In the upper right corner, click on the pen to edit the file
5. To persist your code, add it between the HTML tags of the textarea `id=yourcode`
6. On the bottom of the page, click `Commit changes`
7. Wait for the website to be generated

To change the content of your webpage, you should only need to change and add Markdown files, meaning, the files with an *.md* ending.
You can change the title and description of the website in the .yml configuration file, please make further changes only if you know what you are doing :-) 

Fancy different themes and colours? The [Jekyll documentation](https://jekyllrb.com/docs/) will teach you how to do that.

This short tutorial on [github markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) will teach you how to write new content, e.g. to add pictures.

This theme is called architect, you can find configuration options for it [here](https://github.com/pages-themes/architect).

## Running outside of the browser
You may also want to install python and run these files outside of the browser. In this case whenever you close the turtle window you will crash your code. So perhaps add:

    def on_close():
        global running
        running = False
    window.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)

And instead of running a loop `while True` run 

    running = False
    while running:
        # Your code here



