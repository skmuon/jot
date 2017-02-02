# jot
Simple tool to log work log

__Files__
- jot.py 
- dwlog.sh

Simple framework to log work related information. The information will be appended to textfile (worklog.txt).
The tool prepends user provided information with current and data and time. These are stored in CSV format.

Format : [Data],[Time],[Information],

Shell script (dwlog.sh) can be used to dump information from worklog.txt file. The shellscript accepts arguments to filter the outputs. In simple format user can provide date information to get relevant work log.

__sample worklog.txt__
```

----------------------------------------------------------------------
2017-02-02  21:03,Merged initial version to GitHub,
2017-02-02  21:03,Started working on jot utility,

```
__sample output from dwlog.sh__

```


Merged initial version to GitHub
Started working on jot utility
```
