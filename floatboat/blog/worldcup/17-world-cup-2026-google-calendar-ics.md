---
title: "Add World Cup 2026 to Google, Outlook & Apple (ICS)"
description: "Add World Cup 2026 fixtures to Google, Outlook & Apple Calendar. ICS import guide, subscription URL setup, and FloatCup one-click sync with reminders."
slug: "world-cup-2026-google-calendar-ics"
date: 2026-06-25
author: "Floatboat"
category: "World Cup"
secondaryCategory: "Product"
---

## TL;DR

- Download and import an **ICS file** (~2 minutes) to add all 104 matches to Google Calendar, Outlook, or Apple Calendar — free, works everywhere, but static if FIFA changes kickoff times.
- Subscribe via an **ICS URL** for periodic auto-refresh without re-importing — refresh frequency depends on the provider.
- Use **FloatCup** for one-click subscription with automatic match-time updates and pre-configured reminders — no file download required.
- Create a dedicated **"World Cup 2026" calendar layer** before importing so you can toggle or delete all match events in one step after the tournament.

---

## 1. ICS vs. PDF vs. Copy-Paste: Why Calendar Sync Wins

There are three ways to keep a match schedule, and only one of them actively helps you not miss a kickoff.

| Approach | Effort to Set Up | Stays Updated | Time Zone Handling | Reminders |
|----------|:---:|:---:|:---:|:---:|
| **PDF printout or screenshot** | Low | No — re-download when times change | Manual conversion | None |
| **Manual copy-paste into calendar** | High — 104 events × ~45 seconds each ≈ 78 minutes | Only if you redo it | You set it per event | You set it per event |
| **ICS import (one file)** | Low — ~2 minutes | No — re-import for changes | Automatic (if file includes timezone) | Configurable per event or in bulk |
| **Calendar subscription (FloatCup)** | Lowest — ~30 seconds | Yes — updates automatically | Automatic | Included (30 min / 1 hr / 3 hr options) |

The ICS file is the baseline: it is free, it works everywhere, and it saves you from typing 104 events by hand. A calendar subscription goes one step further by handling the one thing a static file cannot — what happens when a match time changes.

During the group stage, FIFA occasionally shifts kickoff times for broadcast optimization. If you imported a static ICS file, those changes do not appear in your calendar unless you re-import. A subscription keeps you in sync without any extra work.

---

## 2. Method 1: Import an ICS File (Google Calendar)

Google Calendar supports ICS import natively. The process takes about two minutes.

### Step 1: Download the ICS file

