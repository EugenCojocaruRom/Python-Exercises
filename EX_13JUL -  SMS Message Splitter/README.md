EX\_13JUL - SMS Message Splitter

Some text messages are longer than a carrier's character limit, so they get split into numbered parts, like (1/3) Hey, are we (2/3) still on...



Requirements:

&#x20;- Ask the user to input a message.

&#x20;- Ask for a max character limit per part (e.g. 20).

&#x20;- Split the message into as many parts as needed so each part (including the (x/y)  prefix!) doesn't exceed the limit.

&#x20;- Try to split on word boundaries where possible (don't cut a word in half) — though if you want to keep it simpler at first, splitting by raw character count is a totally fine first pass.

&#x20;- Print each part on its own line, properly numbered, e.g.:



&#x20;  (1/3) Hey, are we

&#x20;  (2/3) still on for

&#x20;  (3/3) today at 5?

