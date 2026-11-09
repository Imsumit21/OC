# Baseline All-Fail Justifications

All 6 baseline rollouts completed, so an all-fail rubric is one that failed in all 6. 2 rubrics failed in all 6, and 2 are valid.

## The Agent shows a count of 5 holders labeled "Already told" on its holder sheet

The holder sheet had to count 5 rows labeled Already told: ENG-2438, ENG-2439, ENG-2440, ENG-2446 and ENG-2447. The prompt points to Leonard's close-out notes, which define told as a written message about the closing sent directly to the holder by a founder, and Sunset's intake mail asks for a count of holders by what each still needs to hear. Two of the five are told only in Leonard's own records: his Feb 9 direct message to the ENG-2440 holder ('shut down the company we decided') and Robert's Feb 12 mail to the ENG-2446 holder with Leonard copied ('we're closing the company'). No run used both. Runs 1, 2, 4 and 6 labeled ENG-2440 Closing (run 4 wrote 'No direct closing message found'), and runs 3 and 5 labeled ENG-2446 Closing (run 5 wrote 'Not told'), so all six count blocks give 4 for Already told instead of 5.

## The Agent shows a count of 5 holders labeled "Closing" on its holder sheet

The holder sheet had to count 5 rows labeled Closing: ENG-2441, ENG-2442, ENG-2443, ENG-2448 and ENG-2449. Sunset's intake mail asks for a count of holders by what each still needs to hear, and Leonard's close-out notes, which the prompt points to, treat a holder who already had a direct written closing message from a founder as Already told, not Closing. Every run moved one told holder into Closing: runs 1, 2, 4 and 6 missed Leonard's Feb 9 direct message to the ENG-2440 holder, and runs 3 and 5 missed Robert's Feb 12 mail to the ENG-2446 holder. Run 4 also put the Covered lines ENG-2444 and ENG-2445 under Closing and run 5 put ENG-2444 there, so the six count blocks give 6, 6, 6, 8, 7 and 6 instead of 5.