Several providers distribute free World Cup 2026 ICS files. CalendarLabs, Yahoo Sports, and FotMob all offer downloadable `.ics` or `.zip` files with the full 104-match schedule, as listed on [CalendarLabs](https://calendarlabs.com/ical-calendar/ics/subscribe/196/FIFA_World_Cup). Look for a file that specifies your time zone in the filename (e.g., `world-cup-2026-edt.ics`) — this makes the import cleaner because Google Calendar reads the time zone from the file.

*If the file comes as a `.zip`, unzip it first. Right-click → "Extract All" on Windows, or double-click on Mac.*

### Step 2: Create a dedicated calendar (recommended)

Before importing, create a separate calendar called "World Cup 2026." This keeps all 104 match events in their own layer — you can toggle the whole tournament on or off without cluttering your main calendar with football matches alongside work meetings.

In Google Calendar (web): left sidebar → "Other calendars" → click the "+" → "Create new calendar" → name it "World Cup 2026" → "Create calendar."

### Step 3: Import the ICS file

1. In Google Calendar, click the gear icon (top right) → **Settings**
2. In the left menu, select **Import & Export** — see <a href="https://support.google.com/calendar/answer/37118" rel="nofollow noopener">Google Calendar import help</a> for the full walkthrough
3. Click **Select file from your computer** and choose your `.ics` file
4. Under **Add to calendar**, select "World Cup 2026" (or your main calendar)
5. Click **Import**

Google Calendar processes the file and adds all 104 matches as individual events. Each event includes the teams, venue, and kickoff time. You can now search for "Brazil" or "Semifinal" in your calendar and find the relevant matches instantly.

**One limitation to know**: imported ICS events are static. If a match time changes, you need to delete the old events and re-import an updated file. For automatically-updating events, see Method 4 (FloatCup) in section 6 below.

---

## 3. Method 1b: Subscribe via URL (ICS Link)

If the provider offers a subscription URL rather than a downloadable file, the setup is even simpler:

1. In Google Calendar, left sidebar → "Other calendars" → click "+" → **From URL**
2. Paste the ICS subscription URL
3. Click **Add Calendar**

The matches appear as a separate calendar layer. Google Calendar checks subscription URLs periodically for updates, though the refresh frequency varies. This approach is better than a one-time import for keeping match times current, assuming the URL provider updates the source file when FIFA adjusts the schedule.

---

## 4. Method 2: Import into Outlook

Microsoft Outlook supports ICS import across desktop, web, and mobile versions.

### Outlook Desktop (Windows / Mac)

1. Click **File** → **Open & Export** → **Import/Export**
2. Select **Import an iCalendar (.ics) or vCalendar (.vcs) file** → Next
3. Browse to your `.ics` file and select it
4. Choose **Open as New** to create a separate calendar, or **Import** to merge into your main calendar
5. Click **OK**

The matches appear in a new calendar tab within Outlook. You can overlay it with your main calendar to see match times alongside your work schedule.

### Outlook Web (outlook.office.com)

1. Click the calendar icon → **Add calendar** (left sidebar)
2. Select **Upload from file**
3. Choose your `.ics` file
4. Select the destination calendar → **Import**

### Outlook Mobile

On iOS and Android, the approach is slightly different: you typically open the `.ics` file from your email or file manager, and the system prompts you to add events to your default calendar app. Outlook mobile reads from the same calendar database as your phone's built-in calendar app, so importing at the system level makes the events visible in Outlook as well.

---

## 5. Method 3: Import into Apple Calendar (Mac / iPhone / iPad)

Apple Calendar reads ICS files natively on all Apple devices.

### On Mac

1. Double-click the `.ics` file in Finder
2. Calendar.app opens and shows a preview of the events
3. Choose the calendar to add them to (create a new "World Cup 2026" calendar first via File → New Calendar)
4. Click **OK**

### On iPhone or iPad

1. Open the `.ics` file from an email attachment, a downloaded file in Safari, or from Files.app
2. Tap the file — a preview appears with an **Add All** button at the top
3. Tap **Add All**, then select which calendar to add the events to
4. Tap **Done**

All 104 events appear in Apple Calendar and sync across your iCloud-connected devices automatically.

### Subscribe via URL on Apple Calendar

Apple Calendar also supports calendar subscriptions — see <a href="https://support.apple.com/guide/calendar/subscribe-to-calendars-icl1022/mac" rel="nofollow noopener">Apple Calendar subscription help</a>:
1. Mac: File → New Calendar Subscription → paste the URL → Subscribe
2. iPhone/iPad: Settings → Calendar → Accounts → Add Account → Other → Add Subscribed Calendar → paste the URL

Subscribed calendars auto-refresh, similar to Google Calendar's "From URL" method.

### Android: Import into Google Calendar

On Android, Google Calendar is typically the default calendar app, and the import process differs slightly from the desktop version:

1. Download the `.ics` file to your phone — either from an email attachment, a web download, or a file shared via a messaging app
2. Open the **Google Calendar** app
3. Tap the **+** button (bottom right) → **Event** → tap the three-dot menu → **Import .ics file**
4. Navigate to the downloaded file and select it
5. Choose which calendar to import into (create a "World Cup 2026" calendar first via Settings → Manage calendars → Add calendar)
6. Confirm the import — all 104 matches appear

If the Google Calendar app does not show the import option, an alternative is to email the `.ics` file to your Gmail address and open it from the Gmail app on your phone — Gmail automatically previews `.ics` attachments and offers an "Add to calendar" button that handles the import without navigating calendar settings.

For Samsung Calendar users: the app supports `.ics` import through Settings → Manage calendars → Import. Download the `.ics` file, open Samsung Calendar, and use the import function to add all events.

---

## 6. Method 4: FloatCup — One Click, Auto-Updating

If you do not want to download files, unzip archives, or re-import when schedules shift, FloatCup handles the entire process in one step.

FloatCup is a free calendar subscription service built on Floatboat's Calendar-Driven AI. Instead of importing a file, you subscribe once. The 104-match schedule appears in your calendar within seconds. When FIFA adjusts a kickoff time — which happens occasionally during the group stage — the change appears in your calendar automatically. No re-download. No re-import. Official fixture data is published by <a href="https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums" rel="nofollow noopener">FIFA</a>.

FloatCup also includes match reminders. You choose the lead time — 30 minutes, 1 hour, or 3 hours before kickoff — and FloatCup notifies you through your calendar's standard reminder system. After the tournament, you unsubscribe with one click, and the events are removed.

**What FloatCup adds beyond a basic ICS file**:
- Match times update automatically when FIFA adjusts the schedule
- Reminders are pre-configured — no manual setup per match
- Post-match recap links appear in your Floatboat workspace after each game
- Timezone conversion is automatic regardless of where you are

**Subscribe with FloatCup** — the subscribe button on the FloatCup page adds all matches to your calendar in one click.

---

## 7. Troubleshooting Common ICS Import Problems

ICS imports usually work on the first try, but a few common issues can trip up the process. Here is what to check if the matches do not appear as expected.

**Events imported but times are wrong.** The ICS file likely lacks timezone metadata, or your calendar app imported it without applying the correct conversion. Solution: look for an ICS file that explicitly specifies a timezone in the filename (e.g., `world-cup-2026-edt.ics`) and re-import. Delete the old events first to avoid duplicates.

**Import appears to succeed but no events show up.** You may have imported into the wrong calendar layer, or the `.ics` file was corrupted during download. Check that the destination calendar you selected during import is visible (toggle it on in your calendar app's sidebar). If it still does not appear, re-download the file from a different source and try again. Google Calendar sometimes silently fails on ICS files with encoding issues — trying a file from another provider often resolves this.

**Duplicate events after re-importing.** If you imported the schedule, then re-imported an updated version without deleting the old events, your calendar will show two copies of every match. Solution: before re-importing, delete the existing "World Cup 2026" calendar entirely (right-click the calendar name in Google Calendar → Settings → Remove calendar) and re-import the new file into a fresh calendar. This is another reason to use a dedicated calendar layer rather than importing into your main calendar.

**Google Calendar says "0 events imported."** The ICS file may be inside a `.zip` archive that you have not extracted. Unzip the file first (right-click → "Extract All" on Windows, double-click on Mac), then import the `.ics` file inside. If the `.ics` file is valid but Google Calendar still shows 0 events, try the subscription URL method (Method 1b) instead — it bypasses the file import entirely.

---

## 8. Which Method Should You Use?

For readers who want to understand the tournament format and context before importing the schedule, start with the <a href="/blog/world-cup-2026-guide">World Cup 2026 overview</a>.

| If you... | Use |
|-----------|-----|
| Want the schedule in your calendar with zero ongoing effort | **FloatCup** (Method 4) |
| Prefer a one-time import and do not mind re-importing if times change | **ICS file import** (Method 1 or 2) |
| Want a subscription that auto-refreshes without a Floatboat account | **ICS subscription URL** (Method 1b or Apple Calendar subscription) |
| Only need to look up a match time occasionally | The [full schedule page](/blog/world-cup-2026-schedule) |

The first three methods are not mutually exclusive. You can subscribe with FloatCup for automatic updates and reminders, and also keep a printed view from your calendar app for quick reference.

---

## 9. Conclusion

For most readers, the choice comes down to maintenance. A one-time ICS import takes two minutes and works on every major platform — Google Calendar, Outlook, and Apple Calendar all handle `.ics` files natively. If FIFA adjusts a kickoff during the group stage, you re-import. That is fine if you check the schedule weekly.

If you want zero upkeep — automatic timezone conversion, live kickoff updates, and pre-match reminders without configuring 104 events — FloatCup is the simpler path. Subscribe once, and the calendar handles the rest through the final on July 19.

Either way, create a dedicated "World Cup 2026" calendar layer before you import or subscribe. It keeps 104 match events separate from work meetings and makes cleanup after the tournament a single delete.

---

## FAQ

### Does importing an ICS file add all 104 matches at once?
Yes. An ICS file for the World Cup contains all 104 matches as individual calendar events. Importing one file adds every match — group stage, knockout rounds, and the final — in a single operation.

### Will the match times display in my local time zone?
If the ICS file includes timezone data (most do), your calendar app converts kickoff times to your local time automatically. If you are unsure, check one imported event against the official match time — if it shows the stadium's local time instead of yours, the file may lack timezone metadata, and you should look for a version that specifies a timezone.

### What happens if FIFA changes a match time after I import the ICS file?
Static ICS imports do not update. You need to delete the old events and re-import an updated file. Calendar subscriptions — URL-based or FloatCup — update automatically.

### Can I import the schedule into multiple calendar apps?
Yes. The same ICS file works in Google Calendar, Outlook, and Apple Calendar. You can import it into each platform separately. If you use multiple devices, importing once on a platform that syncs (Google, iCloud) is usually sufficient.

### How do I remove the World Cup events after the tournament?
If you imported into a dedicated calendar (recommended), delete the entire calendar in one step. In Google Calendar: Settings → the calendar name → Remove calendar. If you subscribed via FloatCup, use the one-click unsubscribe. If you imported into your main calendar, you will need to delete events in bulk — another reason to use a dedicated calendar layer.

### What should I do if the import succeeds but no events appear?

First check that the destination calendar you imported into is visible — toggle it on in your calendar app's sidebar. If it still shows nothing, the `.ics` file may be corrupted or lack valid event data; re-download it from a different provider and try again. Google Calendar can also silently fail on files with encoding issues, in which case the subscription URL method bypasses file import entirely. If you see "0 events imported," you likely forgot to unzip a `.zip` archive first.
