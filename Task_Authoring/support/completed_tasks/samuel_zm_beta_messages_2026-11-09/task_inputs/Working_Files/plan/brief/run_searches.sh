#!/bin/sh
# Natural searches as Samuel for brief section 5a. Workspace root. persona_view search reads the base only.
O=Task_Authoring/task_inputsK/Working_Files/plan/brief/search_out.txt; : > $O
s(){ svc=$1; shift; timeout 170 python3 -B Task_Authoring/tools/persona_view.py search samuel_turner $svc "$@" --limit 10 >> $O 2>&1; echo "" >> $O; }
s gsheets "Push Notifications Zombie Match"
s gdocs "GTM - Beta"
s gdrive "Push Notifications Zombie Match"
s slack "shove" --no-hidden
s slack "variant c" --no-hidden
s slack "notfication pop ups" --no-hidden
s slack "All our PNs are local" --no-hidden
s slack "required versions" --no-hidden
s slack "Axe Arena" --no-hidden
s slack "Beta target" --no-hidden
s slack "desert theme" --no-hidden
s slack "could you help me test the build" --no-hidden
s gmail "PR #248" --no-hidden
s gcal "review" 
s trello "Push Notifications"
s trello "Fix TECH ISSUES"
s trello "Minor Bugs to Fix"
s trello "Hourly Collection"
s trello "Rewarded Ads"
s trello "Axe Arena"
s linear "Boss Arena"
s linear "daily gift"
s linear "Rate us"
s linear "red dot"
s linear "permission"
s github "Push notification"
s confluence "Collect & Win"
s confluence "release checklist"
s contacts "Brian Foster"
s confluence "Same feature as Win"
s confluence "live-ops calendar"
s contacts "brian.foster"
s linear "Collect"
s trello "Win and Collect"
s gslides "readiness"
s confluence "Collect"
s confluence "under a different name"
s slack "shove it to level 20" --no-hidden
s slack "notification pop up is triggered at level 13" --no-hidden
s slack "PNs are at the beginning" --no-hidden
s slack "postpone Axe Arena" --no-hidden
s slack "the PNs for Zombie Match" --no-hidden
s gsheets "Push Notifications Domino"
