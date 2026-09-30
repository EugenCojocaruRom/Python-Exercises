EX\_30SEP - Caesar Cipher Encoder - Decoder

Write a program that shifts letters in a message by a fixed number of positions in the alphabet.



Part 1: Encode

Write a function encode(message, shift) that returns the encoded message.

&#x20;- Letters move forward by shift positions, wrapping around after z (so x with shift 3 becomes a).

&#x20;- Keep uppercase letters uppercase and lowercase letters lowercase.

&#x20;- Leave spaces, digits, and punctuation unchanged.



Part 2: Decode

Write decode(message, shift) that reverses the encoding. Try to reuse encode instead of writing new logic.



Part 3: Changed positions

Write changed\_positions(original, encoded) that uses enumerate() and a list comprehension to return a list of the indexes where the two strings differ.



Part 4: Brute force

Given an encoded message, print all 25 possible decodings (shifts 1 to 25), one per line.

Find the shift that gives a readable message.

