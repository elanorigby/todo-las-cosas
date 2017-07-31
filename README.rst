Todo las Cosas
==============

This is to be a project-specific command line managed todo list.

Initialize it in the home folder of your project. Use it anywhere
below the home folder in the file tree.

Current design
--------------

command: todo

options
~~~~~~~
--done, -d

--remove, -r (deletes item, confirm first)


subcommands
~~~~~~~~~~~
* done (show numbered list of done items)
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


example
-------

::
    $ todo "ride to camelot"
    $ todo "seek the grail"
    $ todo

    TODO
    | 1 - ride to camelot
    | 2 - seek the grail

    $ todo -r 1
    Are you sure you want to remove "ride to camelot"? [Y]/n
    '->
    "ride to camelot" has been removed

    $ todo

    TODO
    | 1 - seek the grail

    $ todo -d 1
    $ todo

    TODO
    | nothing nada rien semmi tipota

    $ todo done

    DONE
    | 1 - seek the grail

    # can also mark multiple items at once (with the same mark)

    TODO
    | 1 - tab completion for del
    | 2 - seek the grail

    $ todo -d 1 2
    "tab completion for del" and "seek the grail" marked done

    $ todo

    TODO
    | nothing nada rien semmi tipota

    $ todo done

    DONE
    | 2 - seek the grail
    | 1 - tab completion for del

    # todo las_cosas

     Todo las Cosas
    -----------------
     TODO
    ******
    - tab completion for del
        (created 04/08/17 14:56)

     DONE
    ******
    - all the stuff
        (created 04/08/17 14:56)
        (marked done 06/08/17 12:23)
    - you've got
        (created 04/08/17 14:56)
        (marked done 06/08/17 12:23)
    - done good
        (created 04/08/17 14:56)
        (marked done 06/08/17 12:23)
    - job, you.
        (created 04/08/17 14:56)
        (marked done 06/08/17 12:23)




