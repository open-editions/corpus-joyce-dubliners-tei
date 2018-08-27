# Why contribute?

We're trying to make the best possible edition of _Dubliners_, by encoding literary information about the book in a machine readable format (TEI XML). This will allow the knowledge about the book--which has previously been scattered across academic journals, out-of-print books, and university libraries--to be well-organized, easily accessible, and easily analyzed. 

# Who should contribute?

Anyone who is interested in _Dubliners_, and who is interested in contributing to the community's body of knowledge about it. 

You don't have to be a CS major, or be "technically inclined" to do this. You don't even need to be an English major, or an expert on Joyce. You just need to be curious and willing to learn a thing or two. 

In particular, we could really use help with: 
 - Markup (explained below. Basically, annotating the stories with your observations about them.)
 - Research (learning more about this book, so that we can better describe it.)
 - Graphic design / web design (the design of our upcoming Open-Editions.org website, for instance)
 - Coding (transforming the XML to HTML for display as a website.)
 - Planning (maybe you just have some good ideas for us, or some questions?)
 - Compliance (making our markup and code validate, and streamlining the toolchains we use.)

# How to Contribute
The rest of this document is basically a guide to being a GitHub contributor, for the uninitiated. It assumes no prior technical knowledge. 

## Step 1: Sign up for a GitHub account.
GitHub accounts are free, and you can sign up for one at [github.com](https://github.com/). Try to make sure your real name and main email address are shown somewhere in your user profile, so that your work can be properly credited to you. Please upload a picture, too. This keeps you from being an "egg" (in Twitter terms), or a mysterious masked figure. Our project is friendly, and we're proud of it, so we want to show our faces.

## Step 2: Choose something to contribute. 
Generally speaking, the first place an open-source contributor would want to go is to the GitHub issues page of the project they want to work on. Issues are like a todo list or a bulletin board: they track problems with code (or in our case, text), but also plans for future enhancements, ideas, and even questions. It's our main space for communication about the project. The [issues page for _Dubliners_, as the newest of our projects](https://github.com/Open-editions/corpus-joyce-dubliners-TEI/issues), doesn't have much in it, yet, but the project's ambitions are roughly the same as those in the other books, so check [the issues page for _Portrait_](https://github.com/open-editions/corpus-joyce-portrait-TEI/issues), and [the one for _Ulysses_](https://github.com/open-editions/corpus-joyce-ulysses-tei) for inspiration. Choose an issue that you'd like to work on. 

Once you choose something to work on, create this issue in the _Dubliners_ issue tracker, if it doesn't already exist. If it exists, leave a note in that issue so that others won’t be working on the same thing. For example, let’s say you want to work on marking up dialog for part of a story. First, see if an issue exists for that by looking through the list of issues. It does for _Portrait_--it’s [issue #7: add dialog attribution with format <said who="">](https://github.com/JonathanReeve/corpus-joyce-portrait-TEI/issues/7). If an analogous issue doesn't yet exist for _Dubliners_, create one, and state what you're going to work on in the . Otherwise, look through the comments for that issue to make sure no one else is already working on that section. Then, log in to GitHub, and leave a comment at the bottom of that issue, saying something like “I’ll start working on dialog attribution for part of Chapter 2.”

## Step 3: Fork the project. 
“Forking” is just coding jargon for making a copy of a project. To fork the project, go to [the project homepage](https://github.com/JonathanReeve/corpus-joyce-dubliners-TEI), and click the “Fork” button in the upper right corner. **NB: these screenshots are from the _Portrait_ edition, but are basically the same thing you would see for _Dubliners_.**

![Fork](assets/fork.png)

This will create a copy of the project in your user account where you will make all of your changes. Now your copy lives at `github.com/your-username-here/corpus-joyce-dubliners-TEI`. Navigate to your fork’s homepage, if you’re not already there. You can also find it by going to your profile page and clicking the “repositories” tab. 

## Step 4: Make your edits. 
The stories are currently in the root directory, labeled sequentially. For example, "The Sisters" is 01_sis.xml. They're all imported into one collection by header.xml. Choose a story you've read and are interested in working on, then find the .xml file for that story on your fork. To do that, go to your fork, click the "code" tab, and click the name of the XML file that corresponds to the story you want to work on. It should look like this: 

![XML](assets/xml.png)

but instead of my username, JonathanReeve, you should see your own. To edit the file, click the pencil icon in the upper right: 

![Edit](assets/edit.png)

Now you should be able to make changes to your fork. Find the area in the novel that you want to change (you can click in the text area and use Control+F to search the novel for your section), and then make the changes. For example, here is what my dialog section looked like before: 

![Dialog Before](assets/dialog-before.png)

And here is what it looks like after I make my edit: 

![Dialog After](assets/dialog-after.png)

If you’re not already used to XML, there are a couple things to note here. 

 * The `<said>` tags are inside the `<p>` tags, since the dialog is within the paragraph, not the other way around. 
 * For the attribution (`who=`), I’m writing the full name of the character, not just how they’re referred to in this line of text (i.e. “Simon Dedalus” instead of “Mr. Dedalus”). 
  
If you want a quick introduction to XML, check out [the w3schools introduction](http://www.w3schools.com/xml/xml_whatis.asp), a 10-minute read at most. If you want a more TEI-specific guide, the [TEI Lite Introduction](http://www.tei-c.org/release/doc/tei-p5-exemplars/html/tei_lite.doc.html) is good. 

## Step 5: Commit your changes. 
Now that you’ve made all your changes for this round (you might want to make another, separate set of changes later), you can commit your changes, and describe what it is that you did. **Please reference the issue that you're working on.** For this dialog attribution example, I’ve described my change as `Add dialog attribution to Chapter 2, for issue #7`, and added an additional description that `It was difficult to find Mrs. Dedalus’s first name!`. 

![Commit](assets/commit.png)

Repeat steps 4-5 as necessary, until you’re done making your changes. 

## Step 6: Submit a pull request with your changes. 
Now that you’ve made your changes, you’ll want to submit them to the main edition for approval. A “pull request” is a request to the main project to integrate the changes you made on your fork. To submit a pull request, go to your fork’s homepage, i.e. `github.com/your-username-here/corpus-joyce-dubliners-TEI` and click the button labeled “Pull request”: 

![Pull request](assets/pr.png)

This should bring up a page where you can describe your pull request: 

![Pull request description](assets/pr-message.png) 

Write a description of all the edits you committed. In this example, I wrote roughly the same thing as my commit message, `Add dialog attribution to Chapter 2, for issue #7`, but if you have more than one commit, you’ll want to describe the changes represented by all of your commits.

Before clicking “Create pull request,” scroll down and review your changes once more. If everything looks good, create the pull request. 

# What Tags To Use 

* Attribute dialog by surrounding it with `<said who="">` and `</said>`
* Attribute thought or stream-of-consciousness with `<said who="" aloud="false">`, and `</said>`. 
* Mark up poetry (and verse more generally) by surrounding stanzas with `<lg>` (for “line group”) and lines with `<l>` (for “line”). End each stanza with `</lg>` and each line with `</l>` 
* Mark up personal names with `<persName>` and place names with `<placeName>`. 
* Mark up songs with `<seg type="song">` and prayers with `<seg type="prayer">`
* Mark up foreign languages with, e.g. `<seg xml:lang="fra">`, using the standard 3-letter language codes (ISO-639)

If the feature you’d like to mark up is not in the above list, first see if there’s an issue in [the issue tracker](https://github.com/JonathanReeve/corpus-joyce-dubliners-TEI/issues) for it. If there’s no issue, or if there’s no tag convention in the issue’s comments, consult [the TEI P5 Guidelines](http://www.tei-c.org/release/doc/tei-p5-doc/en/html/). When in doubt, feel free to ask a question [in our Gitter chatroom](https://gitter.im/corpus-joyce-dubliners-TEI/Lobby#). 
