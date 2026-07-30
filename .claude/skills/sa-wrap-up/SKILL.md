---
name: sa-wrap-up
description: Wrap up or pick up a South Air Helicopters website work session. Use this whenever the user says they want to pause, stop, wrap up, take a break, call it here, or save state on the SA site — and equally when they come back and ask where things stand, what's next, or "let's keep going on the helicopter site." Also use it when they hand over new client material (photos, pricing, history, hours, the Bell logo, a domain) and you need to fold it into the tracked state. Keeps PROJECT-STATUS.md honest about what is real content versus placeholder, what is waiting on Mike or the office manager, and what got decided.
---

# SA Wrap Up / Pick Up

This project is a website for a real, small, family-adjacent business. The user is
building it for pay, on nights and weekends, in bursts separated by days. Between
bursts, the state of the work lives in exactly one place: `PROJECT-STATUS.md` at the
repo root. Everything here exists to keep that file trustworthy, because if it drifts
out of date it becomes worse than useless — the user will act on it and be wrong.

The defining fact of this project: **most page copy is placeholder text waiting on the
client.** The interesting state isn't "which files exist" (they all do) — it's *which
sentences are real and which are still a guess.* Track that above all else.

## Which mode am I in?

Read the signal from the user, don't ask if it's obvious:

- **Wrapping up** — "let's pause", "stop here", "wrap up", "I'm done for tonight",
  "save where we are." Run *Wrap Up* below.
- **Picking up** — "where were we", "what's next", "let's keep going", or the first
  substantive message of a fresh session. Run *Pick Up* below.
- **New client material arrived** — they paste or attach real info (hours, pricing,
  a photo, the Bell logo, the domain). Do the actual work of folding it in first,
  then run *Wrap Up* so the tracker reflects it.

If genuinely ambiguous, pick up — orienting is cheap and never destructive.

---

## Pick Up

The goal is for the user to be able to start working within one message, without
re-reading the whole repo or re-deciding things already decided.

1. **Read `PROJECT-STATUS.md` first.** It is the source of truth for intent.
2. **Verify it against reality rather than trusting it.** The file was written by a
   past session that may have been interrupted before it could save. Check:
   - `git log --oneline -8` and `git status` — commits since the tracker's "last
     updated" line? Uncommitted work someone left behind?
   - The open PR's state (it may have been merged, closed, or picked up comments).
   If the tracker and the repo disagree, the repo wins. Say so plainly and correct
   the file — a silently stale tracker is the main failure mode here.
3. **Lead with what's actionable.** Open with the 2–4 things that can move *right
   now* without the client, then separately name what's blocked on Mike or the
   office manager. The user often has a spare hour and no new client info; tell
   them what's doable in that hour.
4. **Don't re-litigate settled decisions.** The Decisions Locked section exists so
   the logo, the plural company name, and the palette don't get reopened every
   session. If you think a locked decision is wrong, say why once, then respect it.

---

## Wrap Up

The user is stopping. Leave the repo and the tracker in a state that a version of you
with no memory of this conversation could resume from cleanly.

1. **Land the work.** `git status` — if anything is uncommitted, commit it with a
   real message and push to the working branch. Never leave a session with
   uncommitted changes; this container is ephemeral and the work would be lost.
   If something is half-finished and shouldn't be committed as-is, commit it anyway
   on the branch and write the caveat into the tracker's In Flight section — losing
   it is strictly worse than a messy commit on a draft branch.
2. **Update `PROJECT-STATUS.md`.** Keep the section order stable (see Structure
   below) so diffs between sessions are readable. Specifically:
   - Move anything that became real out of Placeholder into Real.
   - Add any new open question to Waiting On, attributed to whoever can answer it.
   - Add any decision the user made this session to Decisions Locked, with the
     one-line reason. Reasons are what stop a decision being relitigated.
   - Refresh the "last updated" line and the current commit.
   - Delete stale entries. This file earns its keep by being short and true; an
     append-only pile of history does not help the user.
3. **Verify before claiming.** If you say a page is done or a link works, you should
   have actually loaded it this session. Prefer "built, not yet viewed in a browser"
   over an unverified "done."
4. **Give the user a short spoken summary** — what moved, what's now waiting on the
   client, and the single most useful next step. Then stop. Don't start new work.

---

## PROJECT-STATUS.md structure

Keep these sections, in this order. They're chosen so the two questions the user
actually has — *what can I do right now?* and *what am I still waiting on?* — are
answerable from the top of the file.

```markdown
# Project Status
<!-- one-line: last updated date, current branch, current commit, PR link -->

## Where This Stands
<!-- 2-4 sentences of plain-language orientation -->

## Next Up
<!-- ordered, actionable without the client -->

## Waiting On The Client
<!-- grouped by who can answer: Mike (owner) / office manager / either -->

## Content: Real vs Placeholder
<!-- per page, what's genuinely confirmed vs still invented -->

## Decisions Locked
<!-- decision + one-line why, so it doesn't get reopened -->

## Constraints That Bite
<!-- Bell + NASA trademark rules, unverified claims, anything with legal edges -->

## In Flight
<!-- anything half-done, with enough detail to resume; usually empty -->
```

---

## Things specific to this project, worth not forgetting

These recur every session and are easy to get wrong from a cold start:

- **The company name is plural.** "South Air Helicopters, Inc." is the legal name,
  confirmed off the owner's business card. Never write the singular; the repo is
  named `SouthAirHelicopter` and that name is a trap.
- **Bell and NASA are other people's trademarks.** The company is a Bell Customer
  Service Facility and does NASA-adjacent work, but neither logo may appear on the
  site without written permission, and the copy must not imply endorsement. Both
  pages carry standing warnings — don't quietly remove them to make a page look
  finished.
- **Placeholders are load-bearing.** The dashed amber `[PLACEHOLDER: ...]` blocks are
  the mechanism that stops invented content reaching a real customer. Filling one in
  with a plausible-sounding guess is the worst available outcome. If content isn't
  confirmed, it stays flagged.
- **The contact form doesn't send anywhere.** Until it's wired to a real handler,
  a customer filling it in reaches nobody. This is the highest-severity item on the
  site and shouldn't slide down the list.
- **Contact details are temporary.** The sbcglobal/att.net addresses get replaced
  once the Google domain and Workspace email exist. When that happens they change in
  the footer of all 7 pages plus `contact.html`.
- **The nav and footer are copy-pasted across all 7 pages.** There's no templating
  layer, so a header or footer change is a 7-file change. Verify all seven.
- **Nothing is client-approved yet.** The user has signed off on the logo; Mike has
  not. Keep "approved by the user" and "approved by the owner" distinct in the
  tracker — conflating them could put unapproved work in front of a paying client.
