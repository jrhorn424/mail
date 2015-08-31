mail
====

Homeshick-compatible dotfiles for mail

Dependencies
------------

* [`mutt`](http://www.mutt.org): mail user agent
* [`mu`](http://www.djcbsoftware.nl/code/mu/): full-text search and contact search
* [`muttqt`](https://github.com/tgray/muttqt): sent-mail address completion, wrapper for mu
* [`isync/mbsync`](http://isync.sourceforge.net): synchronize IMAP accounts
* [`msmtp`](http://msmtp.sourceforge.net): SMTP client and mail relay

Installation
------------

```
homeshick clone jrhorn424/mail
homeshick cd mail
./install
```

Post-installation
-----------------

You may wish to generate a sent-mail database for `muttqt`. Sync with your IMAP server and then change to your "Sent Mail" folder.

```
for $email in $(\ls $PWD); do muttqt -f $email; done
```

See Also
--------

* [The Homely Mutt / Steve Losh](http://stevelosh.com/blog/2012/10/the-homely-mutt/)
* [A unix style mail setup](http://dev.gentoo.org/~tomka/mail.html)
* [Real Programmers: Jump Start: Mutt -- by hackers, for hackers](http://realprogrammers.com/jump_start/mutt/)
* [Dave's mutt config](http://www.davep.org/mutt/muttrc/)
