# Unit 2 written test (Form A): review of revision 1 and what was done

ChatGPT reviewed revision 1 of the 60-minute written turtle-basics test, mainly its time estimate. The request asked for a per-item time estimate and the smallest changes that fit 60 minutes; it contained the full test with answers and rubrics. The reviewer's report was pasted into the chat and is not stored here; this file records the findings and decisions.

## Findings and decisions

| Finding | Decision |
|---|---|
| Revision 1 takes about 69 min for an average student (teacher's estimate was 66); too long for 60 min. Questions 3, 4 and 6 are heavier than estimated, 1 and 2 lighter. Ranges: strong student ~42 min, weak student ~100 min | Accepted. Revision 2 removes drawings from five items; estimate is now about 62 min. Still an unmeasured estimate; a pilot with 3 students (strong, average, weak) is the open item |
| Item 4ב path leaves the 8×5 grid ("critical") | **Rejected, false positive.** Start is column 4 (0-based 3); the path goes 2 right, 2 up, 4 left and ends in column 2. The builder walks every drawing and throws if one leaves its grid, and the key's solved grid shows it fitting |
| Grids on multiple-choice items 1א, 2א, 2ג, 2ד repeat what the chosen answer shows | Accepted: grids removed there |
| 4א and 4ג: drawing adds load without a new concept | Accepted: 4א grid removed, 4ג is words only. Points restored to the original rubric lines |
| Shorten the opening instructions | Accepted: 8 items cut to 7, hints merged |
| One small solved example of a grid drawing is missing | Accepted: worked example added to the instructions page (code, empty grid, solved grid) |
| 3ב: "distance from start" can be confused with total path length | Accepted: wording now says "במרחק בקו ישר" |
| Hints on the instruction page give away 1ב, 1ג, 2ב | Left as is: hints are a design rule of this test (see unit README) |
| Drawing parts should give partial credit per segment | Already so in the rubrics; kept |

## Other changes in revision 2 (teacher feedback, not from the reviewer)

- 1א replaced: a student claims the line points up because `left` follows `forward`; tests understanding instead of syntax.
- Code-analysis items with a drawing show the code on the right and an empty grid on the left; every grid has a start arrow and a stated step size per square.
- The test is printed and scanned in black and white: no colors, bold black headings, black grid lines. The key uses grey squares.
