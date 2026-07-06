EX\_06JUL - Elevator Floor Request Simulator

An elevator starts at the ground floor (0). Throughout the day, people press buttons requesting floors. Your program processes these requests in the order they come in (not sorted — this isn't a scheduling optimizer, just a simulator) and reports on the elevator's journey.



Requirements

&#x20;- Ask the user for a comma-separated list of floor requests (e.g. 3, 1, 5, 0, 2).

&#x20;- The building has floors 0 to 10 (0 = ground). Any request outside that range should be rejected — print a message and skip it, don't crash.

&#x20;- Starting from floor 0, process each valid request in order:

&#x20;  -> Print which stop number this is (1st, 2nd, 3rd...) using enumerate()

&#x20;  -> Print whether the elevator is going UP or DOWN to get there

&#x20;  -> Print how many floors it traveled for that leg



At the end, print:

&#x20;- The total number of floors traveled across the whole day

&#x20;- The highest floor reached

&#x20;- The lowest floor reached

