Todo las Cosas
==============

This is to be a project-specific command line managed todo list.

Initialize it in the home folder of your project. Use it anywhere
below home folder in the filetree.

Current design
--------------

command: todo

options
~~~~~~~
--done, -d
--remove, -r (deletes item, confirm first)
--amend (last added item)
--resurrect (last item done'd)

subcommands
~~~~~~~~~~~
* done (numbered list of done items)
* las_cosas (all items, ip and done, [with dates])

arguments: "item text"

    ``$ todo [--done][-d] [--remove][-r] [--amend] [--resurrect] <item id>``

    ``$ todo "item text"`` - adds to todo list

    ``$ todo`` - shows todo list (numbered)
    ``$ todo done`` - shows items in done list (numbered)
    ``$ todo las-cosas`` - shows all items now and ever, with dates

    ``$ todo -r <int>``
    ``confirm: delete "chosen item text"`` - deletes item

    ``$ todo -d <int>`` - "item text" marked as done - moves item to done list



