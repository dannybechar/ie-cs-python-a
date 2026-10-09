# Follow-up on the ChatGPT review (Claude's triage)

Reviewer: OpenAI model (gpt-5.6-sol, via the Codex CLI), given both tests, both keys and the three lesson notes. Full report: [`REVIEW-REPORT.md`](REVIEW-REPORT.md).

## Rejected
- **"Version B Q14 key is wrong (should be ג, key says ד)"**: false positive. The key already says ג (4x20 + 3x10 = 110), in the data and in the Word file. The report's own table has the key letters misaligned for B13/B14.
- **"A4 and B18 need `import turtle` stated"**: the test's instruction 4 already says import/setup are omitted from the code. (B18 was still reworded, see below.)

## Accepted and fixed (both versions rebuilt)
- A Q10: now asks which line *sets the pen color* to red (the old wording said the line "colors the line").
- A Q15: removed the incorrect "the turtle starts on the left" remark.
- A Q21: new program. It reused Q20's broken-square code, so Q20 gave away the reasoning.
- A key Q15: grammar typo ("שמציירים").
- B Q18: states that the file starts with the usual setup lines and ends with `turtle.done()`.
- B Q19: consistent second person ("שחזיתם").
- B Q20: replaced. It duplicated B Q6 (right-to-left swap); it is now a rectangle with one wrong turn.
- A Q16 / B Q16: "לפי הסדר" added to the Shell-output questions.

## Not changed (your call)
- Weak distractors (A18, B19, B4, B10), repeated lab-example wording, and the F/L/R shorthand in the rectangle questions.
- The reviewer doubts the "only 1-2 above 90%" goal because many items are direct recall. That is fair: run a pilot or compare the first class's results, then swap 3-4 recall items for 6-8 instruction traces if too many pass 90.
- Difficulty labels and the 70 average / 38 minutes are estimates, not measurements.
