cd /home/sumit/Downloads/OC/OC; W=Task_Authoring-2/support/task_work/rb_winddown_closeout
H="python3 Task_Authoring-2/tools/hg.py search lookup"
$H slack --ids-file $W/ids_slack.json --file 'messages/*.json' > $W/coll_slack.json 2>/dev/null
$H linear --ids-file $W/ids_linear.json --file 'data.json' --pointer /issues > $W/coll_linear_issues.json 2>/dev/null
$H linear --ids-file $W/ids_linear.json --file 'data.json' --pointer /projects > $W/coll_linear_projects.json 2>/dev/null
$H gdrive --ids-file $W/ids_gdrive.json --file 'data.json' --pointer /drive_files > $W/coll_gdrive.json 2>/dev/null
$H trello --ids-file $W/ids_trello.json --file 'data.json' --pointer /cards > $W/coll_trello_cards.json 2>/dev/null
$H trello --ids-file $W/ids_trello.json --file 'data.json' --pointer /actions > $W/coll_trello_actions.json 2>/dev/null
$H confluence --ids-file $W/ids_confluence.json --file 'confluence_working.json' --pointer /pages > $W/coll_conf_pages.json 2>/dev/null
$H confluence --ids-file $W/ids_confluence.json --file 'confluence_working.json' --pointer /comments > $W/coll_conf_comments.json 2>/dev/null
echo done
