/*
Write a function take_umbrella() that takes two arguments: a string representing
the current weather and a float representing the chance of rain today.

Your function should return True or False based on the following criteria.

    You should take an umbrella if it's currently raining or if it's cloudy 
    and the chance of rain is over 0.20.
    
    You shouldn't take an umbrella if it's sunny unless it's more likely to 
    rain than not.

The options for the current weather are sunny, cloudy, and rainy.

For example, take_umbrella('sunny', 0.40) should return False.

As an additional challenge, consider solving this kata using only logical 
operaters and not using any if statements.


*/
const takeUmbrella = (weather, chance) => {
    if (weather === 'rainy') {
        return true;
    } else if (weather === 'cloudy') {
        if (chance > 0.2) {
            return true;
        }
        return false;
    } else {
        if (chance > 0.5) {
            return true;
        }
        return false;
    }
}

console.assert(takeUmbrella('sunny', 0.4) === false);
console.assert(takeUmbrella('rainy', 0) === true);
console.assert(takeUmbrella('cloudy', 0.2) === false);