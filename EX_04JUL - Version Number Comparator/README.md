EX\_04JUL - Version Number Comparator

You get two version strings, like "1.4.2" and "1.4.10". Your job: figure out which one is newer, treating each dot-separated segment as a number, not text (so 10 > 2, even though as strings "10" < "2" alphabetically would trip you up if you weren't careful).



Requirements:

&#x20;- Split each version string into its numeric parts (list comprehension is a natural fit here).

&#x20;- Handle versions with different numbers of parts, e.g. "1.4" vs "1.4.0.1" — treat missing parts as 0.

&#x20;- Compare part by part (this is where enumerate() or zip() could help) and determine: is version A greater, is version B greater, or are they equal?

&#x20;- Print a clear result, like "1.4.10 is newer than 1.4.2".



For test:

("1.4.2", "1.4.10")   -> second is newer

("2.0", "1.9.9")      -> first is newer

("1.0.0", "1.0")      -> equal

("3.1.4", "3.1.4.1")  -> second is newer

