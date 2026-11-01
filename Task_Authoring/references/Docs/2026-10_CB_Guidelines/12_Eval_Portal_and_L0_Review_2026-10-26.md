<!-- Source: CB guideline PDF (watermarked copy) (Archive 6.zip, received 2026-11-01). Text extracted with pdftotext; watermark lines removed; two-column pages may interleave. -->

Eval Portal and L0 Review
HarmonyGames · Fixed environment date: October 1, 2025 or February 14, 2026, 00:00 UTC · Updated
October 26, 2026
How to run your reviews in the Original Conference Eval Portal, and how to submit the pass screens that prove
each one passed.
0 · The flow at a glance
ONLY THE PASS SCREEN COUNTS
Report cards, chat messages and FAIL results are not accepted as proof. Every passing review needs its own
pass screen screenshot.
1.​ Log in to the Eval Portal with your email or Outlier ID and your attempt ID.
2.​ Explore the data in the chat while you build your task.
3.​ Add your task inputs in the chat.
4.​ Run the reviews: /injection, /prompt, /hardness, /oe, and /rubric, the same ones you ran before.
5.​ Screenshot the pass screen of every review that passes.
6.​ Post your proof in the Eval Pass Submission form.
Open the Eval Portal and sign in with two things: your email or Outlier ID (make sure to add + outlier towards the
end), and the attempt ID from your task page. The attempt ID works for a task you are still working on, too, and the
portal checks that it belongs to your account. Everything you add and every review you run is saved to that attempt.
The sign-in screen
2 · Explore the data
What to type (examples)
Which Slack channels talk about the Combo Fighters
launch?
Find where something lives
List the messages in #zombie-marketing dated after
February 10, 2026.
EXPLORE, DO NOT WRITE
What was the total Meta spend in Snowflake for
February 1-11, 2026?
Get a value you will reuse
Can Marcus Bennett read #ua-spend?
Show the Linear tickets assigned to Leonard, with their
state and due date.
Check what your persona can see
Check dates
What you want
Read specific records
Use the portal to look through the universe while you build your task. Type your question in the chat with no
command in front of it, and the portal answers from the universe data. Explore before you write your prompt and
SQL injection, and come back whenever you need to check a value.
You may use the portal to explore the universe and evaluate your task. You may not use it to write your
prompt, your Oracle Events, or your rubric criteria.
3 · Add your task inputs
Paste your inputs into the chat, or attach them as files with Attach. Each input is saved to the attempt and listed
under Saved inputs in the sidebar: your prompt, the task details (persona, role, business function, competency, task
skill and horizon, universe date and difficulty mode), your error / async config, your injection SQL, and later your
Oracle Events and rubric.
Saved inputs in the sidebar
Click a saved input to see exactly what the eval will use. You can download it from there.
One Opus trajectory: is the task hard enough to
continue
/hardness
Sending an input again replaces the saved one. If you change your prompt or your SQL, send the new version before
you run the review again.
The trajectory JSON from your
Opus pre-check, attached as a file
Unique answer, feasibility, persona access and
clarity
The exact task prompt, plus persona, business
function, competency, task skill and horizon
/prompt
IDs, structure and chronology of your injection
SQL against the universe
Type the command and the portal shows what the review needs and which inputs are saved for this attempt. Click
Start review to begin.
Your injection SQL
/injection
Your rubric, as JSON
Criteria, weights and facts
/rubric
Your Oracle Events
Your Oracle Events path
4 · Run a review
What it needs
What it checks
Command
A saved input, exactly as the eval will use it
When a review passes, a pass screen pops up. A review counts as passed when it returns PASS, or NON-FAIL with a
complete run. The pass screen shows:
•​ the verdict and the review it belongs to, for example PASS, /injection · Injection review · COMPLETE
•​ a verification code in the card EVP-XXXX-XXXX-XXXX
•​ your attempt ID and user, when the review was completed, and how long it ran
•​ the model calls and tokens it used, the report hash, and a link to check the pass
The portal runs the same evals as the sandbox. A FAIL still blocks the task: fix the artifact and run the review
Anything you type without a command is answered as a follow-up about your attempt, for example, "why did
criterion 4 fail?". To reach a person, type /admin followed by your message.
A review takes about 20–40 minutes, and an attempt runs one review at a time. You can close the page while it
runs; the result appears in the chat and is saved to the attempt. If an input is missing, the review asks you for it in
the chat.
6 · What counts as proof
5 · Ask questions
THE SAME REVIEWS AS BEFORE
Starting a review
Closed the pass screen by accident? Reopen it from Passes in the sidebar, or click Show pass screen on the pass
card in the chat. The sidebar lists your Reports and your Passes for the attempt.
Screenshot the whole pass screen, with the verification code visible. Take one screenshot for each passing review.
Reports and Passes in the sidebar
A full pass screen
Counts as proof
Does not count
Chat messages
One screenshot per passing review
Report cards
The pass screen, whole, with its verification code
PASS, or NON-FAIL with a complete run
FAIL results
7 · Post your proof
1. Open the form at the Eval Pass Submission link, signed in with a Google account. The form needs one to accept
image attachments.
2. Fill in your details: your handle or email address, your task ID, and every review that passed.
3. Add each pass by entering its verification code and attaching its pass screen screenshot.
4. Send one entry per task. If a later run of the same task passes, update the form with the new screenshot and
verification code.
8 · Before you submit, check these things
• ☐ I logged in with my email or Outlier ID and the attempt ID of this task.
• ☐ Every ID, name, date, and figure in my task was checked in the portal, from my persona’s view.
• ☐ The saved inputs are the final versions of my prompt, SQL, Oracle Events, and rubric.
• ☐ /injection, /prompt, /hardness, /oe, and /rubric each returned PASS, or NON-FAIL with a complete
• ☐ I have one whole pass screen screenshot for each passing review, with the verification code visible.
• ☐ I submitted every pass screen and its verification code in the Eval Pass Submission form.
Original Conference · Eval Portal and L0 Review · Spec V2 · Updated Oct 26, 2026
