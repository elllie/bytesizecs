---
title: "Q&A"
parent: "0. Introduction"
has_children: false
has_toc: true
nav_order: 100
---

# Chapter 0 - Introduction: Student Questions!

This page has public answers to some of our most frequently asked questions for this chapter.

Question not answered here, but you'd like it to be? [Shoot us a voice message](https://anchor.fm/bytesizecs/message) and we might feature it here and in the podcast!

## Terminal/command line syntax: How to get the terminal to listen to your commands

The terminal can be confusing when you first start using it. After a while it will become second nature. 

The terminal only accepts sentences in a certain format and gets really confused if you give it something else.

### Anatomy of a terminal command

![anatomy of a terminal command](../../assets/terminal-anatomy.png)

Any given line in a terminal window will look like this:

1. The username of whoever is using the terminal. (Probably your name.)
2. The current folder on your computer where the terminal window is operating out of. This is important context because when you're opening files, you'll have to give the terminal directions on where to find those files *from where you are currently.*
3. A symbol separating that contextual information from the stuff you'll type in. Sometimes this is a %, sometimes it's a $, sometimes it's a > or something else. You can't type to directly modify the symbol or anything before it, but you can change your user and location through commands.
4. The command you are executing.
5. The thing you want to execute that command on or with.
6. Optionally, you'll also see "flags" at the end of a command denoted with a `-`. These are kind of like adjectives that modify the command you're giving.

Some examples of this:

#### Change the folder you're in

```sh
username currentFolder % cd newFolder
```
The verb is `cd` ("change directory") and the noun (place) we want to `cd` to here is `newFolder`.

After you run this command, `newFolder` should replace `currentFolder` on the left.

You can also give it a whole path to a different folder, e.g. `cd insideFolder/path/to/anotherFolder/newFolder2`. In this case, `newFolder2` will replace `currentFolder` once the command is executed successfully.

#### Run a Python program

```sh
username currentFolder % python pythonFile.py
```
The verb is `python` and the noun (program) we want to `python` here is `pythonFile.py`. If your python program is in a different location than `currentFolder`, you'll have to tell the terminal where to find it, e.g. `python insideFolder/pythonFile.py`.

#### See who owns a particular Web address (Mac/Linux only)

```sh
username currentFolder % whois ncf.edu
```
For this command, the current location doesn't matter at all. The verb is `whois` and the noun (website) we want to `whois` here is `ncf.edu`. When you run this command, the `whois` program built into your (Mac/Linux) computer will search internet directories to find out who owns the domain name you specified.

If you want to learn more about the command-line interface and things you can do with the terminal, I found [this cool guide](https://medium.com/@JuxtaposedWords/an-introduction-to-mac-s-terminal-part-i-cli-vs-gui-b6acd3794d7c) with a lot of good information for beginner to intermediate terminal users.

### Common mistakes

## Writing code and using the terminal is intimidating! Isn't there a less scary way where I can just click buttons?

## Who made the first programming language?

## How are programming languages developed? For what purposes are they created?

## What makes Python special?
