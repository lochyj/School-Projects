# Covid simulations

## Steps

1. Estimate α
2. Create simple simulation
3. Make the simulation more intricate
4. Expand the size / scale of the simulation
5. Optimize the simulation so it can actually run

## Estimating α

As this requires what is essentially finding the interest rate of
the balance of the initial population over the time period of 29 days
that compounds to lead to the final amount, we need mathematica.
To estimate the value, we of course need the formula for compound interest:
`A=P(1+r/n)^(nt)`
where in our case, A = 12741386, P = 7769783, r is unknown, n is 1 and t is 29.
n can also be 29, where t is 1 but I chose t to be the counter for the number of days.

```wl
principal_amount = 7769783;
final_amount = 12741386;
Solve[final_amount == principal_amount * (1 + x)^29, x, Reals]
```

This then gives us:
`x -> 0.0172019` where `x == α`!

## Creating a simple simulation

The basic simulation will have a single region with a number of actors in it.
The actors will randomly interact and using the `α` value we found earlier, will
spread covid-19 to other actors they interact with if they are infected.

## Making the simulation more intricate

Firstly, we can improve the accuracy of our simulation by introducing immunity
to the actors once they have recovered from covid-19 for a random period of
2 - 12 weeks with a immunity percentage from 50% - 100% that reduces their
chance to catch covid-19 by that percentage when they interact with an
infected agent.

## Expanding and optimizing the simulation

For us to effectively simulate the entire world population and some fake cities, we need to optimize our simulation, otherwise it will take until the end of time to simulate.
