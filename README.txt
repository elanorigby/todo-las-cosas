-------------Todo las Cosas-------------


This is to be a project-specific command line managed todo list.

Initialize it in the home folder of your project. Use it anywhere
below the home folder in the file tree.

Current design

commands: todo

options
    --done, -d (moves item to done list)
    --remove, -r (deletes item, confirm first)


subcommands
    done (show numbered list of done items)
    las_cosas (all lists, todo and done, [with dates])

arguments
    "item text"


example

$ todo "ride to camelot"
$ todo "seek the grail"
$ todo

TODO
| 1 - ride to camelot
| 2 - seek the grail

$ todo -r 1
Are you sure you want to remove "ride to camelot"? [Y]/n y
"ride to camelot" has been removed

$ todo

TODO
| 1 - seek the grail

$ todo -d 1
$ todo

TODO
| nada

$ todo done

DONE
| 1 - seek the grail

# can also mark multiple items at once (with the same mark)

TODO
| 1 - ride to camelot
| 2 - seek the grail

$ todo -d 1 2
"ride to camelot" and "seek the grail" marked done

$ todo

TODO
| nothing nada rien semmi tipota

$ todo done

DONE
| 2 - seek the grail
| 1 - ride to camelot

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




